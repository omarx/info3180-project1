from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
import os

from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, '..', 'uploads')


from .models import Properties
from app import views
