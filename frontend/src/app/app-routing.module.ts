import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CreateLossComponent } from './loss/create-loss/create-loss.component';
import { DeleteLossComponent } from './loss/delete-loss/delete-loss.component';
import { DetailLossComponent } from './loss/detail-loss/detail-loss.component';
import { EditLossComponent } from './loss/edit-loss/edit-loss.component';
import { ListLossComponent } from './loss/list-loss/list-loss.component';

const routes: Routes = [
  {path:"", component:ListLossComponent},
  {path:"create", component:CreateLossComponent},
  {path:"edit/:id", component:EditLossComponent},
  {path:"detail/:id", component:DetailLossComponent},
  {path:"delete/:id", component:DeleteLossComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
