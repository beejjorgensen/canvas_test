from mods.request import canvas_put
import json

def update_page(course_id, page_id, title, body, editing_roles="teachers"):
    data, _ = canvas_put(f'courses/{course_id}/pages/{page_id}', {
        "wiki_page[title]": title,
        "wiki_page[body]": body,
        "wiki_page[editing_roles]": editing_roles,
    })

    return json.loads(data)

