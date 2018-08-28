from flask import Flask,render_template,request,redirect,url_for
import numpy as np
import os
from model.sobel import Sobel

app = Flask(__name__)
PATH = 'index.html' # you have to add files in templates
ins = Sobel()

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

if __name__ =='__main__':
    app.debug = True
    app.run(host='0.0.0.0')
