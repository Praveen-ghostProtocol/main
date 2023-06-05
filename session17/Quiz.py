 
import Question
import Answer

class Quiz:
    questionlist = []
    answerlist = []
    def __init__(self):
        self.answerlist.append(Answer.Answer("Delhi",True))
        self.answerlist.append(Answer.Answer("Mumbai"))
        self.answerlist.append(Answer.Answer("Chennai"))
        self.answerlist.append(Answer.Answer("Kolkata"))
        self.questionlist.append(Question.Question("What is the capital of India?",self.answerlist))
        

 