#./app/app.py

from flask import Flask, render_template, request, flash, redirect, url_for, session
import os
import io
from PIL import Image
from uuid import uuid4
import base64
from model import lightUp

UPLOAD_FOLDER = 'upload'

app = Flask(__name__)
app.secret_key='this-is-a-secret-key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')
    
@app.route('/examples')
def examples():
    return render_template('examples.html')
    
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/lightup', methods=['GET','POST'])
def light_up():
    if request.method == 'POST':
        image=request.files['file']
        extension=image.filename.split('.')[-1]
        if extension not in ['jpeg','jpg','png']:
        	flash('Unsupported format :( - Supported formats are .jpg, .jpeg and .png')
        	return render_template('lightup-input.html')
        identifier=uuid4()
        path = os.path.join(app.config['UPLOAD_FOLDER'],str(identifier)+'-'+image.filename)
        image.save(path)
        output, resized = lightUp(path)
        os.remove(path)
        #if resized == None:
        #	flash('The image is too small :( - The minimum height and width are 128 pixels.')
        #	return render_template('lightup-input.html')
        output = Image.fromarray(output.astype("uint8"))
        w, h = output.size
        if resized:
        	flash('Warning: Your image was too large, so it was resized to width ' + str(w) + ' and height ' +str(h)+'.')
        width="80%"
        if (h/w>0.5): # Adjust display dimensions
        	width=str(40*w/h)+"%" # Same proportions. Height limited to 40% and width limited to 80%
        rawBytes = io.BytesIO()
        extension_aux=extension
        if extension_aux.lower()=='jpg':
        	extension_aux='JPEG'
        output.save(rawBytes, extension_aux)
        rawBytes.seek(0)
        img_base64 = base64.b64encode(rawBytes.getvalue()).decode('ascii')
        mime = "image/"+str(extension)
        uri = "data:%s;base64,%s"%(mime, img_base64)
        return render_template('lightup-output.html', img=uri, width=width, filename=image.filename)
    else:
        return render_template('lightup-input.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
