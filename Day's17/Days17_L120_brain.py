class Quiz_brain:

    def __init__(self, q_list):
        self.question_list = q_list
        self.num_questions = 0
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.num_questions]
        self.num_questions += 1
        user_answer = input(f"Q.{self.num_questions}) {current_question.text},True/False: ")
        self.check_answer(user_answer,current_question.answer)

    def is_still_question(self):
        return self.num_questions < len(self.question_list)

    def check_answer(self , u_answer , c_answer):

        if u_answer.lower() == c_answer.lower() :
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!")
            print(f"Current score: {self.score}")




