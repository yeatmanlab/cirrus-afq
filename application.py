import os
from flask import (Flask, request, redirect, url_for, send_from_directory,
                   render_template)
from werkzeug import secure_filename

UPLOAD_FOLDER = '/Users/arokem/projects/cirrus-afq/images'
ALLOWED_EXTENSIONS = set(['nii.gz', 'nii', 'bval', 'bvec', 'bvals', 'bvecs'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    for ext in ALLOWED_EXTENSIONS:
        if filename.endswith(ext):
            return True
    return False


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        for f in [request.files['dwi_file'],
                  request.files['bval_file'],
                  request.files['bvec_file']]:
            if f and allowed_file(f.filename):
                filename = secure_filename(f.filename)
                f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return render_template('layout.html')



@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


"""
import matplotlib.pyplot as plt
import numpy as np
import flask
app = flask.Flask(__name__)

app.vars = {}


@app.route('/index', methods=['GET', 'POST'])
def index():
    if flask.request.method == 'GET':
        return flask.render_template('layout.html')
    else:
        return flask.render_template('layout.html')

"""

if __name__ == "__main__":
    app.run(debug=True)
