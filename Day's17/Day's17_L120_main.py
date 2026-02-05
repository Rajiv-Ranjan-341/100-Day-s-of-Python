from Days17_L120_class import Question
from Days17_L120_data import questions_data
from Days17_L120_brain import Quiz_brain

question_bank = []
for question in questions_data:
    question_text = question["question"]
    answer = question["correct_answer"]
    new_question = Question(question_text, answer)
    question_bank.append(new_question)


quiz = Quiz_brain(question_bank)

while quiz.is_still_question():
    quiz.next_question()
