"""MODULE: Afficher et comparer le highscore de l'utilisateur connecté"""

class scoring():
    def __init__(self, name, note):
        self.name = name
        self.note = str(note)

    """Fonction afficher"""
    def afficher(self):
        with open ("annexes/highscore.txt", 'r') as f:
            data = f.read()
        return data

    """Fonction pour comparer la note et le dernier highscore"""
    def bestScore(self):
        best = self.afficher()
        if int(best) < int(self.note):
            with open ("annexes/highscore.txt", 'w') as f:
                f.write(self.note)
        else:
            print ("Vous n'avez pas battu votre meilleur score")
        print("Votre meilleur score est: %s" %self.afficher())

"""MAIN DE TEST"""
if __name__ == '__main__':
    sc = scoring("rezr", 3)
    sc.bestScore()
    sc2 = scoring("haha", 30)
    print (sc2.afficher())
    sc2.bestScore()
    print (sc2.afficher())
