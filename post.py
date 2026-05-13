from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField

class PostForm(FlaskForm):
    title = StringField("Post Title")
    body = TextAreaField("Post Body")
    submit = SubmitField("Add Post")