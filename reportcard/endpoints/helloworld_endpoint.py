from reportcard import reportcard_app

@reportcard_app.route('/')
def hello_world():
    return 'Hello from Flask! This is a test'