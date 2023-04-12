from flask import Blueprint, render_template, request, redirect, url_for, flash

views = Blueprint('views', __name__)

# @views.route('/')
# def home():
#     return "<h1>hi</h1>"

@views.route('/')
def home():
      return render_template('index.html')

@views.route('/products')
def products():
      return render_template('full_prod_page.html')

@views.route('/whyus')
def whyus():
      return render_template('whyus.html')