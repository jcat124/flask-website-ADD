from flask import Flask, url_for, render_template
import os


DROWSY_FOLDER = os.path.join('static', 'img')


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = DROWSY_FOLDER


@app.route("/")
def home_page():
	full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'drowsy-img.png')
	return render_template("index.html",  drowsy_image = full_filename)


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
	return render_template("pages/instructions.html")


@app.route("/troubleshoot")
def troubleshoot_page():
	return render_template("pages/troubleshoot.html")


@app.route("/why")
def why_page():
	return render_template("pages/why.html")



if __name__ == '__main__':
	app.run(debug=False)
