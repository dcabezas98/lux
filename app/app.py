#./app/app.py

from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
import os
import io
from PIL import Image
from uuid import uuid4
import base64
from model import lightUp

HOST='localhost'
PORT_NUMBER='8080'

UPLOAD_FOLDER = 'upload'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
        image=request.files['input-img']
        extension=image.filename.split('.')[-1]
        identifier=uuid4()
        path = os.path.join(app.config['UPLOAD_FOLDER'],str(identifier)+'-'+image.filename)
        image.save(path)
        output=lightUp(path)
        os.remove(path)
        output = Image.fromarray(output.astype("uint8"))
        rawBytes = io.BytesIO()
        extension_aux=extension
        if extension_aux.lower()=='jpg':
        	extension_aux='JPEG'
        output.save(rawBytes, extension_aux)
        rawBytes.seek(0)
        img_base64 = base64.b64encode(rawBytes.getvalue()).decode('ascii')
        mime = "image/"+str(extension)
        uri = "data:%s;base64,%s"%(mime, img_base64)
		# TODO: borrar en upload
        return render_template('lightup-output.html', img=uri)
    else:
        return render_template('lightup-input.html')
        
# Manejador de error 404: URL no definida
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    
if __name__ == '__main__':
	app.run(host=HOST, port=PORT_NUMBER, debug=True)
