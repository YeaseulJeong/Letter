import os
import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template, request, redirect, jsonify, url_for, send_file
from werkzeug.utils import secure_filename
app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.aeank.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta



@app.route('/')
def home():
   return render_template('index.html')


@app.route("/convert_page", methods=["GET"])
def convert_photo():
    return render_template('convert_page.html')


@app.route('/submit_img', methods=['POST'])
def submit_img():
    f = request.files['file']
    # title_receive= request.form['title']
    f.save('C:/Users/user/Desktop/Letter_Sparta/static/'+ "0_"+secure_filename(f.filename))

    return render_template('convert_page.html')


@app.route('/convert_img', methods=['POST'])
def convert_img():
    files = os.listdir('C:/Users/user/Desktop/Letter_Sparta/static')

    for file in files:
        if file.split("_")[0]=="0":
            return jsonify({'file_name': file})
        else:
            pass


@app.route('/download_img')
def download_img():
    return send_file('C:/Users/user/Desktop/Letter_Sparta/static/', as_attachment=True)


if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)