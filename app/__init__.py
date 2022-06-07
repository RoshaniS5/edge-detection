from flask import Flask, render_template, request, redirect
from edgedetection import *

app = Flask(__name__)

@app.route("/")
def image():
    # sobel("./static/flower.png", "edges")
    # gaussianBlur("./static/flower.png")
    # sobel("./static/blur.png", "edges2")
    return render_template('index.html', res=False)

@app.route("/submit", methods=['GET', 'POST'])
def submit():
    try:
        uploadedfile = request.files['filename']
        print(uploadedfile.filename)
        uploadedfile.save("input.png")
        sobel(uploadedfile, "result")
        return render_template('index.html', res=True)
    except:
        return redirect("/")

if __name__ == "__main__":
        app.debug = True
        app.run()