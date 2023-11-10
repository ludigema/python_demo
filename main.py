from acheteur import Acheteur
from objet import Objet

# Le prix gagnant est le prix de l'offre la plus élevée d'un acheteur 
# non gagnant au-dessus du prix de réserve 
# (ou le prix de réserve s'il n'y en a aucun qui s'applique)
def winner(nb, enchere, acheteurs):
	win  = None
	for i in range(nb):
		for a in acheteurs :
			if a.offre[i] > enchere.prixEnchere:
				enchere.prixEnchere = a.offre[i]
			if a.offre[i] > enchere.prixEnchere  and win == None or win.name != a.name:
				win = a
				
def createAcheteurs(nb):
	acheteurs = []
	for i in range(nb):
		nom = input("Entrer le nom de l'acheteur " + str(i+1))
		acheteurs.append(Acheteur(nom))
	return acheteurs

def saisieOffre(acheteurs):
	for a in acheteurs:
		a.offre.append(int(input("Acheteur" + a.name + "entrer votre offre")))

def tours_achat(n, acheteurs):
	for i in range(n):
		print("*** \t Tour", i+1, "\t ***")
		saisieOffre(acheteurs)

def main():
	nameObjet = input("Enter l'objet")
	prixObjet = input("Enter le prix de l'objet")
	#enchere = Objet(name-objet, prix-objet)

	nbAcheteurs = int(input("Combien d'achteurs ?"))
	acheteurs = createAcheteurs(nbAcheteurs)

	nbTours = 3
	tours_achat(nbTours , acheteurs)

	winner(nbTours, Objet(nameObjet, prixObjet), acheteurs)

if __name__ == '__main__':
	main()