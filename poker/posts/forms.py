from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    """
    Form for accepting players comments
    """
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Let\'s know if you had fun', validators=[DataRequired()])
    submit = SubmitField('Post Comment')