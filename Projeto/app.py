#!/usr/bin/env python3

#controle dos modulos
import flask
import config
import logging
#Controle das rotas
from blueprints.docker_blueprint import docker_routes
from blueprints.jenkins_blueprint import jenkins_routes
from blueprints.ldap_blueprint import ldap_routes
#controle da aplicacao principal
app = flask.Flask(__name__)
app.secret_key = 'chave'

#controle das blueprints
app.register_blueprint(docker_routes)
app.register_blueprint(jenkins_routes)
app.register_blueprint(ldap_routes)

@app.route('/')
def index():
    if 'logged' in flask.session and flask.session['logged'] == True:
        pass
    else:
        flask.session['logged'] = False

    if not flask.session['logged']:
        return flask.redirect(flask.url_for('ldap.index'))
    logging.info ('Rota acessada com sucesso')   
    logging.warning ('log de warning') 
    config.corona_virus.covid('Cheguei')
    return flask.render_template('index.html',titulo='Inicio')
#por enquanto deixar o app.run()
app.run(debug=True)

