from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, EmailField, BooleanField
from wtforms.validators import DataRequired, Email, Length


class Form(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Зарегистрироваться')
    remember = BooleanField('Запомнить меня', default=False)