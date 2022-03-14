
class Question:


    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer

class Quiz:

    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f"question {self.questionIndex + 1}: {question.text}")

        for q in question.choices:
            print("-" + q )

        answer = input("answer: ")
        self.guess(answer)
        self.loadQuestion()
    
    def guess(self,answer):
        question = self.getQuestion()
        
        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()
    def showScore(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print("quiz is over")
            print("score: ", self.score)
    

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1
        print(f"{questionNumber}/{totalQuestion}")

q1 = Question("capital of turkey: ",["istanbul","ankara","izmir","çorum"],"ankara")
q2 = Question("greatest two-digit even number: ",["98","96","99","97"], "98")
q3 = Question("the most crowded city of turkey: ",["ankara", "izmir","istanbul","adana"],"istanbul")
q4 = Question("23+67: ",["90","100","89","99"],"90")
questionList = [q1,q2,q3,q4]

quiz = Quiz(questionList)
quiz.loadQuestion()

