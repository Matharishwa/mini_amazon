from flask import Flask,request,render_template,redirect,url_for,session
import requests



app=Flask(__name__)
app.secret_key='hello'



@app.route('/')
def home():
	return	render_template('home.html',title="home")
	


@app.route('/about')
def about():
	return	render_template('about.html',title="about")

@app.route('/contact')
def contact():
	return	render_template('contact.html',title="contact")	

@app.route("/login",methods=['GET','POST'])
def login():
	if request.method=='POST':
		users={
		'user1':'123',
		'user2':'456',
		'user3':'789',
		'user4':'012'}
		username=request.form['username']
		password=request.form['password']

		if username not in users:
			return"User doesn't exist.Go back and enter a valid username"
		if users[username]!=password:
			return "password doesn't match.Go back enter the correct password"
		session['username']=username
		return redirect(url_for('home'))
	return redirect(url_for('home'))

@app.route("/logout",methods=['GET','POST'])
def logout():
	session.clear()
	return redirect(url_for('home'))
app.run(debug=True)


