# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from flask_pymongo import PyMongo


#MONGODB_URI = ""

app = Flask(__name__)

mongo = PyMongo(app)

# Main
@app.route("/", methods=["GET"])
def main():
    if request.method == "GET":
        #mongo.db.collection.remove({})
        restrooms = []
        cursor = mongo.db.collection.find()
        for record in cursor:
            restrooms.append(record)
        return render_template("index.html", restrooms=restrooms)


# Restroom add form
@app.route("/add", methods=["GET", "POST"])
def add_restroom():
    if request.method == "GET":
        restroom = {}
        return render_template("form.html", r=restroom)
    if request.method == "POST":
        restroom = {}
        restroom["place"] = request.form["place"]
        restroom["description"] = request.form["description"]
        # Calculate latitude and longitude with given direction
        restroom["lat"] = request.form["lat"]
        restroom["lng"] = request.form["lng"]
        mongo.db.collection.insert(restroom)
        return render_template("form.html", r=restroom)


if __name__ == "__main__":
    app.run()