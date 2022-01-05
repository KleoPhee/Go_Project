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
		#create a widget to hold other widgets
		self.mainWidget = QWidget()
		self.mainLayout = QVBoxLayout()
		self.takenPieces = [0, 0]

		#create two labels which will be updated by signals
		#self.label_clickLocation = QLabel("Click Location: ")
		self.label_timeRemaining = QLabel("Time remaining: ")
		self.label_playerTurn = QLabel("Player 1 (black)")
		self.label_takenPieces = QLabel("Player 1 (black) taken pieces: 0\nPlayer 2 (white) taken pieces: 0")
		self.mainWidget.setLayout(self.mainLayout)
		#self.mainLayout.addWidget(self.label_clickLocation)
		#self.mainLayout.addWidget(self.label_timeRemaining)
		self.mainLayout.addWidget(self.label_playerTurn)
		self.mainLayout.addWidget(self.label_takenPieces)
		self.setWidget(self.mainWidget)


	def center(self):
		'''centers the window on the screen, you do not need to implement this method'''

	def make_connection(self, board):
		'''this handles a signal sent from the board class'''
		# when the clickLocationSignal is emitted in board the setClickLocation slot receives it
		board.clickLocationSignal.connect(self.setClickLocation)
		# when the updateTimerSignal is emitted in the board the setTimeRemaining slot receives it
		board.updateTimerSignal.connect(self.setTimeRemaining)
		# update the number of taken pieces by players
		board.newMoveSignal.connect(self.updateTakenPieces)
		# update player turn
		board.newMoveSignal.connect(self.updatePlayerTurn)

	@pyqtSlot(dict)
	def updateTakenPieces(self, board):
		if "takenPieces" in board:
			self.takenPieces[0 if board['player'] is Piece.Black else 1] += len(board['takenPieces'])
		self.label_takenPieces.setText("Player 1 taken pieces: " + str(self.takenPieces[0]) + "\n" + "Player 2 taken pieces: " + str(self.takenPieces[1]))

	@pyqtSlot(dict)
	def updatePlayerTurn(self, board):
		if board['player'] is Piece.Black:
			self.label_playerTurn.setText("Player 2 (white)")
		if board['player'] is Piece.White:
			self.label_playerTurn.setText("Player 1 (black)")

	@pyqtSlot(str) # checks to make sure that the following slot is receiving an argument of the type 'int'
	def setClickLocation(self, clickLoc):
		'''updates the label to show the click location'''
		self.label_clickLocation.setText("Click Location:" + clickLoc)
		#print('slot ' + clickLoc)

	@pyqtSlot(int)
	def setTimeRemaining(self, timeRemainng):
		'''updates the time remaining label to show the time remaining'''
		update = "Time Remaining:" + str(timeRemainng)
		self.label_timeRemaining.setText(update)
		#print('slot '+update)
		# self.redraw()