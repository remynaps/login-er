import datetime
from flask import Flask, render_template
from flask import Blueprint, request, jsonify, abort
from config import config

app = Flask(__name__)
app.config.update(**config)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login")
def login():
    app_id = app.config['APP_ID']
    app_secret = app.config['APP_SECRET']
    redirect_url = app.config['REDIRECT_URL']
    return render_template('home.html')

@app.route("/callback")
def loggedin():
    return render_template('loggedin.html')
