from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import dash

server = Flask(__name__)
server.config.from_object('restaurants.config.Config')

db = SQLAlchemy(server)
migrate = Migrate(server, db)
from restaurants.models import *

app = dash.Dash(__name__, server=server, url_base_pathname='/')

from restaurants.dashboard_views.dashboard import app
import restaurants.routes
