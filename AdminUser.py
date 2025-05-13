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
    filepath = fileDir + "\\AUpass.py";
    filenamepath = {
        "__file__":filepath,
        "__name__":"__main__",
        };
    with open(filepath,"rb") as file:
        exec(compile(file.read(), filepath, "exec"),filenamepath);

    if __name__=="__main__":
        main();
