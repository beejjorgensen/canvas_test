import os
from modules.dotenv import load_dotenv
import modules.courses as courses

load_dotenv()

print(f'Token: {os.environ["CANVAS_API_ACCESS_TOKEN"]}')

course_list = courses.get_courses()

networks = courses.get_course_by_name(course_list, "INTRO TO COMPUTER NETWORKS (CS_372_501_F2023)")

print(networks)
