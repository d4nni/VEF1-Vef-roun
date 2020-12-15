from flask import Flask, render_template, json 
from markupsafe import escape
import urllib.request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/a-hluti')
def ahluti():
    return render_template('kennitala.html')

@app.route('/k-tala/<kt>')
def ktalan(kt):
    summa=0
    for item in kt:
        summa = summa + int(item)
    return render_template('ktsum.html',kt = kt,summa = summa)

# B-hluti

with open("C:/Users/danni/Desktop/HEROKU/vef2vf-d4nni/Verkefni-2-json/static/frjettir.json",encoding="utf-8") as skra:
    frjettir = json.load(skra)
#print(frjettir)

@app.route('/b-hluti')
def bhluti():
    return render_template('frettir.html', frjettir=frjettir)

@app.route('/frjett/<id>')
def news(id):
    return render_template('frett.html', frjettir=frjettir, id=id)

@app.errorhandler(404)
def pagenotfound(error):
    return render_template("pagenotfound.html"), 404

@app.errorhandler(500)
def servernotfound(error):
    return render_template("servererror.html"), 500

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'Hæ %s' % escape(username)

if __name__ == '__main__':
    app.run(debug=True,use_reloader=True)