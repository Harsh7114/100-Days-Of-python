class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.score =0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        user_ans= input(f"Q {self.question_number}: {current_question.text} (true or false :")
        self.check_answer(user_ans,current_question.answer)
    def check_answer(self, user_answer , correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score +=1
            print("You got it right")
        else:
            print("Nahh it;s wrong ")
        print(f" to correct ans was :{correct_answer}")
        print(f"Yout current socre is :{self.score} / {self.question_number} ")
        print("\n")
