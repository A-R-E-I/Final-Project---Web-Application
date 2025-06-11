from flask import Flask, render_template, request, redirect
from os import path
import os.path

global whichfilename;
whichfilename = "LoginAdmin.doc";
userfile = "LoginUser.doc";

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("AdminUser.html")

@app.route("/select",methods=["POST"])
def WhichAccount():
    account = request.form.get("WhatAccount")
    match(account):
        
        case("AdminAct"):
            return render_template("ExtractAdmin.html");
    
        case("UserAct"):
            return render_template("ExtractUser.html");

        case("Leave"):
            return render_template("RUsure.html");
     
if __name__=="__main__":
    app.run();
