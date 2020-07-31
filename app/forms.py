from flask_wtf import FlaskForm
from datetime import datetime, date
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField, DateField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User, Children, Pet, Hobby

class LoginForm(FlaskForm):
    identity = StringField('아이디', validators=[DataRequired()])
    password = PasswordField('비밀번호', validators=[DataRequired()])
    remember_me = BooleanField('아이디 저장')
    submit = SubmitField('로그인')

class RegistrationForm(FlaskForm):
    identity = StringField('아이디', validators=[DataRequired()])
    email = StringField('이메일', validators=[DataRequired(), Email()])
    password = PasswordField('비밀번호', validators=[DataRequired()])
    password2 = PasswordField(
        '비밀번호 확인', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('회원가입')

    def validate_identity(self, identity):
        user = User.query.filter_by(identity=identity.data).first()
        if user is not None:
            raise ValidationError('다른 이름을 사용해주세요.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('이미 가입된 이메일 입니다.')

class BasicinfoForm(FlaskForm):
    username = StringField('이름', validators=[DataRequired()])
    gender = RadioField('성별', choices=[(1,'남'),(2,'여')],coerce=int)
    birthday = DateField('생일', format='%Y%m%d', validators=[DataRequired()])
    childage = IntegerField('자녀 나이', validators=[DataRequired()])
    childgender = RadioField('자녀 성별', choices=[(1,'남'),(2,'여')],coerce=int)
    submit = SubmitField('제출')

class ChildForm(FlaskForm):
    childage = IntegerField('자녀 나이', validators=[DataRequired()])
    childgender = RadioField('자녀 성별', choices=[(1,'남'),(2,'여')],coerce=int)
    submit = SubmitField('자녀 추가')

class PetForm(FlaskForm):
    kind = StringField('종류', validators=[DataRequired()])
    submit = SubmitField('반려동물 추가')

class HobbyForm(FlaskForm):
    hobby = StringField('취미', validators=[DataRequired()])
    submit = SubmitField('취미 추가')
