import datetime
from flask import Flask, render_template
from flask import Blueprint, request, jsonify, abort

app = Flask(__name__)

@app.route("/")
def home():
    # session['next'] = request.args.get('next', None)
    return render_template('home.html')

