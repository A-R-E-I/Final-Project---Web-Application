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

@app.route("/exit", methods=["POST"])
def UserExit():
    decision = request.form.get("confirm")
    if decision == "yes":
        return render_template("EndPro.html")
    else:
        return redirect("/")

@app.route("/info",methods=["POST"])
def GetInfo():
    global username
    global userpasswd
    username = request.form.get("txtusername")
    userpasswd= request.form.get("txtpassword")
    checkuse = request.form.get("txtusername")
    checkpass = request.form.get("txtpassword")
    if(username == "" or userpasswd == ""):
        return render_template("ExtractUser.html");
    else:
        CreateCheckFile();
        Infofilename = open(whichfilename,"r");
        UserValue = Infofilename.read().split(",");
        Infofilename.close();
        username = UserValue[0].strip();
        userpasswd = UserValue[1].strip();
        if(username == checkuse or userpasswd == checkpass):
            return render_template("difficultyselect.html");
        else:
            return render_template("ExtractUser.html");

         

def CreateCheckFile():
    fileDir = os.path.dirname(os.path.realpath("__file__"));
    fileexist = bool(path.exists(whichfilename));
    if(fileexist == False):
        status = "new";
    else:
        status = "edit"

    WriteToFile(status);

def WriteToFile(whichstatus):
    if(whichstatus == "new"):
        logacctfile = open(whichfilename,"x")
        logacctfile.close();
        logacctfile = open(whichfilename,"w")
    else:
        logacctfile = open(whichfilename,"a")

    logacctfile.write(str(username) + "," + str(userpasswd));
     
if __name__=="__main__":
    app.run();
