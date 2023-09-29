from mods.request import canvas_get, canvas_post
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

def create_quiz(course_id, qdata):
    data, _ = canvas_post(f'courses/{course_id}/quizzes', qdata)

    return json.loads(data)

def create_quiz_question(course_id, quiz_id, qdata):
    data, _ = canvas_post(f'courses/{course_id}/quizzes/{quiz_id}/questions', qdata)

    return json.loads(data)

def create_quiz_from_file(course_id, filename):

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

    quiz_data = {}

    current_question = None
    qnum = 0

    qlist = []

    # Loop through the file, gathering data

    with open(filename) as fp:
        for line in fp:
            line = line.strip()

            if line == '' or line[0] == '#': continue

            if line[:9] == "QUESTION=":
                preamble = False

            if preamble:
                match split_kv(line):
                    case ["TITLE", x]:
                        quiz_data["title"] = x;
                    case ["DESC", x]:
                        quiz_data["description"] = x
                    case ["SHUFFLE", x]:
                        quiz_data["shuffle_answers"] = "true" if x[0].lower() == "t" else "false"

                # Keep processing preamble
                continue

            # If we get here, we're not in the preamble any longer

            match split_kv(line):
                case ['QUESTION', qname]:
                    if current_question is not None:
                        qlist.append(current_question)

                    qnum += 1
                    anum = 0

                    if qname == '':
                        qname = f"Question {qnum}"

                    current_question = {
                        "question_name": qname,
                        "answers": {}
                    }

                case ['POINTS', qpoints]:
                    current_question["points_possible"] = int(qpoints)
                    pass

                case ['TYPE', qtype]:
                    current_question["question_type"] = typemap[qtype.lower()]
                    pass

                case ['TEXT', qtext]:
                    current_question["question_text"] = qtext
                    pass

                case ['C', atext]:
                    current_question["answers"][str(anum)] = {
                        "answer_text": atext,
                        "answer_weight": 100
                    }
                    anum += 1

                case ['N', atext]:
                    current_question["answers"][str(anum)] = {
                        "answer_text": atext,
                        "answer_weight": 0
                    }
                    anum += 1
                    pass


    # Create the quiz
    print("Creating quiz")
    quiz_res = create_quiz(course_id, { "quiz": quiz_data })
    quiz_id = quiz_res["id"]

    # Create the questions
    for q in qlist:
        print(f"Creating {q['question_name']}")
        print(json.dumps(q, indent=4))
        create_quiz_question(course_id, quiz_id, { "question": q })

