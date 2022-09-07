import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CreateLossComponent } from './loss/create-loss/create-loss.component';
import { ListLossComponent } from './loss/list-loss/list-loss.component';

const routes: Routes = [
  {path:"", component:ListLossComponent},
  {path:"create", component:CreateLossComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
