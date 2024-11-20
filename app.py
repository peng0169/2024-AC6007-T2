# flask is a framework of back end programing: a library
# a way to simplified the code
# pip install: python installed has a small library, and the other library is in the internet
# using install to introduce the library
# front -> website -> DMS -> router -> ISP -> internet -> back end (app.py)
# the protocal is call TCP/IP
# python use WSGI to convert to TCP/IP
# gunicorn.py help using the the WSGI protocal
from flask import Flask
from flask import render_template,request

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

if __name__ == "__main__":
    app.run()