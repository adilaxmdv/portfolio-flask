from flask import Flask,redirect,url_for,render_template,send_from_directory
import os
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/blogs')
def blogs():
    return render_template("blogs.html")

@app.route('/portfolio')
def portfoilo():
    return render_template("portfoilo.html")
@app.route('/cv')
def cv():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/pdf'
    return send_from_directory(filepath, 'cv.pdf')


if __name__ == "__main__":
    app.run(debug= True)