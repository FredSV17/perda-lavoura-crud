import { DatePipe } from '@angular/common';
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


@Component({
  selector: 'app-list-loss',
  templateUrl: './list-loss.component.html',
  styleUrls: ['./list-loss.component.scss']
})
export class ListLossComponent implements OnInit {
  ELEMENT_DATA: any = [];
  load_table:boolean = false;
  displayedColumns: string[] = ['producer_name','producer_cpf','harvest_date','event_type','crop_type','ações'];
  dataSource: any = [];
  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private lossService: LossService,
    public datePipe: DatePipe  ) {}

  async ngOnInit() {
    await this.call_list_loss()
  }

  async call_list_loss(){
    await (await this.lossService.list_loss()).subscribe((response) => {
      console.log(response.entries)
      this.ELEMENT_DATA = response.entries
      // this.ELEMENT_DATA.harvest_date = 
      this.dataSource = this.ELEMENT_DATA;
      this.load_table = true;
    });
  }

  async call_list_loss_by_cpf(cpf: string){
    await (await this.lossService.list_loss_by_cpf(cpf)).subscribe((response) => {
      console.log(response.entries)
      this.ELEMENT_DATA = response.entries
      this.dataSource = this.ELEMENT_DATA;
      this.load_table = true;
    });
  }


  search_for:string = "";
  async search_input(event: any){
    this.search_for = event.target.value
  }

  async search_cpf(){
    this.load_table = false;
    console.log(this.search_for)
    if (this.search_for == ""){
      await this.call_list_loss()
    }
    else{
      await this.call_list_loss_by_cpf(this.search_for)
    }
  }

  goto_create(){
    this.router.navigate(['/create']);
  }

  edit(id: string){
    this.router.navigate(['/edit',id]);
  }
  detail(id: string){
    this.router.navigate(['/detail',id]);
  }
  delete(id: string){
    this.router.navigate(['/delete',id]);
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