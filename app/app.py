#./app/app.py

from flask import Flask, render_template, request, flash, redirect, url_for

import tensorflow as tf

app = Flask(__name__)
# Página principal, con índice
@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/lightup', methods=['GET','POST'])
def lightUp():    
    if request.method == 'POST':
        # Procesar imagen
        inimg=flask.request.files.get('input-img','')
        app.logger.debug(type(inimg))
        return render_template('lightup-output.html')
    else:
        return render_template('lightup-input.html')
        
# Manejador de error 404: URL no definida
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
