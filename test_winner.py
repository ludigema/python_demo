from acheteur import Acheteur
from objet import Objet
from main import winner

def testWin():
	nb = 3
	enchere = Objet("truc", 100)
	acheteurs = []
	acheteurs.append(Acheteur('A'))
	acheteurs[0].offre = [110,0,130]
	acheteurs.append(Acheteur('B'))
	acheteurs[1].offre = [0,0,0]
	acheteurs.append(Acheteur('C'))
	acheteurs[2].offre = [0,125,0]
	acheteurs.append(Acheteur('D'))
	acheteurs[3].offre = [105,115,90]
	acheteurs.append(Acheteur('E'))
	acheteurs[4].offre = [132,135,140]
	assert winner(nb, enchere, acheteurs) == 'E'
