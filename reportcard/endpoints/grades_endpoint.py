from reportcard import reportcard_app

vector_grades = {'nombre': 'Ricardo', 'course': 'Web Services', 'grade': 100}

@reportcard_app.route('/grades')
def get_grades():
    global vector_grades
    return "<h1>Nombre: %s</h1>" % vector_grades['nombre']