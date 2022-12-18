from flask_wtf import FlaskForm
from flask_table import Table, Col
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired


class Game(FlaskForm):
    play = SubmitField('Play')
    play_again = SubmitField('Play Again')
    quit = SubmitField('Quit')