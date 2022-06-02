from flask import Flask, flash, request, redirect, url_for, render_template
import sobel


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def image():
    return render_template("index.html")
if __name__ == "__main__":
    app.run()
