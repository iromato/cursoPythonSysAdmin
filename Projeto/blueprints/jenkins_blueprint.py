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
