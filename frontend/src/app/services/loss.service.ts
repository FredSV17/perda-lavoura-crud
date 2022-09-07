import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
@Injectable({
  providedIn: 'root'
})
export class LossService {

constructor(private http: HttpClient) { }
base_url = "http://localhost:5000"
async list_loss(){
  var response
  await this.http.get(`${ this.base_url }/loss`)
           .subscribe((result: any) => response = result);
  return response
  // return response;
}

}
