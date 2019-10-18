import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html', name="Michael", nums=[1, 1, 2, 3, 5, 8])


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
