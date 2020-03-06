#!/usr/bin/env python3

import flask
import json
app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'Ola Mundo'

@app.route('/pagina/<id>')
def pagina2(id):
    return 'Ola Mundo, estou na pagina {2}'

@app.route('/api')
def api():
    # dados = {
    #     'name': 'renato',
    #     'id':'555'
    #     }
    # return flask.jsonify(dados)
    header = {'content-type': 'application/json'}
    retorno = {'message':'Resposta'}
    return flask.make_response(json.dumps(retorno),404,header)
app.run(port='8080')