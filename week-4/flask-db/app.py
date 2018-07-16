from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pdb
# print(__name__, 'from app.py')

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///espn.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(100))

    # def all_teams_from_east_coast()


# db = SQLAlchemy()
# db.init_app(app)

@app.route('/nba/teams')
def index():
    teams = Team.query.all()
    return render_template('index.html', teams=teams)

@app.route('/nba/teams/<id>')
def show(id):
    team = Team.query.get(id)
    return render_template('show.html', team=team)


# if says need sql alchemy context RUN
# app.app_context().push()
# http://flask-sqlalchemy.pocoo.org/2.3/contexts/

# db.create_all()

# FLASK_APP = app.py
# from flask_migrate import Migrate
# flask db init
# flask db migrate -m 'create_users_table'
# flask db upgrade




# app.add_url_rule('/nba/teams', 'index', index)
# app.add_url_rule('/team/sixers', 'bob', show_bob)

# if __name__ == '__main__':
#     app.run(debug=True)

# Create
    insert into users ()
# Read
    index -> select * from users;
    show -> select * from users where users.id = 1
# Update
    SET 'foobar' name where id = 1
# Destroy
    delete from users where id = 1;
