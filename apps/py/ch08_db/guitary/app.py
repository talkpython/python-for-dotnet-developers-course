import flask
from guitary.services import catalog_service
from guitary.data import session_factory

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

    app.run(debug=True)


if __name__ == '__main__':
    main()
