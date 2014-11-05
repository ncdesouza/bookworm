from flask import render_template, flash, redirect, session, url_for, g

from app import app, db  # lm, oid
from app.workingOn.old.forms import EditForm
from mod_auth.models import User




# @app.errorhandler(404)
# def not_found_error(error):
#     return render_template('404.html'), 404
#
#
# @app.errorhandler(500)
# def internal_error(error):
#     db.session.rollback()
#     return render_template('500.html'), 500


# Test DB
@app.route('/testdb')
def testdb():
    if db.session.query("1").from_statement("SELECT 1").all():
        return 'It works.'
    else:
        return 'Something is broken.'








@app.route('/profile')
def profile():

    if 'email' not in session:
        return redirect(url_for('signin'))

    # << SQL >>
    # SELECT * FROM users WHERE email = session['email'];
    user = User.query.filter_by(email = session['email']).first()

    if user is None:
        return redirect(url_for('signin'))
    else:
        return render_template('profile.html')


@app.route('/user/<fname>.<lname>')
# @login_required
def user(fname, lname):
    user = User.query.filter_by(email= session['email']).first()
    if user is None:
        name = fname + ' ' + lname
        flash('User %s not found.' % name)
        return redirect(url_for('home'))
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html',
                           user=user,
                           posts=posts)

@app.route('/edit', methods=['GET', 'POST'])
# @login_required
def edit():
    form = EditForm(g.user.nickname)
    if form.validate_on_submit():
        g.user.nickname = form.nickname.data
        g.user.about_me = form.about_me.data
        db.session.add(g.user)
        db.session.commit()
        flash('Your profile has been updated.')
        return redirect(url_for('edit'))
    else:
        form.nickname.data = g.user.nickname
        form.about_me.data = g.user.about_me
    return render_template('edit.html', form=form)
