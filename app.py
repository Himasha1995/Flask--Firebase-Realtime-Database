import pyrebase

config = {
  "apiKey": "AIzaSyAd54Rr0cf7NUcIAZt54G6gIJ7e1Kcv1ok",
  "authDomain": "first-flask-app-7d9d9.firebaseapp.com",
  "projectId": "first-flask-app-7d9d9",
  "storageBucket": "first-flask-app-7d9d9.appspot.com",
  "messagingSenderId": "63828194174",
  "appId": "1:63828194174:web:2db68dae03c024aa18392f",
  "measurementId": "G-VT4B240WWD",
  "databaseURL": "https://first-flask-app-7d9d9-default-rtdb.firebaseio.com/",
};

firebase = pyrebase.initialize_app(config)

db = firebase.database()

from flask import*

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def basic():
	if request.method == 'POST':
		if request.form['submit'] == 'add':

			name = request.form['name']
			email = request.form['email']
			db.child("todo").push(name)
			db.child("todo").push(email)
			todo = db.child("todo").get()
			to = todo.val()
			return render_template('index.html', t=to.values())
		elif request.form['submit'] == 'delete':
			db.child("todo").remove()
		return render_template('index.html')
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)