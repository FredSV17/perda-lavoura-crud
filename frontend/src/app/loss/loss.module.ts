import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MaterialModule } from '../comps/material.module';
import { ListLossComponent } from './list-loss/list-loss.component';
import { CreateLossComponent } from './create-loss/create-loss.component';
import { EditLossComponent } from './edit-loss/edit-loss.component';
import { DeleteLossComponent } from './delete-loss/delete-loss.component';
import { DetailLossComponent } from './detail-loss/detail-loss.component';
import { ReactiveFormsModule } from '@angular/forms';

@NgModule({
  imports: [
    CommonModule,
    MaterialModule,
    ReactiveFormsModule
  ],
  declarations: [
    ListLossComponent,
    CreateLossComponent,
    EditLossComponent,
    DeleteLossComponent,
    DetailLossComponent
  ]
})
export class LossModule { }
