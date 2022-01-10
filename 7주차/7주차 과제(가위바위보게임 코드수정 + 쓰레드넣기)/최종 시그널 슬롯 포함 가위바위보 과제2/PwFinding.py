from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import MakeUi
import MyDb

class PwFinding:
    def __init__(self,revui,revdb):
        self.ui = revui
        self.db = revdb
        self.init_event()

    def init_event(self):
        self.ui.nextpushbutton2.clicked.connect(self.pwfind_nextbtn)
        self.ui.gobackbutton3.clicked.connect(self.goback_btn)

    def pwfind_nextbtn(self):
        self.idInput = self.ui.idphoneList[0].text()
        phonenumInput = self.ui.idphoneList[1].text()
        self.recvId = self.db.read("userinformation",["id"],[self.idInput])
        self.recvPhonenum = self.db.read("userinformation",["phonenum"],[phonenumInput])

        if  len(self.idInput) == 0 or len(phonenumInput) == 0 or len(self.recvId) == 0 or len(self.recvPhonenum) == 0:
            self.result = QtWidgets.QDialog()
            self.result.resize(200,50)
            self.message = QtWidgets.QLabel(self.result)
            self.message.resize(200,50)
            self.message.move(0,0)
            self.message.setText("아이디와 전화번호를 확인해주세요")
            self.result.show()
        elif self.recvId[0][0] == self.recvPhonenum[0][0] :             #인증번호는 없고 로우들 중 아이디로 계정을 확인한이유는 회원가입 할 때 아이디 예외처리를 함
            self.ui.stackedWidget.setCurrentIndex(self.ui.setpage + 6)
            self.newpw_inputlabel()

    def newpw_inputlabel(self):
        self.ui.pwconfirmpushbutton.clicked.connect(self.pwconfirm_btn)

    def pwconfirm_btn(self):
        self.newpwInput = self.ui.newpwrealinputlabel.text()             #버튼을 누른 후에 새로운 비밀번호 데이터를 가져와야 입력이 됨. 
        self.db.update("user",["pw"],[self.newpwInput],["id"],[self.idInput])
        self.ui.stackedWidget.setCurrentIndex(self.ui.setpage)
        self.result = QtWidgets.QDialog()
        self.result.resize(200,50)
        self.message = QtWidgets.QLabel(self.result) 
        self.message.resize(200,50)
        self.message.move(0,0)
        self.message.setText("새 비밀번호로 변경되었습니다")
        self.result.show()

    def goback_btn(self):
        self.ui.stackedWidget.setCurrentIndex(self.ui.setpage)
