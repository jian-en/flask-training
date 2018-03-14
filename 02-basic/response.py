import random

from flask import Flask
from flask import request
from flask import redirect, abort
from flask import make_response
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def index():
    dice = random.randint(0, 10)
    if dice < 5:
        abort(404)

    # return redirect("http://www.baidu.com")
    return make_response('hello', 403, {'X-Sex': 'Male'})
    # return jsonify({'name':'fujian', 'age':29})


if __name__ == '__main__':
    app.run(debug=True)
