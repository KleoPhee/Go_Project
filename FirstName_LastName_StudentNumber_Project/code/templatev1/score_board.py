from PyQt5.QtWidgets import QDockWidget, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import pyqtSlot

from FirstName_LastName_StudentNumber_Project.code.templatev1.piece import Piece


class ScoreBoard(QDockWidget):
	'''# base the score_board on a QDockWidget'''

	takenPieces: list

	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		'''initiates ScoreBoard UI'''
		self.resize(200, 200)
		self.center()
		self.setWindowTitle('ScoreBoard')
		self.mainWidget = QWidget()
		self.mainLayout = QVBoxLayout()
		self.takenPieces = [0, 0]

		self.label_playerTurn = QLabel("Player 1 (black)")
		self.label_takenPieces = QLabel("Player 1 (black) taken pieces: 0\nPlayer 2 (white) taken pieces: 0")
		self.mainWidget.setLayout(self.mainLayout)
		self.mainLayout.addWidget(self.label_playerTurn)
		self.mainLayout.addWidget(self.label_takenPieces)
		self.setWidget(self.mainWidget)


	def center(self):
		'''centers the window on the screen, you do not need to implement this method'''

	def make_connection(self, board):
		'''this handles a signal sent from the board class'''
		# update the number of taken pieces by players
		board.newMoveSignal.connect(self.updateTakenPieces)
		# update player turn
		board.newMoveSignal.connect(self.updatePlayerTurn)

	@pyqtSlot(dict)
	def updateTakenPieces(self, board):
		"""function to signal of a taken piece and update data"""
		if "takenPieces" in board:
			self.takenPieces[0 if board['player'] is Piece.Black else 1] += len(board['takenPieces'])
		self.label_takenPieces.setText("Player 1 taken pieces: " + str(self.takenPieces[0]) + "\n" + "Player 2 taken pieces: " + str(self.takenPieces[1]))

	@pyqtSlot(dict)
	def updatePlayerTurn(self, board):
		"""function to signal change in player"""
		if board['player'] is Piece.Black:
			self.label_playerTurn.setText("Player 2 (white)")
		if board['player'] is Piece.White:
			self.label_playerTurn.setText("Player 1 (black)")

	@pyqtSlot(str)
	def setClickLocation(self, clickLoc):
		'''updates the label to show the click location'''
		self.label_clickLocation.setText("Click Location:" + clickLoc)

	@pyqtSlot(int)
	def setTimeRemaining(self, timeRemainng):
		'''updates the time remaining label to show the time remaining'''
		update = "Time Remaining:" + str(timeRemainng)
		self.label_timeRemaining.setText(update)