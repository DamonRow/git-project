from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/home")
def hello_world():
    return render_template("index.html")

@app.route("/resume")
def resume():
    return render_template("resume_page.html")
