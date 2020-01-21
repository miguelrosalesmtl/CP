import { Component, OnInit } from '@angular/core';
import { HttpSecuredService } from '../core/http/http-secured.service'

@Component({
  selector: 'app-about',
  templateUrl: './about.component.html',
  styleUrls: ['./about.component.scss'],
  providers: [HttpSecuredService]
})
export class AboutComponent implements OnInit {
  orders :any = [

  ]
  constructor(private _http:HttpSecuredService) {}

  ngOnInit() {
    this._http.get('api/purchases/orders/').subscribe(
      (payload) => {
        this.orders =payload.body;
      })
  }
  getStatus(code:string){
    if(code === 'N')
      return 'New';
    else if(code === 'C')
      return 'Cancelled';
    else if(code === '')
      return 'Sent';
    else if(code === '')
      return 'Received';
    else
      return 'Undefined';
  }
}
