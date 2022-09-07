import dotenv
import os
from flask import Flask, render_template, request, redirect, url_for

dotenv.load_dotenv()

app = Flask(__name__, static_folder='static')

# static files
@app.route('/static/<path:path>')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    # 5000 or the port defined in the .env file
    port = 5000
    if os.environ.get("PORT"):
        port = int(os.environ.get("PORT"))

    app.run(debug=True, port=port)
