from flask import Flask, request, render_template
import pdb
print(__name__)

app = Flask(__name__)

@app.route('/nba/teams')
def index():
    # response = app.make_response(('<h1> whatever <h1>', 200))
    # , 203, {'content-type': 'text/html'}
    return render_template('index.html')

@app.route('/nba/teams/<id>')
def show(team):
    # return team
    return render_template('show.html', team_name=team)


# def show_sixers():
#     'here we are'
#     pdb.set_trace()
#     pass

# app.add_url_rule('/nba/teams', 'index', index)
# app.add_url_rule('/team/sixers', 'bob', show_bob)


app.run(debug=True)
