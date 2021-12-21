# this code is running logic changed from video
import datetime
from logging import debug
from flask import Flask, render_template, request
from pymongo import MongoClient
from werkzeug.utils import redirect


def create_app():
    app = Flask(__name__)
    client = MongoClient(
        "mongodb+srv://blog_project:blog123@cluster0.hfxzv.mongodb.net/test")
    app.db = client.microblog

    @app.route("/", methods=["GET", "POST"])
    def home():
        if request.method == "POST":
            entry_content = request.form.get("content")
            formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
            data = {"content": entry_content, "date": formatted_date}
            app.db.entries.insert_one(data)

            a = []
            for entry in app.db.entries.find({}):
                a.append(entry)
            return render_template('home.html', entries=a)

        else:
            a = []
            for entry in app.db.entries.find({}):
                a.append(entry)

            print(a)
            return render_template("home.html", entries=a)

    return app
