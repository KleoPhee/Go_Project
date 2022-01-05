from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QMenu, QAction
from PyQt5.QtCore import Qt

from FirstName_LastName_StudentNumber_Project.code.templatev1.score_board import ScoreBoard
from board import Board
from SettingsWidget import SettingsWidget
from HistoricWidget import HistoricWidget
from HowToPlayDialog import HowToPlayDialog
from AboutDialog import AboutDialog

class Go(QMainWindow):

	board: Board
	historicViewAction: QAction
	historicWidget: HistoricWidget
	settingsViewAction: QAction
	settingsWidget: SettingsWidget
	scoreBoard: ScoreBoard

	def __init__(self):
		super().__init__()
		self.initUI()

	def initMenu(self):
		"""
		Function to initialize the menu historic and settings
		:return:
		"""
		viewMenu = self.menuBar().addMenu(" View")
		self.settingsViewAction = QAction(QIcon("./assets/icons/ticked.png"), "Settings", self)
		self.settingsViewAction.triggered.connect(self.toggleSettings)
		viewMenu.addAction(self.settingsViewAction)
		self.historicViewAction = QAction(QIcon("./assets/icons/ticked.png"), "Historic", self)
		self.historicViewAction.triggered.connect(self.toggleHistoric)
		viewMenu.addAction(self.historicViewAction)

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
		self.historicWidget = HistoricWidget()
		self.settingsWidget = SettingsWidget()
		self.scoreBoard = ScoreBoard()

		self.addDockWidget(Qt.LeftDockWidgetArea, self.settingsWidget)
		self.addDockWidget(Qt.LeftDockWidgetArea, self.historicWidget)
		self.addDockWidget(Qt.LeftDockWidgetArea, self.scoreBoard)
		self.historicWidget.make_connection(self.board)
		self.scoreBoard.make_connection(self.board)
		self.settingsWidget.make_connection(self.board)

		self.resize(800, 800)
		self.center()
		self.setWindowTitle('Go')
		self.setWindowIcon(QIcon('./assets/icons/Go.png'))
		self.show()

	def center(self):
		""" Centers the window on the screen """
		screen = QDesktopWidget().screenGeometry()
		size = self.geometry()
		self.move((screen.width() - size.width()) / 2,(screen.height() - size.height()) / 2)

	def howToPlay(self):
		howToPlayDialog = HowToPlayDialog()
		howToPlayDialog.exec()

	def about(self):
		aboutDialog = AboutDialog()
		aboutDialog.exec()

	def toggleSettings(self):
		currentState = self.settingsViewAction.isIconVisibleInMenu()
		self.settingsViewAction.setIconVisibleInMenu(not currentState)
		self.settingsWidget.hide() if currentState else self.settingsWidget.show()

	def toggleHistoric(self):
		currentState = self.historicViewAction.isIconVisibleInMenu()
		self.historicViewAction.setIconVisibleInMenu(not currentState)
		self.historicWidget.hide() if currentState else self.historicWidget.show()