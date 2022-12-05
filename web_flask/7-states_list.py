#!/usr/bin/python3
""" Module 7-states_list.py """
from flask import Flask


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """ remove the current SQLAlchemy Session """
    from models import storage
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Renders all states """
    from models import storage
    from models.state import State
    from flask import render_template

    state_list = []
    for i in storage.all(State).values():
        state_list.append(str(i.name))

    print(state_list)

    return render_template('7-states_list.html',
                           state_list=storage.all(State).values())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)