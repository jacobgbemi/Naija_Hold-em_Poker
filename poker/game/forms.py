"""
The Game Flask Form
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField


class GameForm(FlaskForm):
    """
    Game Form
    """
    username = StringField('')
    hand_name = StringField('')
    status = StringField('')
    submit = SubmitField('Post Game')
 
# from flask_table import Table, Col


# class GameTable(Table):
#     username = Col('Username')
#     hand_name = Col('Handname')
#     status = Col('Winner')