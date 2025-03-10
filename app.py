# flask is a framework of back end programing: a library
# a way to simplified the code
# pip install: python installed has a small library, and the other library is in the internet
# using install to introduce the library
# front -> website -> DMS -> router -> ISP -> internet -> back end (app.py)
# the protocal is call TCP/IP
# python use WSGI to convert to TCP/IP
# gunicorn.py help using the the WSGI protocal
# install python, pip install flask, 
from flask import Flask
from flask import render_template,request
import textblob

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/SA",methods=["GET","POST"])
def SA():
    return(render_template("SA.html"))

@app.route("/SA_result",methods=["GET","POST"])
def SA_result():
    q = request.form.get("q")
    r = textblob.TextBlob(q).sentiment
    return(render_template("SA_result.html", r = r))

@app.route("/paynow",methods=["GET","POST"])
def paynow():
    return(render_template("paynow.html"))

if __name__ == "__main__":
    app.run()