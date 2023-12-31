import os
from mods.dotenv import load_dotenv
import mods.courses as courses
import mods.modules as modules
import mods.pages as pages

load_dotenv()

print(f'Token: {os.environ["CANVAS_API_ACCESS_TOKEN"]}')

course_list = courses.get_courses()

networks = courses.get_course_by_name(course_list, "INTRO TO COMPUTER NETWORKS (CS_372_501_F2023)")

print(networks)

#m = modules.add_module(networks["id"], "Test Module, Ignore")

#print(m)

#p = pages.update_page(networks["id"], "test-page-id", "Test Page Title", "<h1>Test Page Body</h1>This is <i>the</i> page body.")
p = pages.update_page(networks["id"], "", "Test Page Title", "<h1>Test Page Body</h1>This is <i>the</i> page body.")

print(p)
