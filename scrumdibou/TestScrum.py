'''
Created on 12 oct. 2015

@author: Karine
'''
import time

class Question:

    nbr = 0

    def __init__(self, question , allResponses, time, response, point = 1): #Attribut d'instance
        self.question = question
        self.allResponses = allResponses
        self.time = time
        self.response = response
        self.point = point
        self.nbr += 1

    def ask(self):
        print()
        print("-" * 60)
        print()
        print("Vous avez {} secondes !".format(self.time))
        print(self.question)
        for resp in sorted(self.allResponses):
            print(resp + ': '+ self.allResponses[resp])
        myTime = time.time()
        value = input('Your answer : ')

        for resp in self.allResponses:

            if not (value.upper() in self.allResponses.keys()):
                value = input('Error, your answer does not exist ! \nTry again : ')

            if time.time()-myTime < self.time:
                if value.upper() == self.response:
                    return (self.point, True, time.time()-myTime)
            else:
                print("Temps ecoulee !")

        return (0, False, time.time()-myTime)


if __name__ == '__main__':

    test = Question('??', {"A":"1", "B":"2"}, 10, "B", 1 )

    print(test.ask())
