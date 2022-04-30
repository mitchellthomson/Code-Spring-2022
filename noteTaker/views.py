from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/notes')
def notes():
    return render_template("notes.html")

@views.route('/weather')
def weather():
    return render_template("weather.html")