from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
# from wtforms.validators import DataRequired


class GameForm(FlaskForm):
    username = StringField('')
    hand_name = StringField('')
    status = StringField('')
 
# from flask_table import Table, Col


# class GameTable(Table):
#     username = Col('Username')
#     hand_name = Col('Handname')
#     status = Col('Winner')