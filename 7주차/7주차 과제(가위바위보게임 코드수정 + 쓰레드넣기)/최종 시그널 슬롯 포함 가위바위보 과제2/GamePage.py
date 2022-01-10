from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import sys
import random
import MyThread

class GamePage:
    def __init__(self, revui):
        self.ui = revui
        self.game = ["가위","바위","보"]
        self.init_event()
        
    def init_event(self):
        self.ui.gameoverbutton.enterEvent = lambda event : self.enterEvent(event)
        self.ui.gameoverbutton.leaveEvent =lambda event : self.leaveEvent(event)
        self.ui.gameoverbutton.clicked.connect(self.gameover_btn)
        self.ui.gobackbutton5.clicked.connect(self.goback_btn)
        for index in range(0,3):
            self.ui.gameList[index].enterEvent = lambda event, num = index : self.gameEnterEvent(event, num)
            self.ui.gameList[index].leaveEvent = lambda event, num = index : self.gameLeaveEvent(event, num)
        self.ui.gameList[0].clicked.connect(self.scissor_btn)
        self.ui.gameList[1].clicked.connect(self.rock_btn)
        self.ui.gameList[2].clicked.connect(self.paper_btn)
        self.myThread = MyThread.MyThread(self.ui)
        self.myThread.resultSignal.connect(self.resultChange)   # FEEDBACK: 쓰레드 클래스 안에 있는 Signal과 여기 페이지에서 만든 slot을 연결하는 과정
        self.myThread.start()

    def enterEvent(self,event):
        self.ui.gameoverbutton.setStyleSheet(
            "background-color: rgb(255,25,25);font: 12pt \"맑은 고딕\";"
        )
    def leaveEvent(self,event):
        self.ui.gameoverbutton.setStyleSheet(
            "background-color: rgb(225,124,48);font: 10pt \"맑은 고딕\";"
        )

    def gameEnterEvent(self,event,index):
        self.ui.gameList[index].setStyleSheet(
            "background-color: grey;"
        )
    def gameLeaveEvent(self,event,index):
        self.ui.gameList[index].setStyleSheet(
            "background-color: lightgrey;"
        )



    def random_com(self):
        # self.myThread.num += 1
        self.rand = random.randint(0,2)
        self.com = self.game[self.rand]
        self.ui.result[0].setText(self.com)
        self.ui.result[0].setAlignment(QtCore.Qt.AlignCenter)

        # self.myThread.run()

    def scissor_btn(self):
        self.myhandle = '가위'
        # self.myThread.resultSignal.connect(self.random_com)
        self.random_com()
        self.result_browser()

    def paper_btn(self):
        # self.ui.num += 1
        self.myhandle = '보'
        self.random_com()
        self.result_browser()

    def rock_btn(self):
        # self.ui.num += 1
        self.myhandle = '바위'
        self.random_com()
        self.result_browser()

    def result_browser(self):
        win="이겼당!!"
        draw="비겼당!"
        lose="졌당ㅠㅠ"
        if self.myhandle == '가위' :
            if self.com == '가위' :
                self.ui.result[1].setText(draw)
                self.ui.result[1].setAlignment(QtCore.Qt.AlignCenter)
            elif self.com == '바위' :
                self.ui.result[1].setText(lose)
                self.ui.result[1].setAlignment(QtCore.Qt.AlignCenter)
            elif self.com == '보':
                self.ui.result[1].setText(win)
                self.ui.result[1].setAlignment(QtCore.Qt.AlignCenter)
            
        elif self.myhandle == '보':
            if self.com == '보':
                self.ui.result[1].setText(draw)
                self.ui.result[1].setAlignment(QtCore.Qt.AlignCenter)
            elif self.com == '가위':
                self.ui.result[1].setText(lose)
                self.ui.result[1].setAlignment(QtCore.Qt.AlignCenter)
            elif self.com == '바위':
                self.ui.result[1].setText(win)
                self.ui.result[1].setAlignment(QtCore.Qt.AlignCenter)

        elif self.myhandle == '바위':
            if self.com == '바위':
                self.ui.result[1].setText(draw)
                self.ui.result[1].setAlignment(QtCore.Qt.AlignCenter)
            elif self.com == '가위':
                self.ui.result[1].setText(win)
                self.ui.result[1].setAlignment(QtCore.Qt.AlignCenter)
            elif self.com == '보':
                self.ui.result[1].setText(lose)
                self.ui.result[1].setAlignment(QtCore.Qt.AlignCenter)


    def goback_btn(self):
        self.ui.stackedWidget.setCurrentIndex(self.ui.setpage)

    def gameover_btn(self):
        exit()

    def resultChange(self, value):
        self.ui.result[0].setText(value)
        self.ui.result[0].setAlignment(QtCore.Qt.AlignCenter)