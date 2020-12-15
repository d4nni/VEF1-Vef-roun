from flask import Flask, render_template, session, url_for, redirect, request
from markupsafe import escape
import os
from datetime import datetime

app = Flask(__name__)

app.secret_key = os.urandom(8)
print(os.urandom(8))

# dict listi
vorur = [
    [0, "Peysa","peysa.jpg",2500],
    [1, "Skór","skor.jpg",3500],
    [2, "Buxur","buxur.jpg",5000],
    [3, "Trefill","trefill.jpg",3000],
    [4, "Jakki","jakki.jpg",10000],
    [5, "Húfa","hufa.jpg",6000],
]

# hægt að skila þessu líka: return redirect(url_for("index"),v=vorur,fjoldi=fjoldi)
@app.route('/')
def index():
    karfa = []
    fjoldi = 0
    if 'karfa' in session:
        karfa = session['karfa']
        fjoldi = len(karfa)
    return render_template('index.html',v=vorur, fjoldi=fjoldi)

# hægt að skila líka þessu: render_template('index.html',v=vorur, fjoldi=fjoldi)
@app.route('/add/<int:id>')
def teljari(id):
    karfa = []
    fjoldi = 0
    if 'karfa' in session:
        karfa = session['karfa']
        karfa.append(vorur[id])
        session['karfa'] = karfa
        fjoldi = len(karfa)
    else:
        karfa.append(vorur[id])
        session['karfa'] = karfa
        fjoldi = len(karfa)
    return redirect(url_for("index"))

@app.route("/karfa")
def karfa():
    karfa = []
    summa = 0
    #karfan er ekki tóm
    if 'karfa' in session:
        karfa = session['karfa']
        fjoldi = len(karfa)
        for i in karfa:
            summa += int(i[3])
        return render_template('karfa.html', k = karfa, tom = False, fjoldi = fjoldi, samtals = summa)
    else:
        return render_template('karfa.html', k = karfa, tom = True)

# taka út vöru úr lista
@app.route("/eydavoru/<int:id>")
def delete(id):
    karfa = []
    karfa = session['karfa']
    vara = 0
    # finna vöruna
    for i in range(len(karfa)):
        if karfa[i][0] == id:
            vara = i
    karfa.remove(karfa[vara])
    session['karfa'] = karfa
    return redirect(url_for("karfa"))

@app.route("/eyda")
def hreinsun():
    session.pop('karfa', None) # tæma körfu
    return redirect(url_for("index"))

@app.route("/form")
def skilaFormi():
    summa = 0
    if 'karfa' in session:
        karfa = session['karfa']
        for i in karfa:
            summa += int(i[3])
        return render_template('form.html',samtals = summa)

@app.route("/results", methods = ['POST'])
def postform():
    if request.method == 'POST':
        kwargs={
            'nafn': request.form['nafn'],
            'email': request.form['email'],
            'simi': request.form['simi'],
            'samtals': request.form['samtals']
        }
        return render_template('results.html',**kwargs)


@app.errorhandler(404)
def pagenotfound(error):
    return render_template("pagenotfound.html"), 404

@app.errorhandler(500)
def servernotfound(error):
    return render_template("servererror.html"), 500

if __name__ == '__main__':
    app.run(debug=True,use_reloader=True)

#use_reloader=True