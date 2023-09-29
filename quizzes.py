import os
import json
from mods.dotenv import load_dotenv
import mods.courses as courses
import mods.modules as modules
import mods.pages as pages
import mods.quizzes as quizzes

load_dotenv()

print(f'Token: {os.environ["CANVAS_API_ACCESS_TOKEN"]}')

course_list = courses.get_courses()

networks = courses.get_course_by_name(course_list, "INTRO TO COMPUTER NETWORKS (CS_372_501_F2023)")

nid = networks["id"]

#print(nid)

qzs = quizzes.get_quizzes(nid)

#print(json.dumps(qzs, indent=4))

syl_quiz = quizzes.get_quiz_by_title(qzs, "Test Quiz")

print(json.dumps(syl_quiz, indent=4))

syl_quiz_id = syl_quiz["id"]

qs = quizzes.get_quiz_questions(nid, syl_quiz_id)

print(json.dumps(qs, indent=4))
