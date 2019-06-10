import datetime
from flask import Flask, render_template, redirect
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
    return redirect(app.config['AUTH_URL'] + '?client_id=' + app_id + '&client_secret=' + app_secret + '&redirect_url=' + redirect_url + '&state=ransomshits', code=302)

@app.route("/callback")
def loggedin():
    token = request.args.get('token')
    if token:
        return render_template('loggedin.html')
    else:
        return redirect('/')

@app.route("/logout")
def logout():
    return redirect(app.config['AUTH_URL'] + '/logout')