from flask import Flask, render_template, request, redirect
from os import path
import os.path
import sys


global whichfilename;
whichfilename = "LoginAdmin.doc";
userfile = "LoginUser.doc";

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("AdminUser.html")

@app.route("/select",methods=["POST"])
def WhichAccount():
    UserExit = request.form.get("ExitYN")
    if(UserExit == "entyes"):
        return render_template("EndPro.html");
    
    account = request.form.get("WhatAccount")
    if(account == "AdminAct"):
        return render_template("ExtractAdmin.html");
    else:
        return render_template("ExtractUser.html");
     
if __name__=="__main__":
    app.run();
