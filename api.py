from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

@app.route("/")
def intro():
    return render_template('index.html')
