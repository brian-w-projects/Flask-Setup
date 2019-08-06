from flask import render_template, request, jsonify, session, flash, redirect, url_for, current_app
from . import main
from .forms import TermForm
# from ..models import
import os


@main.route('/')
def index():
    return render_template('main/index.html')
