import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { AboutComponent } from './pages/about/about.component';
import { ArtistsComponent } from './pages/artists/artists.component';
import { ContactComponent } from './pages/contact/contact.component';

const routes: Routes = [
{
    path: '',
    component: HomeComponent
},
{
    path: 'about',
    component: AboutComponent
},
{
    path: 'artists',
    component: ArtistsComponent
},
{
    path: 'contact',
    component: ContactComponent
},
{
    path: '**',
    redirectTo: ''
},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
