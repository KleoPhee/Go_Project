from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton


class AboutDialog(QDialog):

	def __init__(self):
		super().__init__()
		self.initLayout()
		self.initDialogWindow()

	def initDialogWindow(self):
		self.setWindowIcon(QIcon("./icons/about.png"))
		self.setWindowTitle("About")
		self.setWindowFlag(Qt.WindowContextHelpButtonHint, False) # remove '?' from window bar
		self.setFixedSize(0,0) # fixe size to fit content

	def initLayout(self):
		layout = QVBoxLayout()
		layout.addWidget(QLabel("HCI and GUI Programming - Group Project: Game of Go\n\n"
								"\n  Members:\n\n"
								"      Cléophée Itier\n   (3076679) cleophee.itier@epitech.eu\n"
								"\n      Matthieu Desrues\n   (3077683) matthieu.desrues@epitech.eu\n\n"))
		btn = QPushButton("Ok")
		btn.clicked.connect(lambda: self.close())
		layout.addWidget(btn)
		self.setLayout(layout)
