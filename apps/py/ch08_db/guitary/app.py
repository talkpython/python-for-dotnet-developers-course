import os
import sys

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

import flask
from guitary.services import catalog_service
from guitary.data import session_factory
from guitary.data import data_loader

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/guitars')
@app.route('/guitars/<style>')
def guitars(style: str = None):
    guitar_list = catalog_service.all_guitars(style)
    return flask.render_template('guitars.html', guitars=guitar_list)


def main():
    session_factory.global_init('guitary.sqlite')
    session_factory.create_tables()
    data_loader.load_guitars_if_empty()

    app.run(debug=True)


if __name__ == '__main__':
    main()
