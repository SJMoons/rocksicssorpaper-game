from PyQt5 import QtCore, QtGui, QtWidgets
import threading
import GamePage
import time
import sys


class MyThread(threading.Thread, QtCore.QObject):   #쓰레드 클래스가 두개 이상 클래스에 쓰이면 클래스를 만들고 하나에만 쓰이면 게임페이지에 한 파일로 만들기
    resultSignal = QtCore.pyqtSignal(str)   # FEEDBACK: 쓰레드를 통한 결과값을 받는 방법 중 1개 ( Signal/Slot )
                                            # FEEDBACK: 클래스 안에서 사용하는 전역변수 즉, 멤버변수와 동일하지만 이렇게 적어주어야만 함
    #
    def __init__(self, revui):
        threading.Thread.__init__(self)
        QtCore.QObject.__init__(self)
        self.ui = revui
        # self.num = 0
        self.gameList = ["가위","바위","보"]
        self.locale = 0

        # self.ui.gameList[0].clicked.connect(self.gam.scissor_btn)

    def run(self):          #쓰레드안에서는 GUI작업을 해주면 안된다.
        while True:         #위에는 self.num = 0일때 계속 돌고
            self.resultSignal.emit(self.gameList[self.locale])   # FEEDBACK: 알고리즘적으로 최적화 되어있음
                                                                # FEEDBACK: emit을 통해 slot으로 데이터를 보내줄 수 있음. 보내주는 데이터는 emit 괄호 안에 들어가는 데이터
            self.locale += 1
            self.locale %= 3
            time.sleep(1.5)
            # if :            #이프문 말고 시그널 슬롯으로 대체   #아래는 self.num = 1 일때 
            #     # self.rand = random.randint(0,2)
            #     # self.resultSignal.emit(self.gameList[self.rand])
            #     break
            #     self.gam.scissor_btn()
    