from flask import render_template, request, Blueprint, session
from app import mod_public, db
from app.mod_public.forms import ContactForm, SearchForm
from app.models import Book

mod_public = Blueprint('public', __name__, url_prefix='/')

# Home - Home page
@mod_public.route('/')
@mod_public.route('home/', methods=['GET', 'POST'])
def home():
    form = SearchForm()
    if request.method == 'POST':
        return render_template('public/home.html', form=form)
    else:
        return render_template('public/home.html', form=form)


# About - Provides basic information about bookworm
@mod_public.route('about/')
def about():
    return render_template('public/about.html')


# Contact - Allows user to contact web admin
@mod_public.route('contact/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if not form.validate():
            return render_template('public/contact.html', form=form)
        else:
            # << Mail method not implemented >>
            return 'Form posted.'
    elif request.method == 'GET':
        return render_template('public/contact.html', form=form)


@mod_public.route('search/', methods=['Get', 'Post'])
def search():
    form = SearchForm()
    if request.method == 'POST':
        books = Book.query.filter(Book.title == form.title.data)
        return render_template('public/home.html', books=books, form=form)
    else:
        return render_template('public/home.html', form=form)

