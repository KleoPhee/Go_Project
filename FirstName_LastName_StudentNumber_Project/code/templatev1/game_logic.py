import os

from FirstName_LastName_StudentNumber_Project.code.templatev1.piece import Piece


def tryPlacePiece(gameBoard,x,y):
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
		parseFile(file, count)

class GameLogic:
	print("Game Logic Object Created")
	# TODO add code here to manage the logic of your game

	folder = "./"
	count = {}


	print(count)
