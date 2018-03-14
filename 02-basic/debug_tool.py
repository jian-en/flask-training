from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fujian'
app.config['DEBUG_TB_PROFILER_ENABLED'] = True
app.debug = True
toolbar = DebugToolbarExtension(app)


@app.route('/')
def index():
    return '<html><head></head><body><h1>Hello World</h1></body></html>'


if __name__ == '__main__':
    app.run()
