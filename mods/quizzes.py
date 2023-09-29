from mods.request import canvas_get
import json
import re

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

def create_quiz(filename):

    def split_kv(s):
        try:
            k, v = s.split('=', 1)
            return k.strip(), v.strip()

        except ValueError:
            return None, None

    typemap = {
        "mc": "multiple_choice_question",
        "tf": "true_false_question",
        "e": "essay_question",
        "sa": "short_answer_question",
        "ma": "multiple_answers_question",
    }

    preamble = True
    title = ""
    description = ""
    shuffle = True

    current_question = None
    qnum = 0

    qlist = []

    # Loop through the file, gathering data

    with open(filename) as fp:
        for line in fp:
            line = line.strip()

            if line == '' or line[0] == '#': continue

            print(line)

            if line[:9] == "QUESTION=":
                preamble = False

            if preamble:
                match split_kv(line):
                    case ["TITLE", x]:
                        title = x
                    case ["DESC", x]:
                        desc = x
                    case ["SHUFFLE", x]:
                        shuffle = x[0].lower() == "t"

                # Keep processing preamble
                continue

            # If we get here, we're not in the preamble any longer

            match split_kv(line):
                case ['QUESTION', qname]:
                    if current_question is not None:
                        qlist.append(current_question)

                    qnum += 1

                    if qname == '':
                        qname = f"Question {qnum}"

                    current_question = {
                        "question_name": qname,
                        "answers": []
                    }

                case ['POINTS', qpoints]:
                    current_question["points_possible"] = int(qpoints)

                case ['TYPE', qtype]:
                    current_question["question_type"] = typemap[qtype.lower()]

                case ['TEXT', qtext]:
                    current_question["question_text"] = qtext

                case ['C', atext]:
                    current_question["answers"].append({
                        "answer_text": atext,
                        "answer_weight": 100
                    })

                case ['N', atext]:
                    current_question["answers"].append({
                        "answer_text": atext,
                        "answer_weight": 0
                    })

    # Create the quiz
    print(qlist)
    print(json.dumps(qlist, indent=4))

    # Create the questions

