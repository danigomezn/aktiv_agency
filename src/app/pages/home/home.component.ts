import { AfterViewInit, Component, ElementRef, OnInit, QueryList, ViewChildren, inject } from '@angular/core';
import { DjInterface } from 'src/app/components/interfaces/dj-interfaces';
import { AktivService } from 'src/app/services/aktiv.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements AfterViewInit, OnInit{



  @ViewChildren('scrollEffect') images!: QueryList<ElementRef>;

  private observer!: IntersectionObserver;
  private djService : AktivService = inject(AktivService)
  public djs : DjInterface[] = []

    ngOnInit(): void {

      this.djService.getAllDjs().subscribe({
        next: response => this.djs = response,
        error: () => console.log('No se ha podido conectar')
      })
      console.log(this.djs)
  }

  ngAfterViewInit() {
    this.observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          this.observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });

    this.images.forEach(image => {
      this.observer.observe(image.nativeElement);
    });
  }

}

