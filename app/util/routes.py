from flask import render_template, flash, redirect, url_for, request
from flask_login.utils import login_required
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user

from app import db
from app.base.models import User
from app.util import blueprint
from app.util.forms import LoginForm, ForgotPasswordForm, ResetPasswordForm
from app.util.email import send_password_reset_email

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('base.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('util.login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('base.index')
        return redirect(next_page)
    return render_template('login.jinja', title='Sign In', form=form)

@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('util.login'))

@blueprint.route('/forgotpassword', methods=['GET', 'POST'])
def forgotpassword():
    if current_user.is_authenticated:
        return redirect(url_for('base.index'))
    form = ForgotPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instrucitons to reset your password.')
        return redirect(url_for('util.login'))
    return render_template('forgot_password.jinja', form=form)

@blueprint.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('base.index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('base.index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('util.login'))
    return render_template('reset_password.jinja', form=form)

@blueprint.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ResetPasswordForm()
    if form.validate_on_submit():
        current_user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been changed.')
        return redirect(url_for('base.index'))
    return render_template('reset_password.jinja', form=form)
    