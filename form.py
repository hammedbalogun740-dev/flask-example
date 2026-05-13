from flask_wtf import FlaskForm
from wtforms import ValidationError, TextAreaField
from wtforms.fields import StringField,  EmailField, PasswordField, DateField, SubmitField
from wtforms.validators import InputRequired, Length
from models import User


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired(),])
    password = PasswordField('password', validators=[InputRequired(), Length(min=6)])


class RegisterForm(FlaskForm):
    email = EmailField(
        'Email',
        validators=[InputRequired(),],
    
    )
    password = PasswordField(
        'Password',
        validators=[InputRequired(), Length(min=6)],
    )

    username = StringField(
        'username',
        validators=[InputRequired(),]
     )
#     dob = DateField(
#     'DateField',
#     validators=[InputRequired()],
#     )
    submit = SubmitField("Register")

    # def validate_email(self, field):
    #     if User.find_by_email(email=field.data):
    #         raise ValidationError("Email is register")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Email is registered")
    

    def validate_username(self, field):
        print(field.data)
        print(User.query.filter_by(username=field.data).all())
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Username is regstered")


class PostForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired()])  
    body = TextAreaField("Body")