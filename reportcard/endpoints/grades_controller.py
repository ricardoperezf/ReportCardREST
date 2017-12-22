import datetime
from flask import request, abort, jsonify
from reportcard import reportcard_app, db
from sqlalchemy import create_engine
from sqlalchemy.log import echo_property
from sqlalchemy.orm import sessionmaker

from ..models.grades import Grade

vector = []


@reportcard_app.route('/grades', methods=['POST', 'GET'])
def the_grades():
    if request.method == "POST":
        course = request.json.get('course')
        grade = request.json.get('grade')
        date = datetime.datetime.now()
        if course is None or grade is None:
            abort(400)  # Missing course or grade
        new_grade = Grade(course, grade, str(date))
        db.session.add(new_grade)
        db.session.commit()
        return jsonify({'course': new_grade.course, 'grade': new_grade.grade, 'date': new_grade.date}), 201
    else:
        global vector
        grades = Grade.query.all()
        for grade in grades:
            element = {'course': grade.course, 'grade': grade.grade, 'date': grade.date}
            vector.append(element)
        return jsonify(vector)
