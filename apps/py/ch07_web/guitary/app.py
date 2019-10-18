import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/guitars')
def guitars():
    guitar_list = []
    return flask.render_template('guitars.html', guitars=guitar_list)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
