#!/bin/python3
from flask import Flask, render_template, redirect, flash, request, url_for, session
from werkzeug.utils import secure_filename
import subprocess
import os

UPLOAD_FOLDER = './static/Q'
CAMERA_FEED = '172.22.1.142:4747'

def getCamIP():
    with open('cameralinks.txt', 'r') as f:
        for line in f:
            pass
        last_line = line
    cameralink = last_line.split(" ", 1)[0]
    return cameralink



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "In iordan botiezandu-tie, Tu, Domnieeeeee"

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        # check if the post request has the file part
        print(request.files)
        if 'plfile' not in request.files:
            return "<p>file not found</p>"
        userfile = request.files['plfile']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if userfile.filename == "":
            return "<p>file empty</p>"
        if userfile:
            filename = secure_filename(userfile.filename)
            session['filename'] = secure_filename(userfile.filename)
            userfile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print("file recieved")
            subprocess.call("../3dpreview.sh static/Q/" + filename, shell=True)
            return redirect(url_for('preview3d', imagename=filename))
    else:
        return render_template("base.html")

@app.route("/preview/<imagename>")
def preview3d(imagename):
    return render_template("preview.html", imagename=("../static/Q/" + imagename.rsplit('.', 1)[0] + ".jpg"))

@app.route("/print/<gcodename>")
def print3d(gcodename):
    subprocess.call("../3dprint.sh static/Q/" + gcodename.rsplit('.', 1)[0] + ".gcode", shell=True)
    return "<h1> busy </h1>"

@app.route("/feed/")
def feed():
    subprocess.call("ffmpeg -i /dev/video0 -listen 1 -vcodec libx264 -crf 32 -f mp4 -movflags +faststart+frag_keyframe+empty_moov http://localhost:8787 &", shell=True)
    return redirect("https://" + getCamIP(), code=302)
    #return redirect("http://172.22.16.226:8787" , code=302)

if __name__ == '__main__' :
    app.run( host='0.0.0.0', port='42069', debug=True )
