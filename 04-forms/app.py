from flask import Flask
from flask import request, render_template

app = Flask(__name__)

# intro

@app.route('/', methods=['GET', 'POST'])
def index():
    # print(request.form)
    # print(request.files)
    # print(request.args)
    # print(request.values)
    # print(request.data)
    print(request.get_json())
    return 'hello'


# form

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app.config['SECRET_KEY'] = 'fdsa9fdusa89das'

class MyForm(FlaskForm):
    name = StringField('ame', validators=[DataRequired()])
    submit = SubmitField('提交')


@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return 'validate success'
    return render_template('submit.html', form=form)
