import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';
import { Observable, Subscription } from 'rxjs';
import { LossService } from 'src/app/services/loss.service';

// {position: 1, name: 'Hydrogen', weight: 1.0079, symbol: 'H'},
// {position: 2, name: 'Helium', weight: 4.0026, symbol: 'He'},
// {position: 3, name: 'Lithium', weight: 6.941, symbol: 'Li'},
// {position: 4, name: 'Beryllium', weight: 9.0122, symbol: 'Be'},
// {position: 5, name: 'Boron', weight: 10.811, symbol: 'B'},
// {position: 6, name: 'Carbon', weight: 12.0107, symbol: 'C'},
// {position: 7, name: 'Nitrogen', weight: 14.0067, symbol: 'N'},
// {position: 8, name: 'Oxygen', weight: 15.9994, symbol: 'O'},
// {position: 9, name: 'Fluorine', weight: 18.9984, symbol: 'F'},
// {position: 10, name: 'Neon', weight: 20.1797, symbol: 'Ne'},
let ELEMENT_DATA: any;

@Component({
  selector: 'app-list-loss',
  templateUrl: './list-loss.component.html',
  styleUrls: ['./list-loss.component.css']
})
export class ListLossComponent implements OnInit {

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private lossService: LossService  ) {}

  async ngOnInit() {
    const response = await this.lossService.list_loss();
    console.log(response)
    // ELEMENT_DATA = response.entries
    // console.log(response)
  }

  displayedColumns: string[] = ['producer_name'];
  //, 'name', 'weight', 'symbol'
  dataSource = ELEMENT_DATA;

  goto_create(){
    this.router.navigate(['/create']);
  }
}

// constructor(
//   private route: ActivatedRoute,
//   private router: Router  ) {}

// // ngOnInit() {
// //   const heroId = this.route.snapshot.paramMap.get('id');
// //   this.hero$ = this.service.getHero(heroId);
// // }

// gotoItems(hero: Hero) {
//   const heroId = hero ? hero.id : null;
//   // Pass along the hero id if available
//   // so that the HeroList component can select that item.
  
// }