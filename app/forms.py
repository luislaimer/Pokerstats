from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User 

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('pasword', validators=[DataRequired()])
    remember_me = BooleanField('remember me')
    submit = SubmitField('submit')

class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('pasword', validators=[DataRequired()])
    confirm_pwd = PasswordField('pasword', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('submit')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username already exists')

    def validate_email(self, email):
        address = User.query.filter_by(email=email.data).first()
        if address is not None:
            raise ValidationError('Email address already in use')
