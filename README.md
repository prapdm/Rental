# Rental

#### Features

A simple program for renting and returning items write in Python with tkinter. Written for educational purposes.

- create/edit new users
- add new items
- print user/items cards with ean code
- rent and return items with quantity and days limit
- search items with simple filter (rented and expired)

#### Prepering environment

* Python 3.7
* MySQL or MariaDB

You need to install MySQL or MariaDB server, create empty database and import schema.sql file. At the first run the "Rental" will ask for database server, port, user and password. Please provide this data. "Rental" will save it in _database.cfg_

![Alt text](screens/database-setup.jpg?raw=true "Database setup")

#### To install requirements:

```
pip install -r requirements.txt
```
#### To create datanase:

    mysql -u root -p
    mysql> CREATE DATABASE rental;

### Create user and password for database

    CREATE USER 'rental'@'%' IDENTIFIED BY 'password';
    GRANT ALL ON rental.* TO 'rental'@'%';
    exit;
### Create tablse
    mysql -u rental -p < schema.sql

### Screenshots

![Alt text](screens/main-window.jpg?raw=true "Main window")

### Add new user

![Alt text](screens/user.jpg?raw=true "User")
![Alt text](screens/user-card.jpg?raw=true "User card")
![Alt text](screens/user-card-ean.jpg?raw=true "EAN")

### Add new items

![Alt text](screens/new-item.jpg?raw=true "Item")
![Alt text](screens/item-ean.jpg?raw=true "EAN")

### Rent and return 

![Alt text](screens/rent.jpg?raw=true "Item")
![Alt text](screens/history.jpg?raw=true "Item")