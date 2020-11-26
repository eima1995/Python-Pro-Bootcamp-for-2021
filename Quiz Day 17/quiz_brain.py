class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer = input(f"Q.{self.question_number + 1}:" + current_question.text + "(True/False)?:")
        self.question_number += 1
        self.check_answer(answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, input_answer):
        if input_answer.lower() == self.question_list[self.question_number - 1].answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        num_questions = len(self.question_list)
        print(f"Your current score is: {num_questions}/{self.score}")
        print("\n")