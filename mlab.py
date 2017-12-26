from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = "reportcard"
app.config['MONGO_URI'] = "mongodb://ricardo:ricardomongodb@ds163826.mlab.com:63826/reportcard"

mongo = PyMongo(app)


@app.route("/add")
def example_mongo_db():
    new_grade = mongo.db.grades
    new_grade.insert({'course': 'Xamarin', 'grade': 100})
    return "Added thanks God."


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
