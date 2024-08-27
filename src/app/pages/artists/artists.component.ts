import { AfterViewInit, Component, ElementRef, QueryList, ViewChildren } from '@angular/core';

@Component({
  selector: 'app-artists',
  templateUrl: './artists.component.html',
  styleUrls: ['./artists.component.css']
})
export class ArtistsComponent implements AfterViewInit{
  @ViewChildren('scrollEffect') images!: QueryList<ElementRef>;

  private observer!: IntersectionObserver;
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
