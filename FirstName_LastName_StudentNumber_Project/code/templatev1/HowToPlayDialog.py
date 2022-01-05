from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QStandardItemModel, QPixmap
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QGridLayout, QTreeView, QSizePolicy, QStyle


class HowToPlayDialog(QDialog):

	prevButton: QPushButton
	nextButton: QPushButton
	chapterLabel: QLabel
	imageHolder: QLabel
	descriptionLabel: QLabel
	indexLabel: QLabel
	manual: list
	index: int

	def __init__(self):
		super().__init__()
		self.index=0
		self.initManual()
		self.initLayout()
		self.initDialogWindow()
		self.updateUI()
		self.setFixedSize(300,500)

	def initManual(self):
		self.manual = [
			{'chapter':'About Go !','description':'Go is an abstract strategy board game invented in China more than 2,500 years ago. It confronts two players with the aim to surround more territory than the opponent.','image':'./assets/icons/goBoard.jpg'},
			{'chapter':'How to play ?','description':'The goal of the game is to surround the largest areas. Stones are caputured and not moved during the game once set on the board.','image':'./assets/icons/Go_game.png'},
			{'chapter':'Place a stone ?','description':'You can place a stone by clicking an intersection of the board grid','image':'./assets/icons/Capture_stone.png'},
			{'chapter': 'Suicide Rule ?', 'description': 'You cannot place a stone which will immediately have no liberties. A liberty is a free intersections surrounding a stone. ', 'image':'./assets/icons/suicide_rule.png'},
			{'chapter':'KO rule ?','description':'To prevent endlessly re-capturing the same space, the "Ko rule" prevents the player to immediately recapturing the same position.','image':'./assets/icons/KO_rule.png'},
			{'chapter':'End of game ?','description':'If both players pass their turns the game end.','image':'./assets/icons/end_game.png'},
		]
		# Following lines are a code sample if we are willing to implement .gif display
		#self.movie = QMovie("earth.gif")
		#self.label.setMovie(self.movie)
		#self.movie.start()

	def initDialogWindow(self):
		self.setWindowIcon(QIcon("./assets/icons/manual.png"))
		self.setWindowTitle("How to play")
		self.setWindowFlag(Qt.WindowContextHelpButtonHint, False) # remove '?' from window bar
		self.setFixedSize(0,0) # fixe size to fit content

	def initLayout(self):
		self.chapterLabel = QLabel()
		self.chapterLabel.setStyleSheet('font-weight:bold;font-size:22px;margin:10px')
		self.chapterLabel.setAlignment(Qt.AlignCenter)

		self.descriptionLabel = QLabel()
		self.descriptionLabel.setWordWrap(True)
		self.descriptionLabel.setMinimumSize(200,40)
		self.descriptionLabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
		self.descriptionLabel.setAlignment(Qt.AlignCenter)
		self.descriptionLabel.setStyleSheet('font-size:16px')

		self.imageHolder = QLabel()
		self.imageHolder.setFixedSize(200,200)
		self.imageHolder.setAlignment(Qt.AlignCenter)

		self.prevButton = QPushButton(QIcon('./assets/icons/left-arrow.png'),'')
		self.prevButton.clicked.connect(lambda: self.navigate(-1))
		self.indexLabel = QLabel()
		self.indexLabel.setStyleSheet('font-size:16px')
		self.nextButton = QPushButton(QIcon('./assets/icons/right-arrow.png'),'')
		self.nextButton.clicked.connect(lambda: self.navigate(1))

		layout = QGridLayout()
		layout.addWidget(self.chapterLabel,0,1,1,5)
		layout.addWidget(self.imageHolder,1,1,1,5)
		layout.addWidget(self.descriptionLabel,2,1,1,5)
		layout.addWidget(self.prevButton,3,2)
		layout.addWidget(self.indexLabel,3,3)
		layout.addWidget(self.nextButton,3,4)
		layout.setRowStretch(2,1)
		layout.setColumnStretch(0,1)
		layout.setColumnStretch(1,1)
		layout.setColumnStretch(5,1)
		layout.setColumnStretch(6,1)
		self.setLayout(layout)

	def navigate(self, to :int):
		self.index += to
		self.updateUI()

	def updateUI(self):
		self.prevButton.setDisabled(self.index == 0)
		self.nextButton.setDisabled(self.index == len(self.manual)-1)
		self.indexLabel.setText(str(self.index+1)+'/'+str(len(self.manual)))
		image = QPixmap(self.manual[self.index]['image']
						if '' != self.manual[self.index]['image']
						else './assets/icons/Go.png')
		self.imageHolder.setPixmap(image.scaledToWidth(200))
		self.descriptionLabel.setText(self.manual[self.index]['description'])
		self.chapterLabel.setText(self.manual[self.index]['chapter'])
