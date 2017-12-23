from flask import request, abort, jsonify
from reportcard import reportcard_app, db
from time import gmtime, strftime

from ..models.grades import Grade

vector = []


@reportcard_app.route('/grades', methods=['POST'])
def post_grades():
    course = request.json.get('course')
    grade = request.json.get('grade')
    date = strftime("%a, %d %b %Y %H:%M", gmtime())
    if course is None or grade is None:
        abort(400)  # Missing course or grade
    new_grade = Grade(course, grade, str(date))
    db.create_all()
    db.session.add(new_grade)
    db.session.commit()
    return jsonify({'course': new_grade.course, 'grade': new_grade.grade, 'date': new_grade.date}), 201



@reportcard_app.route('/grades', methods=['GET'])
def get_grades():
    global vector
    grades = Grade.query.all()
    for grade in grades:
        element = {'course': grade.course, 'grade': grade.grade, 'date': grade.date}
        vector.append(element)
    return jsonify(vector)
