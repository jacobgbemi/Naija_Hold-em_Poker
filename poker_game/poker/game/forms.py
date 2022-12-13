from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired


class GameForm(FlaskForm):
    play = SubmitField('Play')
    play_again = SubmitField('Play Again')
    quit = SubmitField('Quit')