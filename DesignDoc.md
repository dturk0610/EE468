# Design Document

## Database Architecture

![database_diagram](images/../database_diagram.png)

## Software
This application is uses the following python modules:

* `Django 4.0.3`
* `mysql-connector-python 8.0.28`

and mySQL version 8.0.28.


## Accounts
Accounts are handled through the built-in django account manager accessible at `http://[hostname]/admin`. Permissions are handled via groups named `admin`, `student`, and `prof`. These groups do not have any django permissions, as accounts are limited by the name of the their joined groups. These limitations are implemented using template if conditions and manual checking in API calls.

Any user attempting to access a resource that they do not have access to will be redirected to a login page. 

## URL Paths
All functionality is organized via URL paths:

* `myapp/`
  * `controlPanel` - Main page to navigate functionality
  * `accounts/`
    * `login`
    * `logout`
  * `api/`
    * `F1` through `F6` - API functions


