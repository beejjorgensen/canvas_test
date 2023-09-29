from mods.request import canvas_get
import json

def get_courses():
    data, _ = canvas_get('courses')

    return json.loads(data)

def get_course_by_name(courses, name):
    for c in courses:
        if c["name"] == name:
            return c

    return None
    
