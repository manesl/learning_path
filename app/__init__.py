from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://gtqtanwsuaqmnf:0ee47b3b657378eb2ac9bd9535db053ebc4811efce6b6f7f16be9b0d418388cf@ec2-52-20-160-44.compute-1.amazonaws.com:5432/d3f7lmskmtql64?sslmode=require'
#'postgresql://postgres:postgres123@localhost/lp' #'postgresql://localhost/lp'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
mail = Mail(app)

from app import routes, models
