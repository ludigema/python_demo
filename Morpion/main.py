from Plateau import Plateau

plateau = Plateau()
joueur  = 'X'
while not plateau.grillePleine():
	plateau.joue(joueur)
	if plateau.winner():
		print(joueur,"a gagne")
		break
	if joueur == 'X':
		joueur = '0'
	else:
		joueur = 'X'
else:
	print("pas de vainqueur	")