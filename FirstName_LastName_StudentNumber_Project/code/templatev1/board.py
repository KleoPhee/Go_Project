from PyQt5 import QtCore
from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal, QPoint, QRectF, QRect, QEvent
from PyQt5.QtGui import QPainter, QPen, QBrush, QMouseEvent
from piece import Piece
from game_logic import GameLogic

class Board(QFrame):  # base the board on a QFrame widget
	updateTimerSignal = pyqtSignal(int) # signal sent when timer is updated
	clickLocationSignal = pyqtSignal(str) # signal sent when there is a new click location
	newMoveSignal = pyqtSignal(dict) # signal sent when a player played

	timer: QBasicTimer
	isStarted: bool
	boardArray: list

	# TODO set the board width and height to be square
	boardWidth  = 7     # board is 0 squares wide # TODO default and personalized board size
	boardHeight = 7     #
	timerSpeed  = 1     # the timer updates ever 1 second
	counter     = 10    # the number the counter will count down from


	def __init__(self, parent):
		super().__init__(parent)
		self.gameLogic = GameLogic()
		self.initBoard()
		self.gameLogic = GameLogic()
		self.setStyleSheet('background:rgb(200,200,200);padding:7px')

	def initBoard(self):
		"""initiates board"""
		self.timer = QBasicTimer()  # create a timer for the game
		self.isStarted = False      # game is not currently started
		self.start()                # start the game which will start the timer

		self.boardArray = []
		for x in range(0, self.boardHeight):
			self.boardArray.append([])
			for y in range(0, self.boardWidth):
				self.boardArray[x].append(Piece.NoPiece)
		self.boardArray[2][2] = Piece.Black
		self.boardArray[1][2] = Piece.White
		self.printBoardArray()

	def printBoardArray(self):
		"""prints the boardArray in an attractive way"""
		print("boardArray:")
		outline = ""
		for x in range(0, len(self.boardArray)):
			for y in range(0, len(self.boardArray[x])):
				outline += str(self.boardArray[x][y])
			outline += "\n"
		#print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.boardArray]))

	def mousePosToColRow(self, event):
		"""convert the mouse click event to a row and column"""

	def squareWidth(self):
		"""returns the width of one square in the board"""
		return self.contentsRect().width() / self.boardWidth

	def squareHeight(self):
		"""returns the height of one square of the board"""
		return self.contentsRect().height() / self.boardHeight

	def start(self):
		"""starts game"""
		self.isStarted = True                       # set the boolean which determines if the game has started to TRUE
		self.resetGame()                            # reset the game
		self.timer.start(self.timerSpeed, self)     # start the timer with the correct speed
		print("start () - timer is started")

	def timerEvent(self, event):
		"""this event is automatically called when the timer is updated. based on the timerSpeed variable """
		# TODO adapter this code to handle your timers
		if event.timerId() == self.timer.timerId():  # if the timer that has 'ticked' is the one in this class
			if Board.counter == 0:
				print("Game over")
			self.counter -= 1
			#print('timerEvent()', self.counter)
			self.updateTimerSignal.emit(self.counter)
		else:
			super(Board, self).timerEvent(event)      # if we do not handle an event we should pass it to the super
			# class for handelingother wise pass it to the super class for handling

	def paintEvent(self, event):
		"""paints the board and the pieces of the game"""
		painter = QPainter(self)
		self.drawBoardSquares(painter)
		self.drawPieces(painter)

	def mousePressEvent(self, event):
		"""this event is automatically called when the mouse is pressed"""
		tileSize = {"x": self.size().width() / (self.boardWidth + 1),
					"y": self.size().height() / (self.boardHeight + 1)}
		tileClicked = {
			"x": int(event.x() / tileSize["x"] - 0.5),
		  	"y": int(event.y() / tileSize["y"] - 0.5)
		}
		print(tileClicked)
		if tileClicked["x"] in range(0,self.boardWidth) and tileClicked["y"] in range(0,self.boardHeight):
			self.gameLogic.tryPlacePiece(self.boardArray, tileClicked["x"], tileClicked["y"])
			# get moveData from gameLogic
			moveData = {'player':1,'tile':{'x':tileClicked['x'],'y':tileClicked['y']},
						'takenPieces':[
							{'x': tileClicked['x']+1, 'y': tileClicked['y']},
							{'x': tileClicked['x']+1, 'y': tileClicked['y']+1}
						]}
			self.newMoveSignal.emit(moveData)
		self.update()

	def resetGame(self):
		"""clears pieces from the board"""
		# TODO write code to reset game

	def tryMove(self, newX, newY):
		"""tries to move a piece"""

	def drawBoardSquares(self, painter):
		"""
		Draw all the square on the board
		:param QPainter painter: The painter used for this frame
		"""
		tileSize = {"x":self.size().width() / (self.boardWidth+1),"y":self.size().height() / (self.boardHeight+1)}
		painter.setPen(QPen(QBrush(Qt.black), 5, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
		for row in range(0, Board.boardHeight):
			for col in range(0, Board.boardWidth):
				if row in range(1, Board.boardHeight) and col in range(1, Board.boardWidth):
					painter.setPen(QPen(QBrush(Qt.black), 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
					painter.drawRect(QRectF(
						tileSize["x"]*col,tileSize["y"]*row,
						tileSize["x"],
						tileSize["y"])
					)
				if row == (self.boardHeight-1) / 2 and col == (self.boardWidth-1) / 2:
					painter.setBrush(QBrush(Qt.black, Qt.SolidPattern))
					painter.setPen(QPen(QBrush(Qt.black), 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
					center = QPoint(
						tileSize["x"]*col + tileSize["x"],
						tileSize["y"]*row + tileSize["y"]
					)
					painter.drawEllipse(center, tileSize["x"]*0.05, tileSize["y"]*0.05)
					painter.setBrush(QBrush(Qt.transparent, Qt.SolidPattern))

	def drawPieces(self, painter: QPainter):
		"""
		Draw the pieces on the board
		:param QPainter painter: The painter used for this frame
		"""
		tileSize = {"x": self.size().width() / (self.boardWidth+1), "y": self.size().height() / (self.boardHeight+1)}
		radiusX = tileSize["x"] / 2.0
		radiusY = tileSize["y"] / 2.0
		for row in range(0, len(self.boardArray)):
			for col in range(0, len(self.boardArray[0])):
				if self.boardArray[col][row] == Piece.Black:
					painter.setBrush(QBrush(Qt.black, Qt.SolidPattern))
					painter.setPen(QPen(QBrush(Qt.white), 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
				if self.boardArray[col][row] == Piece.White:
					painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))
					painter.setPen(QPen(QBrush(Qt.black), 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
				if self.boardArray[col][row] != Piece.NoPiece:
					center = QPoint(
						tileSize["x"]*col + radiusX + tileSize["x"]/2.0,
						tileSize["y"]*row + radiusY + tileSize["y"]/2.0
					)
					painter.drawEllipse(center, radiusX*0.9, radiusY*0.9)
