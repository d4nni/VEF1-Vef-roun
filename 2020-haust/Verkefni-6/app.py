from flask import Flask, render_template, request, session, redirect, url_for
import pyrebase

app = Flask(__name__)

app.config['SECRET_KEY'] = 'COVID20'

# tengin við firebase realtime database á firebase.google.com ( db hjá danielsimongalvez@gmail.com )
config = {
    # hér kemur tengingin þín við Firebase gagnagrunninn ( realtime database )
    "apiKey": "AIzaSyAG1hNjNk8vKQuMLGv1vFZADpfXTDknTrc",
    "authDomain": "verk6-8c13b.firebaseapp.com",
    "databaseURL": "https://verk6-8c13b.firebaseio.com",
    "projectId": "verk6-8c13b",
    "storageBucket": "verk6-8c13b.appspot.com",
    "messagingSenderId": "675147085965",
    "appId": "1:675147085965:web:018e7a5a3a9116674f8ac4",
    "measurementId": "G-LKCN03D8XV"
}

fb = pyrebase.initialize_app(config)
db = fb.database()

# Test route til að setja gögn í db
@app.route('/')
def index():
     #skrifum nýjan í grunn hnútur sem heitir notandi 
    #db.child("users").push({"usr":"Johnny", "pwd":"Begood"}) 
    #db.child("bill").push({'nr':'HOK25','tegund':'PORSCHE','utegund':'TAYCAN','argerd':'2021','akstur':'500','verd':'30m'})
    return render_template('index.html')

#### LOG IN PASSWORD OG USER ########
# User: danni
# PassWord: ok123
######################
@app.route('/login', methods=['Get', 'POST'])
def login():
    if request.method == 'POST':
        usr = request.form['usrname']
        pwd = request.form['pswd']

        # tjékka á database, er user til?
        u = db.child('users').get().val()
        lst = list(u.items())
        global username
        for i in lst:
            if usr == i[1]['usr'] and pwd == i[1]['pwd']:
                login = True
                username = i[1]['usr']
                break
            else:
                login = False
            
        if login:
            # user fær session id
            session['logged_in'] = usr
            return redirect('/bilasala')
        else:
            return render_template('nologin.html')
    else:
        return render_template('no_method.html')

@app.route('/bilasala')
def secret():
    if 'logged_in' in session:
        b = db.child('bill').get().val()
        lst = list(b.items())
        return render_template('bilasala.html',bilar = lst, user = username) 
    else:
        return redirect('/')

@app.route('/bill/<id>')
def car(id):
    c = db.child('bill').child(id).get().val()
    bill = list(c.items())
    return render_template('car.html',bill = bill, id = id)

@app.route('/bill/breytaeyda',methods=['POST'])
def breytaeyda():
    if request.method == 'POST':
        if request.form['submit'] == 'eyda':
            db.child('bill').child(request.form['id']).remove()
            return render_template('deleted.html',nr = request.form['nr'])
        else:
            db.child('bill').child(request.form['id']).update(
                {
                    'nr':request.form['nr'],
                    'tegund':request.form['tegund'],
                    'utegund':request.form['utegund'],
                    'argerd':request.form['argerd'],
                    'akstur':request.form['akstur'],
                    'verd':request.form['verd']
                }
            )
            return render_template('updated.html',nr = request.form['nr'])
    else:
        return render_template('no_method.html')

@app.route('/nyskra')
def nyskra():
    return render_template('nyskrabil.html')

@app.route('/nyskrabil', methods=['POST'])
def nyskrabil():
    skrnr = []
    if request.method == 'POST':

        nr = request.form['nr']
        tegund = request.form['tegund']
        utegund = request.form['utegund']
        argerd = request.form['argerd']
        akstur = request.form['akstur']
        verd = request.form['verd']

        u = db.child('bill').get().val()
        lst = list(u.items())
        for i in lst:
            skrnr.append(i[1]['nr'])
        if nr not in skrnr:
            db.child('bill').push({ 'nr':nr, 'tegund':tegund, 'utegund':utegund, 'argerd':argerd, 'akstur':akstur,'verd':verd })
            return render_template('nyskrabilok.html',nr=nr)
        else:
            return render_template('billertil.html',nr=nr)
        



@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/doregister',methods=['GET','POST'])
def doregister():
    usernames = []
    if request.method == 'POST':

        usr = request.form['usrname']
        pwd = request.form['pswd']
        #ná í db og ath hvort notandi sé til
        u = db.child('users').get().val()
        lst = list(u.items())
        for i in lst:
            usernames.append(i[1]['usr'])
        #óskráður
        if usr not in usernames:
            db.child('users').push({'usr':usr, 'pwd':pwd})
            return render_template('registered.html')
        else:
            return render_template('userexist.html')
    else:
        return render_template('no_method.html')
 
@app.errorhandler(404)
def pagenotfound(error):
    return render_template("pagenotfound.html"), 404

@app.errorhandler(500)
def servernotfound(error):
    return render_template("servererror.html"), 500

if __name__ == "__main__":
	app.run(debug=True)

# förum í grunn og sækjum allar raðir ( öll gögn )
# u = db.child("notandi").get().val()
# lst = list(u.items()) 