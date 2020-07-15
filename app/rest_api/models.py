from flask import g, Response, request
import re
import hashlib
import json
from datetime import datetime
class Database(object):

    def __init__(self,**kwargs):

        self.cursor = g.cursor
        self.lang = 'en-us'

        #balesan respon
        self.payload = dict(
            error_code=0,
            results={},
            meta={},
            resp_message=''
        )

    def get_bill(self):
        '''method untuk cek user dari no_hp dan email'''

        query = '''
        select * from discount
        '''
        result = self.cursor(query).fetchall()
        bills = []
        price_total = 0
        dis_total = 0
        count = 0
        for row in result :
            tipe = ''
            refund = ''
            discount = 0
            if row['dis_code'] == 1:
                tipe = 'Fashion'
                refund = 'Yes'
                discount = 0.1 * row['Price']
            if row['dis_code'] == 2:
                tipe = 'Furniture'
                refund = 'No'
                discount = 10 + (0.02 * row['Price'])
            if row['dis_code'] == 3:
                tipe = 'Jewelry'
                refund = 'No'
                if row['Price'] >= 100:
                    discount = 0.01 * (row['Price']-100) 

            amount = row['Price'] - discount

            price_total += row['Price']

            dis_total += discount

            count += 1

            bill = {
                'Name':row['name'],
                'DisCode':row['dis_code'],
                'Type':tipe,
                'Refundable':refund,
                'Price': row['Price'],
                'Discount': discount,
                'Amount':amount,
            }
            bills.append(bill)

        if count == 0 :
            self.payload['error_code']=204
            return self.payload
        
        meta = {
            'price_subtotal': price_total,
            'discount_subtotal': dis_total,
            'grand_total': price_total-dis_total
        }
        self.payload['results'] = bills
        self.payload['meta'] = meta

        return self.payload

    def save_dis(self,prod,price,dis_code):
        '''method untuk menyimpan register data'''

        query = '''
        INSERT INTO discount (name, dis_code, price) 
        VALUES (%s, %s, %s);
        '''

        result = self.cursor(query,[prod,dis_code,price])

        if not result.rowcount:
            self.payload['error_code']=500
            return self.payload
        
        self.payload['results'] = 'saved successfully'
        return self.payload
        