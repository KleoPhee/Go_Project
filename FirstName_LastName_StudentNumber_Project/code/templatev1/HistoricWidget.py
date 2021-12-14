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

	@pyqtSlot(int, int)
	def addPlay(self, row: int, col: int):
		"""
		Add a new move to the historic
		"""
		self.historicListView.addItem(QListWidgetItem("Played in "+chr(65+col)+str(row+1)))
