from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import requests

question_bank = []
j = requests.get("https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean").json()
print(j)
for q in j['results']:
    question = q['question']
    answer = q['correct_answer']
    question_bank.append(Question(question, answer))

#local dictionary
# for question in question_data:
#     question_bank.append(Question(question['text'], question['answer']))
q = QuizBrain(question_bank)
while q.still_has_questions():
    q.next_question()

num_question = len(q.question_list)
print("You've completed the quiz")
print(f"Final score {num_question}/{q.score}")
