import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.css']
})
export class ContactComponent {

  formData = {
    name: '',
    email: '',
    message: ''
  };

  constructor(private http: HttpClient) { }

  onSubmit() {
    console.log('Form data:', this.formData);

    this.http.post<any>('http://localhost:5000/submit', this.formData).subscribe({
      next: () => {
        window.location.reload()
      },
      error: (error) => {
        console.error('Error submitting form data', error);
      }
    });
  }

}
