from modules.request import canvas_post
import json

def add_module(course_id, name, position=9999):
    data, _ = canvas_post(f'courses/{course_id}/modules', {
        "name": name
    })

    return json.loads(data)

