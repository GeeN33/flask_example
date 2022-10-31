from flask import Flask, request

# Это уже знакомое callable WSGI-приложение
app = Flask(__name__)

@app.get('/users')
def users_get():
    return 'GET /users'

@app.post('/users')
def users_post():
    return 'Users', 302

@app.route('/')
def hello_world():
    print(request.headers)                # Выводит все заголовки
    return 'Hello, World!'

@app.route('/courses/<course_id>/lessons/<lesson_id>')
def courses(course_id, lesson_id):
    return f'Course id: {course_id}, Lesson id: {lesson_id}'

if __name__ == '__main__':
    app.run(debug=True)


