import os

from FirstName_LastName_StudentNumber_Project.code.templatev1.piece import Piece

class GameLogic:
	print("Game Logic Object Created")

	def tryPlacePiece(self, gameBoard, x, y):
		gameBoard[x][y] = Piece.Black

	def parseFile(file, count):
		with open(file) as f:
			lines = f.readlines()
			for line in lines:
				for word in line.split():
					if word not in count.keys():
						count[word] = {}
					if file not in count[word]:
						count[word][file] = 1
					else:
						count[word][file] += 1

	def parseFolder(folder):
		count = {}
		for file in os.listdir(folder):
			folder.parseFile(file, count)

	# TODO sois fct avec le switch sois dans boucle principale
	# TODO add code here to manage the logic of your game

	# TODO vérifier les regle selectionner et adapter le jeu
	# movement black first white second
	# TODO 1. Suicide Rule: You cannot place a stone which will immediately have no liberties.
	# TODO 2. KO Rule (Eternity Rule):
	# Previous game states are not allowed. Keep a list of previous game states which must be
	# checked before stones are placed
	# techniquement peu pas les enlever préciser dans le help considerer comme aditionelle 10 marks
	# TODO placer une piece a cote d'une autre peut être cocher

	# TODO awarding points stones captured and territory controlled by a colour
	# TODO A stone can be placed at any unoccupied and intersection of the board with limited exceptions

	folder = "./" # keep a file can read and match with the current file
	count = {}


	print(count)
