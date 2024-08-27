from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import csv
import subprocess

app = Flask(__name__)
CORS(app)  # Habilitar CORS para todos los endpoints

# Conectar a la base de datos SQLite
conn = sqlite3.connect('form_data.db', check_same_thread=False)
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS forms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        message TEXT NOT NULL
    )
''')
conn.commit()

@app.route('/submit', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        data = request.json
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')

        # Insertar los datos en la base de datos
        cursor.execute('INSERT INTO forms (name, email, message) VALUES (?, ?, ?)', (name, email, message))
        conn.commit()

        return jsonify({'message': 'Form data saved successfully'}), 200

    return jsonify({'message': 'Error saving form data'}), 400

@app.route('/export-to-csv', methods=['GET'])
def export_to_csv():
    try:
        cursor.execute('SELECT * FROM forms')
        data = cursor.fetchall()

        # Escribir los datos en un archivo CSV
        with open('form_data.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'name', 'email', 'message'])
            writer.writerows(data)

        return jsonify({'message': 'Data exported to CSV successfully'}), 200

    except Exception as e:
        return jsonify({'message': f'Error exporting data to CSV: {str(e)}'}), 500

@app.route('/import-to-mongodb', methods=['GET'])
def import_to_mongodb():
    try:
        # Exportar a CSV primero
        cursor.execute('SELECT * FROM forms')
        data = cursor.fetchall()

        with open('form_data.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'name', 'email', 'message'])
            writer.writerows(data)

        # Importar a MongoDB
        # Asumiendo que tienes MongoDB instalado localmente y ejecutándose
        mongoimport_command = ['mongoimport', '--db', 'mydatabase', '--collection', 'forms', '--type', 'csv', '--file', 'form_data.csv', '--headerline']
        result = subprocess.run(mongoimport_command, capture_output=True, text=True)

        if result.returncode == 0:
            return jsonify({'message': 'Data imported to MongoDB successfully'}), 200
        else:
            return jsonify({'message': 'Error importing data to MongoDB', 'error': result.stderr}), 500

    except Exception as e:
        return jsonify({'message': f'Error importing data to MongoDB: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
