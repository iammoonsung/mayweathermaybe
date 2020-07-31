from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, RegistrationForm, ChildForm, PetForm, HobbyForm, BasicinfoForm
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
from app.models import User, Children, Pet, Hobby, Category, Product, Purchase, Liking
from app import db
from flask import request
from werkzeug.urls import url_parse
from datetime import datetime, date
import pandas as pd
from pandas import dataframe as df


liking=db.session.query(Liking,Product).filter(Liking.user_id==current_user.id).filter(Product.id==Liking.product_id).all()
df = pd.DataFrame(liking)
print(df)