from flask import Flask, request, render_template
import pdb
print(__name__)

app = Flask(__name__)

@app.route('/nba/teams')
def index():
    return render_template('index.html')

@app.route('/nba/teams/<id>')
def show(id):
    team = db.session.query(Team).get(id)
    return render_template('show.html', team=team)

app.run(debug=True)
