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
        if(account == 1):
            return render_template("ExtractAdmin.html");
        else:
            return render_template("ExtractUser.html");
