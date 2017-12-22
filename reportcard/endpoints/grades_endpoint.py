from flask import Flask, request, abort, jsonify
from reportcard import reportcard_app, db
from ..models.grades import Grade


@reportcard_app.route('/grades', methods=['POST', 'GET'])
def grades():
    if request.method == "POST":
        course = request.json.get('course')
        grade = request.json.get('grade')
        if course is None or grade is None:
            abort(400)  # Missing course or grade
        new_grade = Grade(course, grade)
        db.session.add(new_grade)
        db.session.commit()
        return jsonify({'course': new_grade.course, 'grade': new_grade.grade}), 201
