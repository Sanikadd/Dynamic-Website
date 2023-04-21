from flask import Blueprint, render_template, request, redirect, url_for, flash

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
      return render_template('login.html')


