from PyQt5.QtCore import pyqtSlot, Qt, pyqtSignal
from PyQt5.QtWidgets import QDockWidget, QWidget, QVBoxLayout, QCheckBox, QComboBox, QLabel, QHBoxLayout, QPushButton
from board import Board

class SettingsWidget(QDockWidget):
	passTurnSignal = pyqtSignal()
	resetGameSignal = pyqtSignal()

	def __init__(self):
		"""
		Initiates a new Settings Widget
		"""
		super().__init__()
		self.resize(200, 200)
		self.setWindowTitle('Settings')
		mainWidget = QWidget()
		mainLayout = QVBoxLayout()

		KORuleToggle = QCheckBox("KO Rule")

		displayPossibilitiesToggle = QCheckBox("Display move possibilities")

		boardSizeControllerWidget = self.initBoardSizeController()
		mainLayout.addWidget(boardSizeControllerWidget)
		mainLayout.addWidget(KORuleToggle)
		mainLayout.addWidget(displayPossibilitiesToggle)

		passTurnButton = QPushButton('Pass turn')
		passTurnButton.clicked.connect(lambda: self.passTurnSignal.emit())
		mainLayout.addWidget(passTurnButton)

		resetGameButton = QPushButton('Reset Game')
		resetGameButton.clicked.connect(lambda: self.resetGameSignal.emit())
		mainLayout.addWidget(resetGameButton)

		mainLayout.setAlignment(Qt.AlignTop)
		mainWidget.setLayout(mainLayout)
		self.setWidget(mainWidget)

	def initBoardSizeController(self):
		"""function to control board size"""
		boardSizeControllerWidget = QWidget()
		boardSizeLayout = QHBoxLayout()
		boardSizeLabel = QLabel("Board size: ")

		boardSizeController = QComboBox()
		boardSizeController.addItem("7x7")
		boardSizeController.addItem("13x13")
		boardSizeController.addItem("19x19")
		boardSizeController.addItem("Custom")

		boardSizeLayout.addWidget(boardSizeLabel)
		boardSizeLayout.addWidget(boardSizeController)
		return boardSizeControllerWidget

	def make_connection(self, board: Board):
		"""function to give pass and reset signal"""
		self.passTurnSignal.connect(board.passTurn)
		self.resetGameSignal.connect(board.resetGame)

	@pyqtSlot()
	def gameStarted(self):
		pass