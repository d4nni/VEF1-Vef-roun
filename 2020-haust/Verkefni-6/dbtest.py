from flask import Flask
import pyrebase

app = Flask(__name__)

# tengin við firebase realtime database á firebase.google.com ( db hjá danielsimongalvez@gmail.com )
config = {
    # hér kemur tengingin þín við Firebase gagnagrunninn ( realtime database )
    "apiKey": "AIzaSyDnVt5TSs145VbYylk6zqhQmN4dZY8b80I",
    "authDomain": "dbtest-6bbc5.firebaseapp.com",
    "databaseURL": "https://dbtest-6bbc5.firebaseio.com",
    "projectId": "dbtest-6bbc5",
    "storageBucket": "dbtest-6bbc5.appspot.com",
    "messagingSenderId": "451843601795",
    "appId": "1:451843601795:web:8cc2e7cf15b4c7d18372b6",
    "measurementId": "G-Z0CZX4HB2P"
}

fb = pyrebase.initialize_app(config)
db = fb.database()

# Test route til að setja gögn í db
@app.route('/')
def index():
     #skrifum nýjan í grunn hnútur sem heitir notandi 
    db.child("notandi").push({"notendanafn":"Palli", "lykilorð":"sdfsf"}) 
    return "Skrifað í grunn"

# Test route til að sækja öll gögn úr db
@app.route('/lesa')
def lesa():
    # # förum í grunn og sækjum allar raðir ( öll gögn )
    u = db.child("notandi").get().val()
    lst = list(u.items())
    print(lst)
    return "Lesum úr grunni"

if __name__ == "__main__":
	app.run(debug=True)

# # förum í grunn og sækjum allar raðir ( öll gögn )
# u = db.child("notandi").get().val()
# lst = list(u.items())