import flask
import docker

docker_routes = flask.Blueprint(name='docker',import_name=__name__,url_prefix='/docker')

@docker_routes.route('/')
def index():
    client = docker.from_env() # Docker na instancia local
    # client = docker.DockerClient() # Docker na instancia Remota
    container = client.containers.get('ubuntu') # pego uma instancia de um container
    dir(container)
    container_ubuntu = {
        'id':container.short_id,
        'imagem':container.image.tags[0],
        'nome':container.name,
        'status':container.status
    }

    return flask.render_template('docker.html',titulo=f'Gereciamento do servico {container.name}',container=container_ubuntu)


@docker_routes.route('/start')
def start():
    client = docker.from_env()
    container = client.containers.get('ubuntu')
    container.start()
    return flask.redirect(flask.url_for('docker.index')) 


@docker_routes.route('/stop')
def stop():
    client = docker.from_env()
    container = client.containers.get('ubuntu')
    container.stop()
    return flask.redirect(flask.url_for('docker.index'))

@docker_routes.route('/restart')
def restart():
    client = docker.from_env()
    container = client.containers.get('ubuntu')
    container.restart()
    return flask.redirect(flask.url_for('docker.index'))