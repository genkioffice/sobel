from flask import Flask,render_template,request,redirect,url_for,send_from_directory,jsonify
import numpy as np
from werkzeug import secure_filename
import os
import sys
import sqlite3
sys.path.append('model')
from sobel_func import Sobel
import cv2

PATH = 'index.html' # you have to add files in templates

# UPLOAD_FOLDER = './data/uploads'
UPLOAD_FOLDER = './static'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = os.urandom(24)

sob = Sobel()

@app.route('/')
def index():
    message = "Hello Hello"
    return render_template(PATH,message=message)

@app.route('/post',methods=['GET','POST'])
def post():
    if request.method == 'POST':
        name = request.form['name']
        return render_template('index.html',name=name)
    else:
        return redirect(url_for('index.html'))#例外処理

@app.route('/send', methods=['GET','POST'])
def send():
    if request.method == 'POST':
        img_file = request.files['img_file']
        filename = secure_filename(img_file.filename)
        img_file.save(os.path.join(app.root_path,app.config['UPLOAD_FOLDER'], filename))
        # img_url = '/static/' + filename
        img_url = os.path.join(app.root_path,'static',filename)
        return render_template('index.html',img_url=img_url,filename=filename)
    else:
        redirect(url_for('index'))


#no needed
@app.route('/static/<filename>', methods=['GET'])
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ =='__main__':
    app.debug = True
    app.run(host='0.0.0.0')
