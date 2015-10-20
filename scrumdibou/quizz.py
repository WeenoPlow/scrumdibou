import correction

class Quizz():

# Initialization of all elements needed
    def __init__(self, questions):
        self.score = 0
        self.track = []
        self.questions = questions

# Display all questions with the 'for' loop
    def start(self):

        # @int goodAnswer
        # @int reduction
        goodAnswer = 0
        reduction = 0

        for question in self.questions:

            #Checks if the user has 5good answers
            if goodAnswer == 5 :

                #Decreases the limit time by 1 more second
                reduction = reduction+1

                # resets the amount of good answers
                goodAnswer = 0

            points, result, time = question.ask(reduction)

            #If the result is good, adds 1 to goodAnswer
            if result == True :
                goodAnswer = goodAnswer+1

            self.score += points
            self.track.append(result)

# Display all questions with the results, "Right" or "Wrong"
    def results(self):
        print()
        print(" Test report ".center(60, "-"))
        print("Your final score : {}".format(self.score))
        for i, good in enumerate(self.track):
            print("Question {}: {}".format(i + 1, "Right" if good else "Wrong"))

# We create a file and note on it the high score
    def save(self):
        with open("highscore.txt", "rw") as score:
            pass

    @staticmethod
    def highscore():
        with open("highscore.txt", "r") as score:
            print(score.read())

# We display the full correction if the user ask it at the end of test
    @staticmethod
    def correction():
        resp = input('Do you want to see the all correction ? (yes/no)')
        if resp.upper() == 'YES':
            print(correction.correction)
