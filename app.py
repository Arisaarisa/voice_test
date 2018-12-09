from flask import Flask, render_template, request, redirect, url_for

import db

app = Flask(__name__)


# @app.route("/")
# def index():
#     return render_template("index.html")

@app.route("/")
def voice():
    return render_template("voice.html")


@app.route("/add_answer", methods=["POST"])
def add_answer():
    this_year = request.form["this_year"]
    season = request.form["season"]
    after_today = request.form["after_today"]
    prefecture = request.form["prefecture"]
    region = request.form["region"]

    db.add_answer(this_year, season, after_today, prefecture, region)

    return redirect(url_for("voice"))


if __name__ == "__main__":
    app.run(debug=True)
