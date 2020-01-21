import { Component, OnInit } from '@angular/core';
import { finalize } from 'rxjs/operators';
import { HttpSecuredService } from '../core/http/http-secured.service'
import { ThrowStmt } from '@angular/compiler';

interface OrderDetail{
  id?: number,
  order?:number,
  food: number,
  quantity: number,
  unit_price: number,
  line_total: number,
}

interface Food{
  id: number,
  name: string,
  unit_price: number,
  food_type: number,
}

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
  providers: [HttpSecuredService]
})
export class HomeComponent implements OnInit {
  isLoading = false;
  selectedItem: Food;
  quantity: number;
  SelectedItemName: string = "Select...";
  id: number;
  total: number = 0;

  foodList: Array<Food> = [
  ]

  items: Array<OrderDetail> = [
  ]

  constructor(private _http: HttpSecuredService) {}

  ngOnInit() {
    this.isLoading = true;
    this.quantity = 0;
    this.SelectedItemName = 'Select...';
    this._http.get('api/food/').subscribe(
      (payload) =>{
        this.foodList = payload.body;
        this._http.get('api/purchases/orders/cart/').subscribe(
          (payload) => {
            this.items = payload.body.order_detail;
            this.id = payload.body.id;
            this.total = payload.body.total;
          });
      });
  }

  getFoodName(id:number): string {
    for (let food of this.foodList) {
      if(food.id === id)
        return food.name
    }
    return "Unavailable";
  }

  selectItem(food:Food) {
    this.selectedItem = food;
    this.SelectedItemName = food.name;
  }

  addItem(){
    if(this.selectedItem != undefined) {
      let index:number = this.getIndexForFoodIdd();
      if(index>-1){
        this.items[index].order = this.id;
        this.items[index].quantity = this.quantity;
        this.items[index].unit_price = this.selectedItem.unit_price;
        this.items[index].line_total = this.quantity*this.selectedItem.unit_price;
        if (this.items[index].id === undefined){
          this._http.post(`api/purchases/orders/${this.id}/details/`, '', this.items[index]).subscribe(
            (payload) =>{
              this.items[index] = payload.body;
              this.total += this.items[index].line_total;
            });
        }else{
          // An entry already exists for a given food
          this._http.put(`api/purchases/orders/${this.id}/details/${this.items[index].id}/` ,'', this.items[index]).subscribe(
            (payload) =>{
              this.items[index] = payload.body;
              this.total = 0;
             for (let item of this.items) {
              this.total += item.line_total;
            }
            });
        }
        
      }else{
        let new_entry = {
          order: this.id,
          food: this.selectedItem.id,
          quantity: this.quantity,
          unit_price: this.selectedItem.unit_price,
          line_total: this.quantity*this.selectedItem.unit_price};

        this._http.post(`api/purchases/orders/${this.id}/details/`, '', new_entry).subscribe(
          (payload) => {
            this.items.push(payload.body);
            this.total += payload.body.line_total;
          },
          err => console.log(err));
      }
    }    
  }

  placeOrder() {
    this._http.post(`api/purchases/orders/${this.id}/send_order/`,'', {}).subscribe(
      (payload) =>{
        this.ngOnInit();
      });
  }

  getIndexForFoodIdd(): number{
    let index:number = 0;
    for (let item of this.items) {
      if(item.food === this.selectedItem.id)
        return index;
      index++;
    }
    return -1;
  }

  deleteItem(item:any) {
    const index = this.items.indexOf(item);
    this._http.delete(`api/purchases/orders/${this.id}/details/${this.items[index].id}/`).subscribe(
      (resp) => {
        this.total -= this.items[index].line_total;
        this.items.splice(index,1);
      }
    );
  }
}
