from collections import namedtuple

from flask import Flask, render_template, redirect, url_for, request


import real_path


app = Flask(__name__)


paths = []


@app.route('/', methods=['GET'])
def hello_user():
    """Welcomed by the user on the start page"""
    return render_template('index.html')


@app.route('/main', methods=['GET'])
def main():
    return render_template('main.html', paths=paths)


@app.route('/get_real_path', methods=['POST'])
def get_real_path():
    """Prints the real path"""
    text = request.form['text']

    rp = real_path.RealPath(text)
    text = rp.real_path()

    paths.append(text)

    return redirect(url_for('main'))
