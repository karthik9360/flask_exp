from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return "Flask Working fine"

@app.route("/login")
def template():
  return render_template("web page.html")

if __name__ == "__main__":
	app.run(debug=True)