import os
from mods.dotenv import load_dotenv
import mods.courses as courses
import mods.modules as modules

load_dotenv()

print(f'Token: {os.environ["CANVAS_API_ACCESS_TOKEN"]}')

course_list = courses.get_courses()

networks = courses.get_course_by_name(course_list, "INTRO TO COMPUTER NETWORKS (CS_372_501_F2023)")

print(networks)

m = modules.add_module(networks["id"], "Test Module, Ignore")

print(m)

