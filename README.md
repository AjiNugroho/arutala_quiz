# arutala_quiz

## How to run program

#### Install dependency:

run
```bash
pip3 install -r requirement.txt
```
#### Restore database:
- go to folder dumb_db 
- get discount.sql

run
```bash
mysql -u [username] -p < discount.sql
```
#### Run the FlaskApp

run
```bash
python3 main.py
```
#### Open Web Browser

goto [your base url]/arutala/discount  => to input/create discount

goto [your base url]/arutala/view_bill => to show bill

#### Api Test
API BILLING :
- open postman
- add GET request
- set url to [your base url]/arutala/bill
- klick Send

API Create Discount :
- open postman
- add POST request 
- set url to [your base url]/arutala/save_dis
- add product, price, dis_code in the Body request
- klick send
