#!/usr/bin/env python3
import flask
app = flask.Flask(__name__)

@app.route('/')
def index():
    nomes = ['Daniel','Maria','Juliana','Paulo','Pedro','Astolfos']
    return flask.render_template('footer.html', pessoas=nomes)

app.run(debug=True)