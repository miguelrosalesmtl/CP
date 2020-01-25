# Cyberpublicity Shopping Cart
by Miguel Rosales

# Requirements
  - Docker version 19.03.5 or greater
  - Docker-compose version 1.21 or greater
  - NodeJS v.13.6.0  or greater
  - npm 6.13.4 or greater

# Description
**frontend:**

Angular 8+
https://github.com/ngx-rocket/starter-kit

**backend:**
Python 3.7, Django 2.2.9

# Installation
### Backend

**build image**

sudo docker-compose build

**deploy image**

sudo docker-compose up -d

**migrate**

sudo docker-compose exec app python3 manage.py migrate

**Load fixtures**

sudo docker-compose exec app python3 manage.py loaddata shopping_cart/fixtures/auth.json

sudo docker-compose exec app python3 manage.py loaddata shopping_cart/fixtures/shopping_cart.json

**Monitor the container**

sudo docker logs --tail 50 --follow --timestamps backend_app_1

### Frontend

npm install &

npm start

http://locahost:4200


# Test Account

**username:** test

**password:** cyberpublicity

# ReDoc

http://localhost:8000/api/redoc/

# Key points
#### General Solution
The orders are composed of two models Order and OrderDetail (header and detail). While the status is CART, it is considered a CART object and when the order is submitted it is considered as an order.

#### Django admin
There are three models registered Food, FoodCategory and Order. OrderDetail appears as an inline in Order.


**2.1 Add a bunch of items in the Food tables and create an initial_data.**

DONE (shopping_cart/fixtures/)

**2.2 In Django admin, where we list each entries of a table, make columns sortable when we click on them.**

DONE

**2.3 You must be able to add/edit/delete the Django User table from the admin**

DONE

**3.1 We want an API endpoints in order to get a list orders or delete an order.**

list: [GET] http://localhost:8000/api/purchases/orders/

delete: [DELETE] http://localhost:8000/api/purchases/orders/{pk}

**3.2 Make sure that when getting the details of an order, you add an extra field called Total,
which provide the overall total of the order.**

DONE

**3.3 We want an API endpoints in order to update the status of an order**

[PUT] http://localhost:8000/api/purchases/orders/{pk}

**3.4 When requesting a list of Orders, we can filter the list by user and status.**

example1: http://localhost:8000/api/purchases/orders/?user=1

example2: http://localhost:8000/api/purchases/orders/?user=1&status=N

**3.5 When requesting a list of Orders, we can order the list by any field.**

example: http://localhost:8000/api/purchases/orders/?ordering=total

