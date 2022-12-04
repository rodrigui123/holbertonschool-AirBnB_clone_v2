#!/usr/bin/python3
"""Python Module"""
from models import storage
from flask import Flask, render_template


app = Flask(__name__)
# create Flask obj referencing self
app.url_map.strict_slashes = False


@app.teardown_appcontext
def tear_down(exit):
    #  removes current SQLAlchemy Session
    storage.close()


@app.route('/states_list')
def list_states():
    #  renders + shows states
    return render_template('7-states_list.html', states=storage.all('State'))


# check that's the route + run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)