class Plateau:
	""" Plateau 3x3 pour le jeu du Morpion """

	def __init__(self,x=3, y=3):
		self.__x = x
		self.__y = y
		self.__grille = [[" " for j in range(self.__y)] for i in range(self.__x)]

	def affiche(self):
		for i in range(self.__x):
			str1 = "|"
			for j in range(self.__y):
				str1 += self.__grille[i][j] + "|"
			print(str1)

	def joue(self, joueur):
		x = -1
		y = -1
		triche = True
		while triche:
			print("Entrer un entier entre 0 et 2 pour x")
			x = int(input())
			print("Entrer un entier entre 0 et 2 pour y")
			y = int(input())
			if ((x > 2 or x < 0) or (y > 2 or y < 0)):
				triche = True
			# par convention, une case vide est un espace
			elif self.__grille[x][y] != " ":
				triche = True
			else:
				triche = False
		self.__grille[x][y] = joueur
		self.affiche()	

	def grillePleine(self):
		for i in range(self.__x):
			for j in range(self.__y):
				if self.__grille[i][j] == " ":
					return False
		return True

	def winner(self):
		# ligne
		for i in range(3):
			if self.__grille[i][0] == self.__grille[i][1] and self.__grille[i][0] == self.__grille[i][2] and self.__grille[i][0] != " ":
				return True
		# colonne
		for i in range(3):
			if self.__grille[0][i] == self.__grille[1][i] and self.__grille[0][i] == self.__grille[2][i] and self.__grille[0][i] != " ":
				return True
		# diagonale
		if self.__grille[0][0] == self.__grille[1][1] and self.__grille[0][0] == self.__grille[2][2] and self.__grille[0][0] != " ":
			return True
		if self.__grille[0][2] == self.__grille[1][1] and self.__grille[0][2] == self.__grille[2][0] and self.__grille[0][2] != " ":
			return True
		return False