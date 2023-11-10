from acheteur import Acheteur
from objet import Objet

# Le prix gagnant est le prix de l'offre la plus élevée d'un acheteur 
# non gagnant au-dessus du prix de réserve 
# (ou le prix de réserve s'il n'y en a aucun qui s'applique)

def winner(enchere, acheteurs):

def createAcheteurs(nb):
	acheteurs = []
	for i in range(nb):
		nom = input("Entrer le nom de l'acheteur", i)
		acheteurs.append(Achteur(nom))
	return acheteurs

def saisieOffre(acheteurs):
	for a in acheteurs:
		a.offre.append(int(input("Acheteur", a.name, "entrer votre offre")))

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