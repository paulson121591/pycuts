from PyQt5.QtWidgets import *
import sys
import os
from os import listdir

folder_names = []
for entry_name in os.listdir('O:\Jobs'):
    entry_path = os.path.join('O:\Jobs', entry_name)
    if os.path.isdir(entry_path):
        folder_names.append(entry_name)


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        # auto complete options                                                 
        completer = QCompleter(folder_names)

        # create line edit and add auto complete                                
        self.lineedit = QLineEdit()
        self.lineedit.setCompleter(completer)
        layout.addWidget(self.lineedit, 0, 0)

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())