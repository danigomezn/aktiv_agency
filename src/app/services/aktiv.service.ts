import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';
import { DjInterface } from '../components/interfaces/dj-interfaces';

@Injectable({
  providedIn: 'root'
})
export class AktivService {
private http= inject(HttpClient)

  constructor() {
   }
public getAllDjs(): Observable<DjInterface[]> {
return this.http.get<DjInterface[]>('http://localhost:8000/djs')

   }
}
