'''
@author: Karine
'''


class Fichier:

    nbr = 0

    #init class
    def __init__(self, name): #Attribut d'instance
        self.name = name
        self.nbr += 1


    # ecrire dans un fichier
    def ecrireDansFichier(self,texte):
        with open(self.name,"aw") as fichier:
            fichier.writelines(texte+"\n")
            fichier.close()

    # lire un fichier
    def lireFichier(self):
        with open(self.name,"r") as fichier:
            ligne = fichier.read()
            fichier.close()
            return ligne



if __name__ == '__main__':


    fichier = Fichier('test')
    fichier.ecrireDansFichier("\ntest")
    fichier.ecrireDansFichier("blabla")
    fichier.ecrireDansFichier("karine")
    affiche = fichier.lireFichier()
    print affiche