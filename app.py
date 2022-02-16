from flask import Flask, url_for, render_template
import os

DROWSY_FOLDER = os.path.join('static', 'img')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = DROWSY_FOLDER


@app.route("/")
def home_page():
    drowsy_image = os.path.join(app.config['UPLOAD_FOLDER'], 'drowsy-img.png')
    return render_template("index.html", drowsy_image=drowsy_image)


@app.route("/about")
def about_page():
    return render_template("pages/about.html")


@app.route("/download")
def download_page():
    return render_template("pages/download.html")


@app.route("/how")
def how_page():
    return render_template("pages/how.html")


@app.route("/instructions")
def instructions_page():
    windows_defender = os.path.join(app.config['UPLOAD_FOLDER'], 'windows_defender.jpg')
    first = 'Open the website https://jcat124.github.io/website/.'
    second = 'Click on “Home”, then click on “Download”.'
    third = 'Download version 1 if you only want drowsiness detection (ADD).'
    fourth = 'Download version 2 if you want drowsiness detection plus interaction (ADD+).'
    fifth = 'Open the file.'
    sixth = 'If it shows the picture below, then click “More info”, then click “Run anyway”.'
    return render_template("pages/instructions.html", first=first, second=second, third=third, fourth=fourth, fifth=fifth, sixth=sixth, windows_defender=windows_defender)


@app.route("/troubleshoot")
def troubleshoot_page():
    return render_template("pages/troubleshoot.html")


@app.route("/why")
def why_page():
    return render_template("pages/why.html")


if __name__ == '__main__':
    app.run(debug=True)
