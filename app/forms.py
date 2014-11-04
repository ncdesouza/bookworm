from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, TextAreaField, validators, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length
from app.models import User


class ContactForm(Form):
    name = StringField("Name", [validators.DataRequired("Please enter your name")])
    email = StringField("Email", [validators.DataRequired("Please enter you email"),
                                  validators.Email("Please enter a  valid email")])
    subject = StringField("Subject", [validators.DataRequired("Please enter a subject")])
    message = TextAreaField("Message", [validators.DataRequired("Please enter your message")])
    submit = SubmitField("Send")



class SignupForm(Form):
    fname = StringField("First name", [validators.DataRequired("Please enter your  first name.")])
    lname = StringField("Last name", [validators.DataRequired("Please enter your  last name.")])
    password = PasswordField('Password', [validators.DataRequired("Please enter a password.")])
    email = StringField("Email", [validators.DataRequired("Please enter your email address"),
                                  validators.Email("Please enter a valid email address.")])
    submit = SubmitField("Create account")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    # def validate(self):
    #     if not Form.validate(self):
    #         return False
    #     # << SQL >>
    #     # SELECT * FROM users
    #     # WHERE email = self.email.data.lower()
    #     # LIMIT 1
    #     user = User.query.filter_by(email=self.email.data.lower()).first()
    #     if user:
    #         self.email.errors.append("That email address is already taken")
    #         return False
    #     else:
    #         return True


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class EditForm(Form):
    nickname = StringField('nickname', validators=[DataRequired()])
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])

    def __init__(self, original_nickname, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.original_nickname = original_nickname

    def validate(self):
        if not Form.validate(self):
            return False
        if self.nickname.data == self.original_nickname:
            return True
        user = User.query.filter_by(nickname=self.nickname.data).first()
        if user != None:
            self.nickname.errors.append('This nickname is already in use. Please choose another one.')
            return False
        return True