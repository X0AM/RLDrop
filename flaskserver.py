from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/', methods=["GET", "POST"])
def index():   
  return render_template("home.html")
app.run(host='0.0.0.0', port=80, debug=True)