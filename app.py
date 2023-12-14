from flask import Flask, render_template, request, redirect
from image import display

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == 'GET':
        return render_template("index.html")

    if request.method == 'POST':
        display(request.files['file'])
        return redirect(request.referrer)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
