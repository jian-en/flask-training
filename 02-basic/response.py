# import random

from flask import Flask
from flask import request
from flask import redirect
# , abort
# from flask import make_response
# from flask import jsonify

app = Flask(__name__)


@app.route('/')
def index():
    request.headers.get('User-Agent')
    """
    dice = random.randint(0, 10)
    if dice < 5:
        abort(404)
    """
    return redirect("http://www.baidu.com")


if __name__ == '__main__':
    app.run(debug=True)
