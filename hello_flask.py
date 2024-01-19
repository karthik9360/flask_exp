from flask import Flask, render_template, redirect
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

if __name__ == "__main__":
	app.run(debug=True)