from flask import Flask 
  
app = Flask(__name__) 
  
@app.route("/")
def hello():
    return "Hello World!"

def home_view(): 
        return "<h1>Welcome to Geeks for Geeks</h1>"
