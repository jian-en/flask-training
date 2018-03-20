from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index/<name>')
def index(name):
    return render_template('index.html',
                           name=name)
