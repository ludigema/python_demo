from acheteur import Acheteur
from objet import Objet

def createAcheteurs(nb):
	acheteurs = []
	for i in range(nb):
		nom = input("Entrer le nom de l'acheteur", i)
		acheteurs.append(Achteur(nom))
	return acheteurs

def saisieOffre(acheteurs):
	for a in acheteurs:
		a.offre = int(input("Achteur", a.name, "entrer votre offrek"))

def tour(n, acheteurs):
	for i in range(n):
		print("*** \t Tour", i+1, "\t ***")
		saisieOffre(acheteurs)

def main():
	name-objet = input("Enter l'objet")
	prix-objet = input("Enter le prix de l'objet")
	enchere = Objet(name-objet, prix-objet)
	
	nb-acheteurs = int(input("Combien d'achteurs ?"))
	acheteurs = createAcheteurs(nb-acheteurs)
	tours_achat(3, acheteurs)

if __name__ == '__main__':
	main()