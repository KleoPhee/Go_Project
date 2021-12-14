from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QStandardItemModel
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QGridLayout, QTreeView


class HowToPlayDialog(QDialog):

	manual: list
	index: int

	def __init__(self):
		super().__init__()
		self.initManual()
		self.initLayout()
		self.initDialogWindow()

	def initManual(self):
		self.manual = [
			{'unique_id':1, 'parent_id':0, 'name':'Basics'},
			{'unique_id':2, 'parent_id':1, 'name':'Place a piece', 'image':' ', 'description':' '},
		]

	def initDialogWindow(self):
		self.setWindowIcon(QIcon("./assets/icons/manual.png"))
		self.setWindowTitle("How to play")
		self.setWindowFlag(Qt.WindowContextHelpButtonHint, False) # remove '?' from window bar
		self.setFixedSize(0,0) # fixe size to fit content

	def initLayout(self):
		quickNavTree = QTreeView()
		prevButton = QPushButton("Previous")
		prevButton.clicked.connect(lambda: self.navigate(-1))
		nextButton = QPushButton("Next")
		nextButton.clicked.connect(lambda: self.navigate(1))

		layout = QGridLayout()
		layout.addWidget(QLabel("Descriptive text"), 0, 1)
		layout.addWidget(quickNavTree,0,0)
		layout.addWidget(prevButton,2,1)
		layout.addWidget(nextButton,2,3)
		layout.columnStretch(2)
		self.setLayout(layout)

	def navigate(self, to :int):
		pass