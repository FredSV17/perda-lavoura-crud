import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';
import { throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
@Injectable({
  providedIn: 'root'
})
export class LossService {

constructor(private http: HttpClient,
  private _snackBar: MatSnackBar) { }
base_url = "http://localhost:5000"
async list_loss(){
  return this.http.get<any[]>(`${ this.base_url }/loss`)
  // return response;
}
async list_loss_by_cpf(cpf: string){
  return this.http.get<any[]>(`${ this.base_url }/loss/cpf/${cpf}`)
  // return response;
}
async get_loss(id: number){
  return this.http.get<any>(`${ this.base_url }/loss/${id}`)
  // return response;
}
async create_loss(body: any){
  return this.http.post<any[]>(`${this.base_url}/loss/create`, body).pipe(
    catchError(error => {
      this._snackBar.open(error.error,'fechar',{ duration: 2000, panelClass: 'errorSnack' });
      return error
    })

  );
  // return response;
}

async edit_loss(id:number,body: any){
  return this.http.put<any[]>(`${this.base_url}/loss/edit/${id}`, body).pipe(
    catchError(error => {
      this._snackBar.open(error.error,'fechar',{ duration: 2000, panelClass: 'errorSnack' });
      return error
    })

  );
  // return response;
}

async delete_loss(id:number){
  return this.http.delete<any[]>(`${this.base_url}/loss/delete/${id}`).pipe(
    catchError(error => {
      this._snackBar.open(error.error,'fechar',{ duration: 2000, panelClass: 'errorSnack' });
      return error
    })

  );
  // return response;
}

}
