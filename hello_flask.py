from flask import Flask, render_template

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

if __name__ == "__main__":
	app.run(debug=True)