from flask import Flask
from flask import request, render_template

app = Flask(__name__)

# intro

@app.route('/', methods=['POST'])
def index():
    print(request.form)
    # print(request.args)
    # print(request.values)
    # print(request.data)
    # print(request.get_json())
    return 'hello'


# form

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

app.config['SECRET_KEY'] = 'a random string'

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(),
                                           Email()])
    submit = SubmitField('提交')


@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return 'validate success'
    return render_template('submit.html', form=form)
