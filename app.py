from flask import Flask
from flask import Response
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    #return render_template("index.html")
    return "This is the awesome app EVER, speaking with brad and sahdev."
 

@app.route("/healthz")
def healthz():
    resp = Response("ok")
    resp.headers['Custom-Header'] = 'Awesome'
    # this is awesome tying things
    return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')
