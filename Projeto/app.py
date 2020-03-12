#!/usr/bin/env python3

#controle dos modulos
import flask

#Controle das rotas
from blueprints.docker_blueprint import docker_routes
from blueprints.jenkins_blueprint import jenkins_routes

#controle da aplicacao principal
app = flask.Flask(__name__)

#controle das blueprints
app.register_blueprint(docker_routes)
app.register_blueprint(jenkins_routes)

@app.route('/')
def index():
    return flask.render_template('index.html',titulo='Inicio')
#por enquanto deixar o app.run()
app.run(debug=True)

