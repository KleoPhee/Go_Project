import os

from FirstName_LastName_StudentNumber_Project.code.templatev1.piece import Piece

class GameLogic:
	print("Game Logic Object Created")
	colorTurn = Piece.Black
	nbTurn = 0
	listHistoric = []
	passCounts = 0

	def tryPlacePiece(self, gameBoard, x, y):
		listTurn = []
		if self.checkLiberties(gameBoard, x, y) is True:
			self.passCounts = 0
			opponentPiece = Piece.Black if self.colorTurn is Piece.White else Piece.White
			gameBoard[x][y] = self.colorTurn
			self.nbTurn = self.nbTurn + 1
			self.writeInFile(self.nbTurn, gameBoard, self.colorTurn)

			# remove taken pieces
			for i in range(-1, 2, 2):
				traceback = []
				if x + i in range(0, len(gameBoard)) and gameBoard[x+i][y] == opponentPiece and self.takePieces(gameBoard, x + i, y, traceback, opponentPiece):
					for toRemove in traceback:
						listTurn.append(toRemove)
						gameBoard[toRemove['x']][toRemove['y']] = Piece.NoPiece
				traceback = []
				if y + i in range(0, len(gameBoard)) and gameBoard[x][y+i] == opponentPiece and self.takePieces(gameBoard, x, y + i, traceback, opponentPiece):
					for toRemove in traceback:
						listTurn.append(toRemove)
						gameBoard[toRemove['x']][toRemove['y']] = Piece.NoPiece

			historicEntry = {'player':self.colorTurn, 'tile':{'x':x, 'y':y},'takenPieces':listTurn}
			self.colorTurn = Piece.Black if self.colorTurn is Piece.White else Piece.White
			return historicEntry
		return None

		#print content of gameboard inside file of folder name numero state + colorTurn at the begining

	def takePieces(self, gameBoard, x, y, traceback, opponentPiece):
		if gameBoard[x][y] == Piece.NoPiece:
			return False
		if gameBoard[x][y] == self.colorTurn:
			return True
		traceback.append({'x': x, 'y': y})
		for i in range(-1, 2, 2):
			if x + i in range(0, len(gameBoard)) and {'x': x + i, 'y': y} not in traceback:
				if not self.takePieces(gameBoard, x + i, y, traceback, opponentPiece):
					return False
			if y + i in range(0, len(gameBoard[0])) and {'x': x, 'y': y + i} not in traceback:
				if not self.takePieces(gameBoard, x, y + i, traceback, opponentPiece):
					return False
		return True

	def passTurn(self):
		self.passCounts += 1
		historicEntry = {'player':self.colorTurn,'passed':self.passCounts}
		self.colorTurn = Piece.Black if self.colorTurn is Piece.White else Piece.White
		return historicEntry, self.passCounts == 2

	def writeInFile(self, nb, gameBoard, colorTurn):
		f = open("state"+str(nb)+".txt", 'w+')
		f.write("Color turn:" + str(colorTurn) + "\nBoard:\n" + '\n'.join(['\t'.join([str(cell) for cell in row]) for row in gameBoard]))
		f.close()

	# TODO 1. Suicide Rule: You cannot place a stone which will immediately have no liberties.
	def checkLiberties(self, gameBoard, x, y):
		if gameBoard[x][y] != Piece.NoPiece:
			return False
		else:
			if x - 1 >= 0 and gameBoard[x - 1][y] == Piece.NoPiece:
				return True
			if x + 1 < len(gameBoard) and gameBoard[x + 1][y] == Piece.NoPiece:
				return True
			if y + 1 < len(gameBoard) and gameBoard[x][y+1] == Piece.NoPiece:
				return True
			if y - 1 >= 0 and gameBoard[x][y-1] == Piece.NoPiece:
				return True
		return False

	# TODO 2. KO Rule (Eternity Rule):
	def KoRule(self):
		return

# count the number of black and white tiles

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

	# Previous game states are not allowed. Keep a list of previous game states which must be
	# checked before stones are placed
	# techniquement peu pas les enlever préciser dans le help considerer comme aditionelle 10 marks
	# TODO placer une piece a cote d'une autre peut être cocher

	# TODO awarding points stones captured and territory controlled by a colour
	# TODO A stone can be placed at any unoccupied and intersection of the board with limited exceptions

	folder = "./" # keep a file can read and match with the current file
	count = {}


	print(count)
