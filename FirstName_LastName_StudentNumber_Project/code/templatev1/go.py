from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QMenu, QAction
from PyQt5.QtCore import Qt
from board import Board
from score_board import ScoreBoard
from SettingsWidget import SettingsWidget
from HistoricWidget import HistoricWidget
from HowToPlayDialog import HowToPlayDialog
from AboutDialog import AboutDialog

class Go(QMainWindow):

	board: Board
	scoreBoard: ScoreBoard
	historicWidget: HistoricWidget
	settingsWidget: SettingsWidget
	def __init__(self):
		super().__init__()
		self.initUI()

	"""
	def getBoard(self):
		return self.board

	def getScoreBoard(self):
		return self.scoreBoard
	"""

	def initMenu(self):
		fileMenu = self.menuBar().addMenu(" File")
		fileMenu.setDisabled(True)

		viewMenu = self.menuBar().addMenu(" View")
		settingsViewAction = QAction(QIcon("./assets/icons/manual.png"), "Settings", self)
		settingsViewAction.setDisabled(True)
		viewMenu.addAction(settingsViewAction)
		historicViewAction = QAction(QIcon("./assets/icons/manual.png"), "Historic", self)
		viewMenu.addAction(historicViewAction)

		helpMenu = self.menuBar().addMenu(" Help")
		howToPlayAction = QAction(QIcon("./assets/icons/manual.png"), "How to play", self)
		howToPlayAction.setShortcut("Ctrl+H")
		helpMenu.addAction(howToPlayAction)
		howToPlayAction.triggered.connect(self.howToPlay)
		aboutAction = QAction(QIcon("./assets/icons/about.png"), "About", self)
		helpMenu.addAction(aboutAction)
		aboutAction.triggered.connect(self.about)

	def initUI(self):
		""" Initiates application UI """
		self.initMenu()
		self.board = Board(self)
		self.setCentralWidget(self.board)
		self.scoreBoard = ScoreBoard()
		self.historicWidget = HistoricWidget()
		self.settingsWidget = SettingsWidget()
		self.addDockWidget(Qt.BottomDockWidgetArea, self.scoreBoard)
		self.addDockWidget(Qt.RightDockWidgetArea, self.settingsWidget)
		self.addDockWidget(Qt.LeftDockWidgetArea, self.historicWidget)
		self.scoreBoard.make_connection(self.board)
		self.historicWidget.make_connection(self.board)

		self.resize(800, 800)
		self.center()
		self.setWindowTitle('Go')
		self.show()

	def center(self):
		""" Centers the window on the screen """
		screen = QDesktopWidget().screenGeometry()
		size = self.geometry()
		self.move((screen.width() - size.width()) / 2,(screen.height() - size.height()) / 2)

	def howToPlay(self):
		howToPlayDialog = HowToPlayDialog()
		howToPlayDialog.show()

	def about(self):
		aboutDialog = AboutDialog()
		aboutDialog.show()
