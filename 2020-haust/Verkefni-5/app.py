from flask import Flask, render_template, request, session, redirect, url_for
import pyrebase

app = Flask(__name__)

app.config['SECRET_KEY'] = 'COVID20'

# tengin við firebase realtime database á firebase.google.com ( db hjá danielsimongalvez@gmail.com )
config = {
    # hér kemur tengingin þín við Firebase gagnagrunninn ( realtime database )
    "apiKey": "AIzaSyAGFh9E9I8PWhJ7vDmJv-pg7yQg5shMCEM",
    "authDomain": "verk5-5d264.firebaseapp.com",
    "databaseURL": "https://verk5-5d264.firebaseio.com",
    "projectId": "verk5-5d264",
    "storageBucket": "verk5-5d264.appspot.com",
    "messagingSenderId": "427320977728",
    "appId": "1:427320977728:web:6341c7137b878ff88df2a5",
    "measurementId": "G-KN5SXQL5PW"
}

fb = pyrebase.initialize_app(config)
db = fb.database()

# Test route til að setja gögn í db
@app.route('/')
def index():
     #skrifum nýjan í grunn hnútur sem heitir notandi 
    #db.child("users").push({"usr":"Johnny", "pwd":"Begood"}) 
    return render_template('index.html')

@app.route('/login', methods=['Get', 'POST'])
def login():
    if request.method == 'POST':
        usr = request.form['usrname']
        pwd = request.form['pswd']

        # tjékka á database, er user til?
        u = db.child('users').get().val()
        lst = list(u.items())
        for i in lst:
            if usr == i[1]['usr'] and pwd == i[1]['pwd']:
                login = True
                break
            else:
                login = False
            
        if login:
            # user fær session id
            session['logged_in'] = usr
            return redirect('/topsecret')
        else:
            return render_template('nologin.html')
    else:
        return render_template('no_method.html')

@app.route('/topsecret')
def secret():
    if 'logged_in' in session:
        return render_template('topsecret.html') 
    else:
        return redirect('/')

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

# # förum í grunn og sækjum allar raðir ( öll gögn )
# u = db.child("notandi").get().val()
# lst = list(u.items()) 