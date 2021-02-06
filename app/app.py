#./app/app.py

from flask import Flask, render_template, request, flash, redirect, url_for
from model import lightUp
from tempfile import NamedTemporaryFile
from shutil import copyfileobj

app = Flask(__name__)
# Página principal, con índice
@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/lightup', methods=['GET','POST'])
def light_up():    
    if request.method == 'POST':
        # Procesar imagen
        inimg=request.files.get('input-img','')
        app.logger.debug(type(inimg))
        app.logger.debug(inimg)
        outimg=lightUp(inimg)
        tempFileObj = NamedTemporaryFile(suffix='jpg')
        coyfileobj(outimg, tempFileObj)
        return render_template('lightup-output.html', img=tempFileObj)
    else:
        return render_template('lightup-input.html')
        
# Manejador de error 404: URL no definida
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
