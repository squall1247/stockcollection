# Stockcollection

The stock management system is a web server for creating and managing stock in database.

## Features

* Sign-in by both local and social accounts (only github now).
* Database administrator can manage the DB on admin page.
* User can add or update a stock information after login successfully.
* It supports Restful API by Django REST framework.
* Restful API basic Authentication.

----
## Development environment
* Python 3.6.6
* Django 2.2.5
* Database is SQLite

----
## Usage

    $ python manage.py runserver "ip_address:port"
The following urls can be accessed.

1.Home page`ip_address:port/`

2.Admin page `ip_address:port/admin/`

3.Restful API testing page` ip_address:port/stock/`

----
## Todos
* Enhance rest authentication.
* Extend stock table in DB that can store more information (e.g., history price, EPS, free cash flow, etc.).
* Add delete function.
