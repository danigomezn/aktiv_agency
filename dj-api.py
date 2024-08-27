from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware

# Modelo Pydantic para DJ
class DJ(BaseModel):
    id: int
    name: str
    genre: str
    description: str

# Inicializar la aplicación FastAPI
app = FastAPI()

# Configurar CORS
origins = [
    "http://localhost:4200",  # Origen de tu aplicación Angular
    # Puedes agregar otros orígenes si es necesario
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Datos de ejemplo de DJs
djs = [
    DJ(id=1, name="DANIGO", genre="REGGAETON - COMERCIAL - URBANO - AFROEBEAT - AFRO HOUSE - TECH HOUSE - HARD TECHNO", description="Se caracteriza por sus espectáculos enérgicos y la conexión que logra con el público. Desde que tenía 10 años comenzó su pasión por la música y ha tocado en los mejores clubs de Valencia donde reside actualmente, así como tambien tuvo una gira en Flordida (MIAMI) ha compartido cabina con artistas internacionales."),
    DJ(id=2, name="DANY MARIN", genre="REGGAETON - TRAP - R&B - AFROEBEAT - MOOMBAHTON - AFRO HOUSE - TECH HOUSE", description="Procedente de Medellin (Colombia). A sus 13 años comienza sus andaduras a los platos. siempre se ha sentido atraído por la música y es su gran pasión, se considera una persona soñadora, luchadora , muy emocional y creativa, que va en sintonía y evolución con la música y siempre da lo mejor de sí en sus sesiones. Además de su pasión como DJ, Dany Marín da sus primeros pasos como productor con la elaboración de Mashups y Remixes, faceta que expresa la ambición y proyección en busca de una constante evolución y crecimiento en el mundo de la música"),
    DJ(id=3, name="MONRA", genre="URBANO - AFRO HOUSE - TECH HOUSE - TRIBAL - GUARACHA - CIRCUIT", description="Conocido como Monra, hasta ahora en su breve pero destacada trayectoria profesional como DJ, está abriéndose camino a pasos agigantados en el panorama nocturno de Valencia. Dándose a conocer y dejando muy buen sabor de boca allá por donde pasa. A finales de 2022 firmó contrato con AktivAgency lo cual le supuso un gran salto en su carrera y le permite seguir escalando puestos... ¿Dónde estará su limite?"),
    DJ(id=4, name="RUBEN DIEGUEZ", genre="URBAN LATIN HITS - REGGAETON - URBANTECH - HIP HOP - DANCEHALL - RAP", description="Es un Dj, productor musical y locutor de radio, además de diseñador gráfico, el cuál se ha encargado del diseño de importantes portadas de discos (una de ellas disco de oro), así como carteles, flyers, creación y edición de vídeo y fotografia, animación 4D y todo lo relacionado con comunicación audiovisual. Su afición por la música empezó a muy temprana edad, comenzando su carrera de Dj a los 11 años pinchando en salas y discotecas de Córdoba"),
    DJ(id=5, name="PARIS", genre="URBANO - COMERCIAL - HIP HOP - AFROBEATS - DANCEHALL", description="Tras viajar continentes, adaptarse a culturas caribeña, sud americana & europea, PARIS DJ aprendió con el tiempo en hacer que la pista nunca deje de bailar. abrió conciertos en club de francia para Naza, Maitre Gims, Marwa Loud, Dj Mike one. Luego se instalo a Valencia en 2019, colaborando en su primer año con Caribbeans Avenue. Desde entonces, se le abrieron la puertas de grandes club de Valencia como Indiana, la Sala Madison, Dady’O, Upper Club, Mya."),
    DJ(id=6, name="ISMA GARRIDO", genre="REGGAETON - AFRO HOUSE - HOUSE - POP", description="Más conocido por su nombre artístico ISMAGARRIDO, es un DJ valenciano que ha ha destacado por su habilidad para mezclar house, reguetón y pop, creando sets vibrantes y memorables. Destaca por su versatilidad adaptándose a todo tipo de públicos y garantizando siempre una pista de baile llena de energía. También es conocido por su habilidad para crear una atmósfera única en sus actuaciones en vivo, donde combina una selección de pistas cautivadoras con una energía contagiosa que mantiene a la multitud en constante movimiento. "),
    DJ(id=7, name="JEEY B", genre="COMERCIAL - URBANO - TECH HOUSE - TECHNO", description="JeeyB  ha demostrado ser una figura destacada en la escena musical gracias a su dominio de los estilos urban, house y tech house. Con una habilidad excepcional para fusionar estos géneros, JeeyB ha creado sets dinámicos y llenos de energía que resuenan profundamente con sus audiencias. Especialmente reconocido por su maestría en el urban, house y tech house, JeeyB no solo se limita a estos estilos. Su versatilidad como DJ le permite adaptarse a todo tipo de público, garantizando siempre una experiencia única y memorable en la pista de baile. Esta capacidad de conectar con diversas audiencias y de mantener la energía en alto durante sus actuaciones ha consolidado su reputación."),
]

# Endpoint para obtener todos los DJs
@app.get("/djs/", response_model=List[DJ])
def get_djs():
    return djs

# Endpoint para obtener un DJ por su ID
@app.get("/djs/{dj_id}", response_model=DJ)
def get_dj(dj_id: int):
    dj = next((dj for dj in djs if dj.id == dj_id), None)
    if dj is None:
        raise HTTPException(status_code=404, detail="DJ not found")
    return dj

# Endpoint para crear un nuevo DJ
@app.post("/djs/", response_model=DJ)
def create_dj(dj: DJ):
    djs.append(dj)
    return dj

# Endpoint para actualizar un DJ existente
@app.put("/djs/", response_model=DJ)
def update_dj(dj: DJ):
    index = next((index for index, d in enumerate(djs) if d.id == dj.id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="DJ not found")
    djs[index] = dj
    return dj

# Endpoint para eliminar un DJ
@app.delete("/djs/{dj_id}", response_model=DJ)
def delete_dj(dj_id: int):
    index = next((index for index, d in enumerate(djs) if d.id == dj_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="DJ not found")
    deleted_dj = djs.pop(index)
    return deleted_dj

# Ejecutar la aplicación con Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
