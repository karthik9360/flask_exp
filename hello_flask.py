from flask import Flask, render_template, redirect, request
import datetime

app = Flask(__name__)

@app.route("/")
def index():
  return "Flask Working fine"

@app.route("/login")
def templates():
  return render_template("web page.html")

@app.route("/pageone")
def template():
  return render_template("firstpage.html")

@app.route("/pagetwo")
def templat():
  return render_template("secondpage.html")
  
@app.route("/frontpage")
def temp():
  return render_template("frontpage.html")
  
@app.route("/resultpage")
def templ():
  return render_template("resultpage.html")
  
@app.route("/printtime")
def printtime():
   print ()
   print (datetime.datetime.now())
   print ()
   return redirect("/resultpage")
   
@app.route("/dashboard")
def dashboard():
  name = "Kumar"
  notification = 60
  mail = 100
  return render_template("dashboard.html", name_temp = name, notification_temp = notification, mail_temp = mail)
  
@app.route("/inputpage")
def inputpage():
  return render_template("inputpage.html")
  
@app.route("/statuspage",methods=["GET"])
def statuspage():
  status = request.args.get("input")
  return render_template("statuspage.html", status_temp = status)
  
@app.route("/formpage")
def formpage():
  return render_template("formpage.html")

@app.route("/submit", methods=["POST"])
def submit():
  username = request.form.get("username")
  password = request.form.get("password")
  return render_template("submit.html", username_temp = username, password_temp = password )
if __name__ == "__main__":
	app.run(debug=True)