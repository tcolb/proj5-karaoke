import flask
import config

app = flask.Flask(__name__)

CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY

FILE_NAME = CONFIG.FILE_NAME
MAPBOX_TOKEN = CONFIG.MAPBOX_TOKEN
MAPQUEST_KEY = CONFIG.MAPQUEST_KEY
PORTNUM = CONFIG.PORTNUM

@app.route("/")
def index():
    return flask.render_template('karaoke.html')

@app.route("/_request", methods=["GET"])
def points():

    points = []
    with open(FILE_NAME) as f:
        for line in f:
            print(line)
            points.append(line.split(','))

    return flask.jsonify(results=points, box_token=MAPBOX_TOKEN, quest_key=MAPQUEST_KEY)

if __name__ == "__main__":
    app.debug = True
    app.run(port=PORTNUM, host="0.0.0.0")
