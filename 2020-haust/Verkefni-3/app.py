from flask import Flask, render_template, json 
from markupsafe import escape
import urllib.request
import os
from datetime import datetime
from jinja2 import ext

app = Flask(__name__)

with urllib.request.urlopen("http://apis.is/petrol/") as url:
    data = json.loads(url.read().decode())

def format_time(data):
    return datetime.strptime(data, '%Y-%m-%dT%H:%M:%S.%f').strftime('%d/%m-%Y %H:%M')

app.jinja_env.filters['format_time'] = format_time

app.jinja_env.add_extension(ext.do)

def minPetrol():
    minPetrolPrice = 1000
    company = None
    address = None
    lst = data['results']
    for i in lst:  
        if i['bensin95'] is not None:
            if i['bensin95'] < minPetrolPrice:
                minPetrolPrice = i['bensin95']
                company = i['company']
                address = i['name']
    return [minPetrolPrice, company, address]

def minDiesel():
    minDieselPrice = 1000
    company = None
    address = None
    lst = data['results']
    for i in lst:  
        if i['diesel'] is not None:
            if i['diesel'] < minDieselPrice:
                minDieselPrice = i['diesel']
                company = i['company']
                address = i['name']
    return [minDieselPrice, company, address]

@app.route('/')
def home():
    return render_template('index.html', data=data, minP=minPetrol(), minD = minDiesel())

@app.route('/company/<company>')
def comp(company):
    return render_template('company.html', data=data, com=company)

@app.route('/moreinfo/<key>')
def info(key):
    return render_template('moreinfo.html',data=data,k=key)

@app.errorhandler(404)
def pagenotfound(error):
    return render_template("pagenotfound.html"), 404

@app.errorhandler(500)
def servernotfound(error):
    return render_template("servererror.html"), 500

if __name__ == '__main__':
    app.run(debug=True,use_reloader=True)