'''
Created on 12 oct. 2015

@author: Karine
'''
import time

class Question:

    nbr = 0

    #init class
    def __init__(self, question , allResponses, time, response, point = 1): #Attribut d'instance
        self.question = question
        self.allResponses = allResponses
        self.time = time
        self.response = response
        self.point = point
        self.nbr += 1

    #Method to ask a question
    def ask(self, reduction):
        print()
        print("-" * 60)
        print()
        print("Vous avez {} secondes !".format(self.time-reduction)) # Displays the real allotted time left to answer
        print(self.question)

        # Affiche les reponses possible
        for resp in sorted(self.allResponses):
            print(resp + ': '+ self.allResponses[resp])

        #Initailize time less the reduction from the difficulty lvl
        myTime = time.time()-reduction

        #init the variable with the answer of the user
        value = input('Your answer : ')

        #Verification sur la reponse
        for resp in self.allResponses:

            #Verifie si la reponse exist
            if not (value.upper() in self.allResponses.keys()):
                value = input('Error, your answer does not exist ! \nTry again : ')

            #Verifie le temps de reponse
            if time.time()-myTime < self.time:
                if value.upper() == self.response:
                    return (self.point, True, time.time()-myTime)
            else:
                print("Temps ecoulee !")

        return (0, False, time.time()-myTime)


if __name__ == '__main__':


    #Unit test of the class 
    test = Question('??', {"A":"1", "B":"2"}, 10, "B", 1 )

    print(test.ask())
