import { DatePipe } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import {FormBuilder, FormControl, FormGroup, FormGroupDirective, NgForm, Validators} from '@angular/forms';
import { ErrorStateMatcher } from '@angular/material/core';
import { MatSnackBar } from '@angular/material/snack-bar';
import { ActivatedRoute, Router } from '@angular/router';
import { CustomValidator } from 'src/app/services/custom-validator';
import { LossService } from 'src/app/services/loss.service';


/** Error when invalid control is dirty, touched, or submitted. */
export class MyErrorStateMatcher implements ErrorStateMatcher {
  isErrorState(control: FormControl | null, form: FormGroupDirective | NgForm | null): boolean {
    const isSubmitted = form && form.submitted;
    return !!(control && control.invalid && (control.dirty || control.touched || isSubmitted));
  }
}


@Component({
  selector: 'app-edit-loss',
  templateUrl: './edit-loss.component.html',
  styleUrls: ['./edit-loss.component.scss']
})
export class EditLossComponent implements OnInit {


  eventTypeList: any[] = [{value:'CHUVA EXCESSIVA',text:'Chuva excessiva'}, 
                          {value:'GEADA',text:'geada'}, 
                          {value:'GRANIZO',text:'granizo'}, 
                          {value:'SECA',text:'seca'}, 
                          {value:'VENDAVAL',text:'vendaval'}, 
                          {value:'RAIO',text:'raio'}];

  constructor(private fb: FormBuilder,
    private route: ActivatedRoute,
    private router: Router,
    private lossService: LossService,
    private datePipe: DatePipe) { }

  loss_id: number = 0;
  matcher = new MyErrorStateMatcher();
  lossForm: FormGroup = this.fb.group({
    producer_name: new FormControl('', Validators.required),
    producer_email: new FormControl('', [Validators.required, Validators.email]),
    producer_cpf: new FormControl('', [Validators.required, CustomValidator.isValidCpf()]),
    crop_local: new FormControl('', [Validators.required,Validators.pattern('[-]?[0-9]+[.]?[0-9]+,[ ]*[-]?[0-9]+[.]?[0-9]+')]),
    harvest_date: new FormControl('', [Validators.required, CustomValidator.ptDate()]),
    crop_type:new FormControl('', [Validators.required]),
    event_type:new FormControl('', [Validators.required]),    
  });
  
  async ngOnInit() {
    this.route.params.subscribe(params => {
      this.loss_id = +params['id']
      console.log(this.loss_id)
    });

    await (await this.lossService.get_loss(this.loss_id)).subscribe((response) => {
      console.log(response)
      this.lossForm.setValue({producer_name: response.producer_name,
                              producer_email: response.producer_email,
                              producer_cpf: response.producer_cpf,
                              crop_local: response.crop_local,
                              harvest_date: this.datePipe.transform(response.harvest_date,'dd/MM/yyyy'),
                              crop_type: response.crop_type,
                              event_type: response.event_type})
    });
  }

  async submit(){
    const body = {
      producer_name: this.lossForm.controls['producer_name'].value,
      producer_email: this.lossForm.controls['producer_email'].value,
      producer_cpf: this.lossForm.controls['producer_cpf'].value,
      crop_local: this.lossForm.controls['crop_local'].value.replace(/^\s+|\s+$/g, ''),
      harvest_date: this.datePipe.transform(this.lossForm.controls['harvest_date'].value,'yyyy-MM-ddTHH:mm:ss'),   
      crop_type: this.lossForm.controls['crop_type'].value,
      event_type: this.lossForm.controls['event_type'].value,      
    }
    
    await (await this.lossService.edit_loss(this.loss_id,body)).subscribe()
    this.router.navigate(['/']);
  }
  back(){
    this.router.navigate(['/']);
  }
}
