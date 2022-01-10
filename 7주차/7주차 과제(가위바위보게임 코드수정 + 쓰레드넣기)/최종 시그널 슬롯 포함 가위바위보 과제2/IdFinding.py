from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import MakeUi
import MyDb

class IdFinding:
    def __init__(self,revui,revdb):
        self.ui = revui
        self.db = revdb
        self.init_event()

    def init_event(self):
        self.ui.nextpushbutton.clicked.connect(self.idfind_nextbtn)
        self.ui.gobackbutton2.clicked.connect(self.goback_btn)
        self.ui.gohomepushbutton.clicked.connect(self.gohome_btn)

    def idfind_nextbtn(self):
        nameInput = self.ui.namephoneList[0].text()
        phonenumInput = self.ui.namephoneList[1].text()
        self.recvName = self.db.read("userinformation",["name"],[nameInput])
        self.recvPhonenum = self.db.read("userinformation",["phonenum"],[phonenumInput])

        if  len(nameInput) == 0 or len(phonenumInput) == 0 or len(self.recvName) == 0 or len(self.recvPhonenum) == 0:
            self.result = QtWidgets.QDialog()
            self.result.resize(200,50)
            self.message = QtWidgets.QLabel(self.result) 
            self.message.resize(200,50)
            self.message.move(0,0)
            self.message.setText("이름과 전화번호를 확인해주세요")
            self.result.show()
        elif self.recvName[0][0] == self.recvPhonenum[0][0] :
            self.ui.nextpushbutton.clicked.connect(self.idrealprint_label)

    def goback_btn(self):
        self.ui.stackedWidget.setCurrentIndex(self.ui.setpage)
    
    def idrealprint_label(self):
        self.ui.stackedWidget.setCurrentIndex(self.ui.setpage + 4)   #idfind_nextbtn함수 위에 elif에서 페이지 넘기는 명령어 선언해줘서 에러 발생
        self.ui.idrealprintlabel.setText(self.recvName[0][0])

    def gohome_btn(self):
        self.ui.stackedWidget.setCurrentIndex(self.ui.setpage)


