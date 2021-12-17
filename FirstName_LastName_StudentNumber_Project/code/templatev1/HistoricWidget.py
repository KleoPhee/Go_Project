from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDockWidget, QWidget, QVBoxLayout, QListWidget, QListWidgetItem

from board import Board


class HistoricWidget(QDockWidget):

	historicListView: QListWidget

	def __init__(self):
		"""
		Initiates Historic Widget
		"""
		super().__init__()
		self.resize(200, 200)
		self.setWindowTitle('Historic')
		mainWidget = QWidget()
		mainLayout = QVBoxLayout()

		self.historicListView = QListWidget()

		mainWidget.setLayout(mainLayout)
		mainLayout.addWidget(self.historicListView)
		self.setWidget(mainWidget)

	def make_connection(self, board: Board):
		"""
		This handles some signals sent from the board class
		"""
		# when the updateTimerSignal is emitted in the board the setTimeRemaining slot receives it
		board.newMoveSignal.connect(self.addPlay)

	@pyqtSlot(dict)
	def addPlay(self, play: dict):
		"""
		Add a new move to the historic
		"""
		self.historicListView.addItem(QListWidgetItem(self.buildHistoricEntry(play)))

	def buildHistoricEntry(self, play: dict):
		historicEntry = 'Played in ' + chr(65 + play['tile']['x']) + str(play['tile']['y'] + 1)
		if len(play['takenPieces']) > 0:
			historicEntry += '\nThe following pieces have been removed:'
			for i in range(0,len(play['takenPieces'])):
				historicEntry += '\n   - ' + chr(65 + play['takenPieces'][i]['x']) + str(play['takenPieces'][i]['y'] + 1)
		return historicEntry
