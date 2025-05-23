from flask import Flask, render_template, request, redirect
import os.path
import sys
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
    account = request.form.get("WhatAccount")
    if(account == "AdminAct"):
        return render_template("ExtractAdmin.html");
    else:
        return render_template("ExtractUser.html");

    
if __name__=="__main__":
    app.run();
