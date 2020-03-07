from flask import Blueprint, request, make_response, jsonify
from config import db
from bson.json_util import dumps

usuarios_route = Blueprint('usuario_route',__name__,url_prefix='/usuarios')

@usuarios_route.route('/',methods=['POST'])
def insert_user():
    try:
        user = dict(request.form)
        db.user.insert_one(

            {
                'name':user['name'],
                'email':user['email'],
                'message':[]
            }
        )
        return jsonify(user)
    except Exception as e:
        print(e)
        return make_response(
                                {'erro':'Data not found'},
                                404,
                                {'content-type':'application/json'}
                            )

@usuarios_route.route('/',methods=['GET'])
def get_users():
    try:
        user = db.user.find()
        return make_response(
            dumps(user),
            200,
            {'content-type':'application/json'}
            )
    except Exception as e:(
                                {'erro':'Data not found'},
                                404,
                                {'content-type':'application/json'}
                            )
        
     

