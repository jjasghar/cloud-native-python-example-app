from flask import Flask
from flask import Response

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello , i can't seem to get 5000 to work."


@app.route("/healthz")
def healthz():
    resp = Response("ok")
    resp.headers['Custom-Header'] = 'Awesome'
    return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')
