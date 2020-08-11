from app import db
from datetime import datetime, date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, index=True)
    identity = db.Column(db.String, index=True, unique=True)
    gender = db.Column(db.Integer)
    birthday = db.Column(db.DateTime)
    age = db.Column(db.Integer)
    email = db.Column(db.String, index=True, unique=True)
    password_hash = db.Column(db.String)
    isworking = db.Column(db.Boolean, default=0)
    havingcar = db.Column(db.Boolean, default=0)
    residence = db.Column(db.String)
    income = db.Column(db.Integer, default=5)
    household = db.Column(db.Float, default=5.0)
    freetime = db.Column(db.Float, default=5.0)


    def __repr__(self):
        return '<User {}>'.format(self.id)   
        
    def set_info(self,username,gender,birthday):
        today_date=date.today()
        self.username=username
        self.gender=gender
        self.birthday=birthday
        self.age = today_date.year - birthday.year + 1

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Children(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    childgender = db.Column(db.Integer)
    childage = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Children {}>'.format(self.gender, self.age)

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kind = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Pet {}>'.format(self.kind)

class Hobby(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hobby = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Hobby {}>'.format(self.hobby)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cat1 = db.Column(db.String)
    cat2 = db.Column(db.String)
    cat3 = db.Column(db.String)
    cat4 = db.Column(db.String)
    cat5 = db.Column(db.String)
    cat6 = db.Column(db.String)
    
    def __repr__(self):
        return '<Category {}>'.format(self.cat1,self.cat2,self.cat3,self.cat4,self.cat5, self.cat6)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)
    image = db.Column(db.String)
    product_cat = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __repr__(self):
        return 'Product {}>'.format(self.product_cat,self.name)

class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    product_id = db.Column(db.String, db.ForeignKey('product.id'))
    purchasetime = db.Column(db.DateTime, db.ForeignKey('weather.time'))
    lat_purchase = db.Column(db.String, db.ForeignKey('weather.latitude'))
    long_purchase = db.Column(db.String, db.ForeignKey('weather.longitude'))

    def __repr__(self):
        return 'Purchase {}>'.format(self.user_id,self.product_id,self.purchasetime)

class Liking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    liketime = db.Column(db.DateTime, db.ForeignKey('weather.time'))
    lat_liking = db.Column(db.String, db.ForeignKey('weather.latitude'))
    long_liking = db.Column(db.String, db.ForeignKey('weather.longitude'))

    def __repr__(self):
        return 'Liking {}>'.format(self.user_id,self.product_id,self.liketime)

class Exposure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))

    def __repr__(self):
        return 'Exposure {}>'.format(self.user_id,self.product_id)

class Chosen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    chosentime = db.Column(db.DateTime, db.ForeignKey('weather.time'))
    lat_chosen = db.Column(db.String, db.ForeignKey('weather.latitude'))
    long_chosen = db.Column(db.String, db.ForeignKey('weather.longitude'))

    def __repr__(self):
        return 'Chosen {}>'.format(self.user_id,self.product_id)

class Pack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sentence = db.Column(db.String)

    def __repr__(self):
        return 'Pack {}>'.format(self.sentence)

class ClickedPack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    pack_id = db.Column(db.Integer, db.ForeignKey('pack.id'))
    pack_cat = db.Column(db.String)
    clicktime = db.Column(db.DateTime, db.ForeignKey('weather.time'))
    lat_clickpack = db.Column(db.String, db.ForeignKey('weather.latitude'))
    long_clickpack = db.Column(db.String, db.ForeignKey('weather.longitude'))

    def __repr__(self):
        return 'ClickedPack {}>'.format(self.user_id,self.pack_id,self.pack_cat)

class Weather(db.Model):
    time = db.Column(db.DateTime, primary_key=True)
    latitude = db.Column(db.String, primary_key=True)
    longitude = db.Column(db.String, primary_key=True)
    temperature = db.Column(db.Float)
    precp_amount = db.Column(db.Float)
    wind_spd = db.Column(db.Float)
    humidity = db.Column(db.Float)
    pressure = db.Column(db.Float)
    rad_amount = db.Column(db.Float)
    visibility = db.Column(db.Float)
    cloud_amount = db.Column(db.Float)
    pm10 = db.Column(db.Float)
    pm25 = db.Column(db.Float)
