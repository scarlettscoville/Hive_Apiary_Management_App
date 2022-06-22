from flask import render_template, request, flash
import requests
from .import bp as main
from flask_login import login_required, current_user
from app.models import User, Hive, Inspection
import random

@main.route('/', methods = ['GET'])
def index():
    return render_template('index.html.j2')
