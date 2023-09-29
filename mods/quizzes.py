from mods.request import canvas_get
import json

def get_quizzes(course_id):
    data, _ = canvas_get(f'courses/{course_id}/quizzes')

    return json.loads(data)

def get_quiz_by_title(quizzes, title):
    for c in quizzes:
        if c["title"] == title:
            return c

    return None

def get_quiz_questions(course_id, quiz_id):
    data, _ = canvas_get(f'courses/{course_id}/quizzes/{quiz_id}/questions')

    return json.loads(data)

