from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    print(dir(request))
    user_agent = request.headers.get('User-Agent')
    return '<h2>Your browser is %s</p>' % user_agent

@app.route('/foo')
def foo():
    return 'hello'


if __name__ == '__main__':
    app.run(debug=True)
