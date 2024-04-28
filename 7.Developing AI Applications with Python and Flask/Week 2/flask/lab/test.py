from flask import Flask
app = Flask(__name__)

@app.route("/userdetails/<userid>")
def getUserDetails(userid):
    return "User Details for  "+userid

