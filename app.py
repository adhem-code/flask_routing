from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Belajar Flask Fundamental</h1>"

@app.route("/about")
def about():
    return "<h1>Ini adalah halaman tentang Flask!</h1>"

@app.route("/user/<username>")  
def user(username):
    return "<h1>Selamat Datang {}!</h1>".format(username)

@app.route("/<no_ktp>")  
def clean(no_ktp):
    return f"<h1>{escape(no_ktp)}</h1>"

if __name__ == "__main__":
    app.run(debug=True)