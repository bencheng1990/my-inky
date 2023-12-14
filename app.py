from flask import Flask, render_template, request, redirect
from image import display
import time

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "./uploads"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        return render_template("index.html")

    if request.method == 'POST':
        display(request.files['file'])
        # time.sleep(1)
        return redirect(request.referrer)


if __name__ == "__main__":
    app.run(debug=True)
