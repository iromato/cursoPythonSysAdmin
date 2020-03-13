import jenkins
import flask

jenkins_routes = flask.Blueprint(name='jenkins',import_name=__name__,url_prefix='/jenkins')

@jenkins_routes.route('/')
def index():
    client = jenkins.Jenkins('http://localhost:8080', username='admin',password='admin')
    jobs_list = client.get_jobs()
    jobs = []

    for job in jobs_list:
        jobs.append(client.get_job_info(job['fullname']))
    return flask.render_template('jenkins.html',titulo='Jobs Jenkins',jobs=jobs)

@jenkins_routes.route('/build/<string:job_name>')
def jenkins_build(job_name):
    client = jenkins.Jenkins('http://localhost:8080',username='admin',password='admin')
    client.build_job(job_name)
    return flask.redirect(flask.url_for('jenkins.index'))

@jenkins_routes.route('/update/<string:job_name>')
def jenkins_update(job_name):
    client = jenkins.Jenkins('http://localhost:8080',username='admin',password='admin')
    job = {
        'xml' : client.get_job_config(job_name)
    }
    print(client.get_job_config(job_name))
    return flask.render_template('jenkins_update.html',job=job,titulo=job_name,job_name=job_name)

@jenkins_routes.route('/rebuild',methods=['POST'])
def jenkins_rebuild():
    try:
        data = flask.request.form
        client = jenkins.Jenkins('http://localhost:8080',username='admin',password='admin')
        client.reconfig_job(data['name'],data['xml'])
        return flask.redirect(flask.url_for('jenkins.index'))
    except Exception:
        return flask.redirect(flask.url_for('jenkins.jenkins_update',job_name=data['name']))