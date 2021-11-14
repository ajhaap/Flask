import server

from datetime import datetime

from flask import render_template

#@app.route("/")
def home_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html", day=day_name)

#@app.route("/movies")
def movies_page():
    return render_template("movies.html")