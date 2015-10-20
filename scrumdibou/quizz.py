import correction

class Quizz():

    def __init__(self, questions):
        self.score = 0
        self.track = []
        self.questions = questions

    def start(self):
        for question in self.questions:
            points, result, time = question.ask()
            self.score += points
            self.track.append(result)

    def results(self):
        print()
        print(" Test report ".center(60, "-"))
        print("Your final score : {}".format(self.score))
        for i, good in enumerate(self.track):
            print("Question {}: {}".format(i + 1, "Right" if good else "Wrong"))

    def save(self):
        with open("highscore.txt", "rw") as score:
            pass

    @staticmethod
    def highscore():
        with open("highscore.txt", "r") as score:
            print(score.read())

    @staticmethod
    def correction():
        resp = input('Do you want to see the all correction ? (yes/no)')
        if resp.upper() == 'YES':
            print(correction.correction)
