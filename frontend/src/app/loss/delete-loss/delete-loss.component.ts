import { DatePipe } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { LossService } from 'src/app/services/loss.service';

@Component({
  selector: 'app-delete-loss',
  templateUrl: './delete-loss.component.html',
  styleUrls: ['./delete-loss.component.scss']
})
export class DeleteLossComponent implements OnInit {

  constructor(private route: ActivatedRoute,
    private router: Router,
    private lossService: LossService,
    private datePipe: DatePipe) { }

  loss_id: number = 0;
  loss: any;
  async ngOnInit() {
    this.route.params.subscribe(params => {
      this.loss_id = +params['id']
      console.log(this.loss_id)
    });

    await (await this.lossService.get_loss(this.loss_id)).subscribe((response) => {
      console.log(response)
      this.loss = {producer_name: response.producer_name,
                producer_email: response.producer_email,
                producer_cpf: response.producer_cpf,
                crop_local: response.crop_local,
                harvest_date: this.datePipe.transform(response.harvest_date,'dd/MM/yyyy'),
                crop_type: response.crop_type,
                event_type: response.event_type}
    });
  }
  back(){
    this.router.navigate(['/']);
  }

  async delete(){
      await (await this.lossService.delete_loss(this.loss_id)).subscribe()
      this.router.navigate(['/']);
  }
}
