from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import dash
import pdb

server = Flask(__name__)
server.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///moes.db'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
server.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(server)
migrate = Migrate(server, db)

app = dash.Dash(__name__, server=server, url_base_pathname='/dashboard')

from package.dashboard import *

from package.models import *
import package.routes
