from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "ward abdo"
password = "2007"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]

@app.route('/')
def friends():
	return render_template(
		'home.html' , Friends = facebook_friends)

@app.route('/' , methods=['GET','POST'])  # '/' for the default page
def login():
	if  request.method == 'GET':
		return render_template('login.html')
	else:
		name = request.form['username']
		password02 = request.form['password']
	if password == password02 and username == name:
		return redirect(url_for('home'))
	else:
		return render_template('login.html')

@app.route('/home')
def home():
		return render_template('home.html' , friends = facebook_friends)


@app.route('/friend_exist/<string:name>' , methods=['GET' , 'POST'])
def friend_exist(name):
	if name in facebook_friends:
		F= True
	else:
		F=False
	return render_template('friend_exist.html', F=F , name=name)



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)