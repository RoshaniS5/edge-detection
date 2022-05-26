from flask import Flask, render_template
import sobel

app = Flask(__name__)

@app.route("/")
def image():
    return render_template('index.html')
if __name__ == "__main__":
        app.run()