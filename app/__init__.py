from flask import Flask, render_template
from edgedetection import *

app = Flask(__name__)

@app.route("/")
def image():
    sobel("./static/flower.png", "edges")
    gaussianBlur("./static/flower.png")
    sobel("./static/blur.png", "edges2")
    return render_template('index.html')
    
if __name__ == "__main__":
        app.debug = True
        app.run()