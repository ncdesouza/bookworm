from datetime import datetime
from flask import session, g
from flask_wtf import Form
from wtforms import IntegerField, validators, StringField, SubmitField, DateField
from wtforms_components import DateRange
from app import db
from app.models import User


class UploadBookForm(Form):
    isbn = IntegerField("ISBN", [validators.DataRequired("Please enter the ISBN number.")])
    title = StringField("Title", [validators.DataRequired("Please enter the book's title.")])
    volume = IntegerField("Vol.")
    author = StringField("Author", [validators.DataRequired("Please enter the book's author")])
    publisher = StringField("Publisher")
    year = IntegerField("Year")
    subject = StringField("Subject")
    endDate = DateField("End Date", validators=[DateRange(min=datetime.now())])
    submit = SubmitField("Upload Book")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

