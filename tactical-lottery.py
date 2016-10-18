#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QIcon, QFont


class TheLottery(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        width = 640
        height = 480
        
        self.initWindow(width, height)
        self.initButton(width, height)

        self.show()

    def initWindow(self, width, height):
        self.setWindowTitle('P1X Tactical Lottery')
        self.setWindowIcon(QIcon('assets/icon.png'))        
        self.setFont(QFont('Courier', 24))

        self.resize(width, height)
        frame = self.frameGeometry()
        screenSize = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(screenSize)
        self.move(frame.topLeft())

        self.statusBar().setFont(QFont('Courier', 12))
        self.statusBar().showMessage('(c) 2016 P1X')

    def initButton(self, width, height):
        theButton = QPushButton('THE LUCKY BUTTON', self)
        theButton.setFont(QFont('Courier', 32))
        theButton.resize(theButton.sizeHint())
        theButton.move(width / 2 - theButton.width() /2, height / 1.5 - theButton.height() /2)        
        theButton.clicked.connect(self.messageUser)

    def messageUser(self):
        youWin = QMessageBox()
        youWin.setFont(QFont('Courier', 24))
        youWin.setWindowTitle('Congratulations')
        youWin.setText('You win a prize!')
        youWin.exec_()

        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    aw = TheLottery()
    sys.exit(app.exec_())  