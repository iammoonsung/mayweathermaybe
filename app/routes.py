from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, RegistrationForm, ChildForm, PetForm, HobbyForm, BasicinfoForm
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
from app.models import User, Children, Pet, Hobby, Category, Product, Purchase, Liking, Exposure, Chosen
from app import db
from flask import request
from werkzeug.urls import url_parse
from datetime import datetime, date
import pandas as pd

@app.route('/')
@app.route('/index')
#@login_required
def index():
    #User.query.delete()
    #Children.query.delete()
    #Pet.query.delete()
    #Hobby.query.delete()
    #Category.query.delete()
    #Product.query.delete()
    #Purchase.query.delete()
    #Liking.query.delete()
    #db.session.commit()
    user = User.query.all()
    children = Children.query.all()
    pet = Pet.query.all()
    hobby = Hobby.query.all()
    category=Category.query.all()
    product=Product.query.all()
    purchase=Purchase.query.all()
    liking=Liking.query.all()
    return render_template('index.html', title='home page', User=user, Children=children, Pet=pet, Hobby=hobby, Category=category, Product=product,Purchase=purchase, Liking=liking)

@app.route('/profile')
def profile():
    if current_user.is_anonymous:
        form = LoginForm()
        return render_template('login.html', title='login', form=form)
    user = User.query.all()
    children = Children.query.all()
    pet = Pet.query.all()
    hobby = Hobby.query.all()
    category=Category.query.all()
    product=Product.query.all()
    purchase=Purchase.query.all()
    liking=Liking.query.all()
    return render_template('profile.html', title='Profile', User=user, Children=children, Pet=pet, Hobby=hobby, Category=category, Product=product,Purchase=purchase, Liking=liking)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(identity=form.identity.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid id or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(identity=form.identity.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('basicinfo'))
    return render_template('register.html', title='Register', form=form)

@app.route('/basicinfo', methods=['GET', 'POST'])
def basicinfo():
    if current_user.is_anonymous:
        form = LoginForm()
        return render_template('login.html', title='Add child', form=form)
    form = BasicinfoForm()
    if form.validate_on_submit():
        current_user.set_info(form.username.data,form.gender.data,form.birthday.data)
        children = Children(user_id = current_user.id, childage=form.childage.data, childgender=form.childgender.data)
        db.session.add(children)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('index'))
    return render_template('basicinfo.html', title='Basicinfo', form=form)

@app.route('/liking', methods=['GET', 'POST'])
def liking():
    if current_user.is_anonymous:
        form = LoginForm()
        return render_template('login.html', title='Add child', form=form)
    liking=db.session.query(Liking,Product).filter(Liking.user_id==current_user.id).filter(Product.id==Liking.product_id)
    df = pd.read_sql(liking.statement, liking.session.bind)
    df.to_csv('C:\\Users\\moonsung\\Desktop\\real\\liking.csv',header=False,index=False,encoding='euc-kr')
    liking=liking.all()
    return render_template('liking.html', title='Liking', Liking=liking)


@app.route('/child', methods=['GET', 'POST'])
def child():
    if current_user.is_anonymous:
        form = LoginForm()
        return render_template('login.html', title='Add child', form=form)
    form = ChildForm()
    if form.validate_on_submit():
        children = Children(user_id = current_user.id, childage=form.childage.data, childgender=form.childgender.data)
        db.session.add(children)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('child.html', title='Add Child', form=form)

@app.route('/pet', methods=['GET', 'POST'])
def pet():
    if current_user.is_anonymous:
        form = LoginForm()
        return render_template('login.html', title='sign in', form=form)
    form = PetForm()
    if form.validate_on_submit():
        pet = Pet(user_id = current_user.id, kind=form.kind.data)
        db.session.add(pet)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('pet.html', title='Add Pet', form=form)

@app.route('/hobby', methods=['GET', 'POST'])
def hobby():
    if current_user.is_anonymous:
        form = LoginForm()
        return render_template('login.html', title='sign in', form=form)
    form = HobbyForm()
    if form.validate_on_submit():
        hobby = Hobby(user_id = current_user.id, hobby=form.hobby.data)
        db.session.add(hobby)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('hobby.html', title='Add Hobby', form=form)