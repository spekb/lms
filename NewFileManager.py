from flask import Flask, abort, app, flash, redirect, render_template, request, send_file, url_for
import os
from werkzeug.utils import secure_filename
import socket
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
BASE_DIR = "resources"
auth = HTTPBasicAuth()

users = {
    "admin": generate_password_hash("pw1"),                     #change this password
    "guest": generate_password_hash("pw2")                      #change this password
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route('/')
def navbar():
    return render_template('index.html')

@app.route('/a/', defaults={'req_path': ''})
@app.route('/<path:req_path>')
def home(req_path):
    
    # Joining the base and the requested path
    abs_path = os.path.join(BASE_DIR, req_path)

    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return abort(404)

    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        if abs_path.endswith("klink"):
            filename = os.path.basename(abs_path)
            # return redirect(filename)
            # Get the local IP address
            print("b")
            print(abs_path)
            ip = socket.gethostbyname(socket.gethostname())
            with open(abs_path, 'r') as file:
                file_content = file.read()
                return redirect("http://" + ip + ":81/" + file_content)
        else:
            print("a")
            return send_file(abs_path)

    # Show directory contents
    files = os.listdir(abs_path)
    for x in files:
        if x.endswith("txt"):
            files.remove(x)
            print(x)
    for x in files:
        if x.endswith("jpeg"):
            files.remove(x)
            print(x)
    descriptions = []
    names=[]
    for x in files:
        names.append(os.path.basename(x))
        try:
            with open(BASE_DIR+x+".txt", 'r') as file:
                file_content = file.read()
                descriptions.append(file_content)
        except FileNotFoundError:
            # Handle the case when the file is not found
            descriptions.append("")
        except Exception as e:
            # Handle any other exceptions
            descriptions.append("An error occurred: " + str(e))
        
    print(files)
    return render_template('files.jinja2', files=files, names=names, descriptions=descriptions, req_path=req_path+"/")


def disallowed_file(filename):
    DISALLOWED_EXTENSIONS={'html','php'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in DISALLOWED_EXTENSIONS

@app.route('/admin', methods=['GET', 'POST'])
@auth.login_required
def upload():
    UPLOAD_DIR=BASE_DIR+"/Uploads"
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and not disallowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_DIR, filename))
            return "Success"
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
    
if __name__ == '__main__':
    app.run(debug=True, port=82, host='0.0.0.0')