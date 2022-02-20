from flask import Flask, url_for, render_template
import os
# from PIL import Image
# import cv2

DROWSY_FOLDER = os.path.join('static', 'img')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = DROWSY_FOLDER


@app.route("/")
def home_page():
    ADDPlus_icon = os.path.join(
        app.config['UPLOAD_FOLDER'], 'icon.png')
    return render_template("index.html", ADDPlus_icon=ADDPlus_icon)


@app.route("/about")
def about_page():
    ADDPlus_icon = os.path.join(
        app.config['UPLOAD_FOLDER'], 'icon.png')
    return render_template("pages/about.html", ADDPlus_icon=ADDPlus_icon)


@app.route("/download")
def download_page():
    ADDPlus_icon = os.path.join(
        app.config['UPLOAD_FOLDER'], 'icon.png')
    return render_template("pages/download.html", ADDPlus_icon=ADDPlus_icon)


@app.route("/how")
def how_page():
    ADDPlus_icon = os.path.join(
        app.config['UPLOAD_FOLDER'], 'icon.png')
    return render_template("pages/how.html", ADDPlus_icon=ADDPlus_icon)


@app.route("/instructions")
def instructions_page():
    # windows_defender = url_for('static', filename='img/windows_defender.jpg')
    ADDPlus_icon = os.path.join(
        app.config['UPLOAD_FOLDER'], 'icon.png')
    windows_defender = os.path.join(
        app.config['UPLOAD_FOLDER'], 'windows_defender.jpg')
    right_or_wrong_face = os.path.join(
        app.config['UPLOAD_FOLDER'], 'right_or_wrong_face.png')
    right_or_wrong_way = os.path.join(
        app.config['UPLOAD_FOLDER'], 'right_or_wrong_way.png')
    proper_detection = os.path.join(
        app.config['UPLOAD_FOLDER'], 'proper_detection.png')
    first = 'Open the website https://anti-drowsy-driving-plus.herokuapp.com/.'
    second = 'Click on “Home”, then click on “Download”.'
    third = 'Download version 1 if you only want drowsiness detection (ADD).'
    fourth = 'Download version 2 if you want drowsiness detection plus interaction (ADD+).'
    fifth = 'Open the file.'
    sixth = 'If it shows the picture below, then click “More info”, then click “Run anyway”.'
    seventh = 'The desktop app will be installed and then you can use it.'
    proper_one = 'Proper lighting: Enough lighting coming to face from the front, not from behind.'
    proper_two = 'Proper camera angle: The camera should be right in front of you.'
    proper_three = '''
    Proper detection: The app is ready to use if the green marks around your eyes and mouth closely follow your eyes’ and mouth’s movements, that is if you close your eyes, the green circle around your eye should also simultaneously go flat/ close; and when you open your mouth—like yawning, the green marks around your mouth should also widen up/ open. And, if you do steps 1 and 2 correctly, eyes and mouth proper detection should not be the problem.
    '''
    proper_four = 'Interaction: When asked, say “yes” or “no” clearly.'
    # img = cv2.imread(windows_defender)
    # width = 440
    # height = 340
    # dim = (width, height)
    # resized_windows_defender = cv2.resize(img, dim)
    # output_size = (125, 125)
    # i = Image.open(windows_defender)
    # resized_windows_defender = i.thumbnail(output_size)
    return render_template("pages/instructions.html", first=first, second=second, third=third, fourth=fourth,
                           fifth=fifth, sixth=sixth, seventh=seventh, windows_defender=windows_defender,
                           proper_one=proper_one, right_or_wrong_face=right_or_wrong_face, proper_two=proper_two,
                           right_or_wrong_way=right_or_wrong_way, proper_three=proper_three,
                           proper_detection=proper_detection, proper_four=proper_four, ADDPlus_icon=ADDPlus_icon
                           )


@app.route("/troubleshoot")
def troubleshoot_page():
    ADDPlus_icon = os.path.join(
        app.config['UPLOAD_FOLDER'], 'icon.png')
    return render_template("pages/troubleshoot.html", ADDPlus_icon=ADDPlus_icon)


@app.route("/why")
def why_page():
    car_collide = os.path.join(
        app.config['UPLOAD_FOLDER'], 'car_collide.png')
    car_collide1 = os.path.join(
        app.config['UPLOAD_FOLDER'], 'car_collide1.png')
    ADDPlus_icon = os.path.join(
        app.config['UPLOAD_FOLDER'], 'icon.png')
    return render_template("pages/why.html",
                           car_collide=car_collide, car_collide1=car_collide1, ADDPlus_icon=ADDPlus_icon)


if __name__ == '__main__':
    app.run(debug=False)
