from flask import Flask, render_template, request, redirect
import os.path
from os import path

global whichfilename;
whichfilename = "LoginAdmin.doc";
userfile = "LoginUser.doc";

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("AdminUser.html")

@app.route("/select",methods=["POST"])
def WhichAccount():
    global account
    account = request.form.get("txtaccount")
    if(account == ""):
        return render_template("AdminUser.html");
    else:
        return render_template("ExtractInfo.html");

    
if __name__=="__main__":
    app.run();
