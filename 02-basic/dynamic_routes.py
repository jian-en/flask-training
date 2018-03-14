from flask import Flask

app = Flask(__name__)


@app.route('/index')
def index():
    return '<h1>Hello World</h1>'


@app.route('/user/<username>/<int:age>')
def user(username, age):
    # username = username # + 1
    age += 10
    return '<h1>Hello World, %s, %s</h1>' % (username, age)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
