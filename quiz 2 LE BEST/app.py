import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

#https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3

app = Flask(__name__)
app._static_folder = "C:/Users/jugur/Documents/projet Git/quiz 2 LE BEST/templates/static"


@app.route('/')
def index():
    return render_template('accueil.html')


app.run(debug = False)
