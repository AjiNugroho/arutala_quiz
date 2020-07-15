from flask import Blueprint, request, send_file, render_template
from app.rest_api.models import Database
from helpers.response_builder import resp
from helpers.validator import client_checker


rest_controller = Blueprint('rest_controller', __name__, url_prefix='/arutala', template_folder='../../templates')
#---------------------------------------------------------------
@rest_controller.route('/welcome', methods=['GET'])
def welcome(**kwargs):

    return 'welcome'
#---------------------------------------------------------------    

@rest_controller.route('/discount',methods=['GET'])
def halamandepan():
    return render_template('create_discount.html')

@rest_controller.route('/view_bill',methods=['GET'])
def bukalogin():
    return render_template('bill_view.html')

#---------------------------------------------------------------
@rest_controller.route('/save_dis',methods=['POST'])
@client_checker(no_auth=True)
def save_dis(**kwargs):
    request_params = kwargs.get('request_params')
    product = request_params.get('product')
    price = request_params.get('price')
    dis_code = request_params.get('dis_code')

    db = Database()


    response = db.save_dis(product,price,dis_code)

    return resp(**response)

#---------------------------------------------------------------
@rest_controller.route('/bill',methods=['GET'])
@client_checker(no_auth=True)
def bill(**kwargs):

    db = Database()
    response = db.get_bill()

    return resp(**response)


