from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import MakeUi
import MyDb
import IdFinding
import PwFinding
import MemberShip
import GamePage
class Home:
    def __init__(self):
        self.ui = MakeUi.MakeUi()
        self.db = MyDb.MyDb()
        self.init_event()
        self.characterList = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',
        'Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M',
        '1','2','3','4','5','6','7','8','9','0',
        ',','.','/',';',"'",'[',']','-','=','`','<','>','?',':','"','{','}','_','+','~','!','@','#','$','%','^','&','*','(',')']
        self.phoneCheckList = ['ㅂ','ㅈ','ㄷ','ㄱ','ㅅ','ㅛ','ㅕ,''ㅑ','ㅐ','ㅔ','ㅁ','ㄴ','ㅇ','ㄹ','ㅎ','ㅗ','ㅓ','ㅏ','ㅣ','ㅋ','ㅌ','ㅊ','ㅍ','ㅠ','ㅜ','ㅡ',
        'q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',
        'Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M',',','.','/',';',"'",
        '[',']','-','=','`','<','>','?',':','"','{','}','_','+','~','!','@','#','$','%','^','&','*','(',')']


    def init_event(self):
        for index in range(0,2):
            self.ui.managegameList[index].enterEvent =lambda event, num = index: self.numberEnterEvent(event, num)
            self.ui.managegameList[index].leaveEvent =lambda event, num = index: self.numberLeaveEvent(event, num)
            self.ui.findingidpwList[0].clicked.connect(self.idfind_btn)
            self.ui.findingidpwList[1].clicked.connect(self.pwfind_btn)
            self.ui.loginmemberbtnList[0].clicked.connect(self.login_btn)
            self.ui.loginmemberbtnList[1].clicked.connect(self.membership_btn)
            self.ui.gobackbutton.clicked.connect(self.goback_btn)
            self.ui.managegameList[0].clicked.connect(self.membershipchange_btn)
            self.ui.managegameList[1].clicked.connect(self.gogame_btn)
            self.ui.updateBtnList[0].clicked.connect(self.idupdate_btn)
            self.ui.updateBtnList[1].clicked.connect(self.nameupdate_btn)
            self.ui.updateBtnList[2].clicked.connect(self.phonenumupdate_btn)
            self.ui.updateBtnList[3].clicked.connect(self.ageupdate_btn)
            self.ui.updateBtnList[4].clicked.connect(self.adressupdate_btn)
            self.ui.memberDeleteGoHomeList[0].clicked.connect(self.deletmember_btn)
            self.ui.memberDeleteGoHomeList[1].clicked.connect(self.gohome_btn)
        

    def numberEnterEvent(self, event, index):
        self.ui.managegameList[index].setStyleSheet(
            "background-color: rgb(52, 177, 230);font: 15pt \"맑은 고딕\";"
        )
    def numberLeaveEvent(self, event, index):
        self.ui.managegameList[index].setStyleSheet(
            "background-color: rgb(52, 177, 200);font: 12pt \"맑은 고딕\";"
        )


    def idfind_btn(self):
        self.idFinding = IdFinding.IdFinding(self.ui,self.db)
        self.ui.stackedWidget.setCurrentIndex(self.ui.setpage + 3)


    def pwfind_btn(self):
        self.pwFinding = PwFinding.PwFinding(self.ui,self.db)
        self.ui.stackedWidget.setCurrentIndex(self.ui.setpage + 5)

    def login_btn(self):
        self.idValue = self.ui.windowList[0].text()
        self.pwValue = self.ui.pwWindow.text()
        self.recvResult1 = self.db.read("user",["id"],[self.idValue])
        self.recvResult2 = self.db.read("user",["pw"],[self.pwValue])
        if len(self.recvResult1) == 0 and len(self.recvResult2) == 0:
                self.result = QtWidgets.QDialog() # 오른쪽 소괄호는 내가 만든 위젯의 부모, 부모가 없을 경우 비워둔다. 
                self.result.resize(200,50)
                self.message = QtWidgets.QLabel(self.result) # 부모가 있음
                self.message.resize(200,50)
                self.message.move(0,0)
                self.message.setText("ID와 PW 둘 다 확인해주세요")
                self.result.show()
                         
        elif len(self.recvResult1) == 0:
                self.result = QtWidgets.QDialog()
                self.result.resize(200,50)
                self.message = QtWidgets.QLabel(self.result)
                self.message.resize(200,50)
                self.message.move(0,0)
                self.message.setText("ID를 확인해주세요")
                self.result.show()

        elif len(self.recvResult2) == 0:            
                self.result = QtWidgets.QDialog()
                self.result.resize(200,50)
                self.message = QtWidgets.QLabel(self.result) 
                self.message.resize(200,50)
                self.message.move(0,0)
                self.message.setText("pw를 확인해주세요")
                self.result.show()
        else:
            self.ui.stackedWidget.setCurrentIndex(self.ui.setpage + 1)

    def goback_btn(self):
        self.ui.stackedWidget.setCurrentIndex(self.ui.setpage)


    def membershipchange_btn(self):
        self.ui.stackedWidget.setCurrentIndex(self.ui.setpage + 2)
        self.recvResult1 = self.db.read("userinformation",["id"],[self.idValue])        #로그인 할때 입력받은 아이디를 이용해서 회원정보를 출력함
        self.ui.existList[0].setText(self.recvResult1[0][0])
        self.ui.existList[1].setText(self.recvResult1[0][1])
        self.ui.existList[2].setText(self.recvResult1[0][2])
        self.ui.existList[3].setText(self.recvResult1[0][3])
        self.ui.existList[4].setText(self.recvResult1[0][4])

    def idupdate_btn(self):
        updateId = self.ui.updateList[0].text()
        confirmId = self.db.read("user",["id"],[updateId])
        if len(updateId) == 0:
            self.result = QtWidgets.QDialog()
            self.result.resize(200,50)
            self.message = QtWidgets.QLabel(self.result) 
            self.message.resize(200,50)
            self.message.move(0,0)
            self.message.setText("아이디를 입력해주세요.")
            self.result.show()
        elif len(confirmId) == 0:
            self.db.update("userinformation", ["id"], [updateId], ["id"], [self.idValue])  #로그인 할때 아이디를 이용하여 업데이트함
            self.db.update("user",["id"],[updateId],["id"],[self.idValue])
            self.result = QtWidgets.QDialog()
            self.result.resize(200,50)
            self.message = QtWidgets.QLabel(self.result) 
            self.message.resize(200,50)
            self.message.move(0,0)
            self.message.setText("아이디가 "+updateId+"로 수정되었습니다.")
            self.result.show()
        else:
            self.result = QtWidgets.QDialog()
            self.result.resize(200,50)
            self.message = QtWidgets.QLabel(self.result) 
            self.message.resize(200,50)
            self.message.move(0,0)
            self.message.setText("이미 있는 아이디입니다.")
            self.result.show()

    def nameupdate_btn(self):                                                           #이름수정 함수
        self.updateName = self.ui.updateList[1].text()
        if len(self.updateName) == 0:
            self.result = QtWidgets.QDialog()
            self.result.resize(200,50)
            self.message = QtWidgets.QLabel(self.result) 
            self.message.resize(200,50)
            self.message.move(0,0)
            self.message.setText("이름을 입력해주세요.")
            self.result.show()

        elif self.korean_check():
            pass
            
        else:
            self.db.update("userinformation", ["name"], [self.updateName], ["id"], [self.idValue])
            self.result = QtWidgets.QDialog()
            self.result.resize(200,50)
            self.message = QtWidgets.QLabel(self.result) 
            self.message.resize(200,50)
            self.message.move(0,0)
            self.message.setText("이름이 "+self.updateName+"로 수정되었습니다.")
            self.result.show()

    def phonenumupdate_btn(self):                                                       #전화번호수정 함수
        self.updatePhoneNum = self.ui.updateList[2].text()
        confirmPhonenum = self.db.read("userinformation", ["phonenum"], [self.updatePhoneNum])
        if len(self.updatePhoneNum) == 0:
            self.result = QtWidgets.QDialog()
            self.result.resize(200,50)
            self.message = QtWidgets.QLabel(self.result) 
            self.message.resize(200,50)
            self.message.move(0,0)
            self.message.setText("전화번호를 입력해주세요.")
            self.result.show()
        
        elif self.phone_check():
            pass
        
        elif len(confirmPhonenum) == 0:
            self.db.update("userinformation", ["phonenum"], [self.updatePhoneNum], ["id"], [self.idValue])
            self.result = QtWidgets.QDialog()
            self.result.resize(200,50)
            self.message = QtWidgets.QLabel(self.result) 
            self.message.resize(200,50)
            self.message.move(0,0)
            self.message.setText("전화번호가 "+self.updatePhoneNum+"로 수정되었습니다.")
            self.result.show()
        else:
            self.result = QtWidgets.QDialog()
            self.result.resize(200,50)
            self.message = QtWidgets.QLabel(self.result) 
            self.message.resize(200,50)
            self.message.move(0,0)
            self.message.setText("이미 있는 전화번호입니다.")
            self.result.show()

    def ageupdate_btn(self):                                                            #나이수정 함수
        updateAge = self.ui.updateList[3].text()
        if len(updateAge) == 0:
            self.result = QtWidgets.QDialog()
            self.result.resize(200,50)
            self.message = QtWidgets.QLabel(self.result) 
            self.message.resize(200,50)
            self.message.move(0,0)
            self.message.setText("나이를 입력해주세요.")
            self.result.show()
        else:
            self.db.update("userinformation", ["age"], [updateAge], ["id"], [self.idValue])
            self.result = QtWidgets.QDialog()
            self.result.resize(200,50)
            self.message = QtWidgets.QLabel(self.result) 
            self.message.resize(200,50)
            self.message.move(0,0)
            self.message.setText("나이가 "+updateAge+"로 수정되었습니다.")
            self.result.show()

    def adressupdate_btn(self):                                                         #주소수정 함수
        updateAdress = self.ui.updateList[4].text()
        if len(updateAdress) == 0:
            self.result = QtWidgets.QDialog()
            self.result.resize(200,50)
            self.message = QtWidgets.QLabel(self.result) 
            self.message.resize(200,50)
            self.message.move(0,0)
            self.message.setText("주소를 입력해주세요.")
            self.result.show()
        
        else:
            self.db.update("userinformation", ["adress"], [updateAdress], ["id"], [self.idValue])
            self.result = QtWidgets.QDialog()
            self.result.resize(200,50)
            self.message = QtWidgets.QLabel(self.result) 
            self.message.resize(200,50)
            self.message.move(0,0)
            self.message.setText("주소가 "+updateAdress+"로 수정되었습니다.")
            self.result.show()

    def deletmember_btn(self):                                                          #계정삭제 함수
        self.db.delete("userinformation", ["id"], [self.idValue])
        self.db.delete("user",["id"], [self.idValue])
        self.result = QtWidgets.QDialog()
        self.result.resize(200,50)
        self.message = QtWidgets.QLabel(self.result) 
        self.message.resize(200,50)
        self.message.move(0,0)
        self.message.setText("아이디가 "+self.idValue+"인 계정이 삭제되었습니다.")
        self.result.show()

    def korean_check(self):
        for index in range(0,len(list(self.updateName))):
            if self.updateName[index] in self.characterList:
                
                self.result = QtWidgets.QDialog()
                self.result.resize(200,50)
                self.message = QtWidgets.QLabel(self.result)
                self.message.resize(200,50)
                self.message.move(0,0)
                self.message.setText("이름은 한글만 사용가능합니다")
                self.result.show()
                return True
        return False

    def phone_check(self):
        for index in range(0,len(list(self.updatePhoneNum))):
            if self.updatePhoneNum[index] in self.phoneCheckList:
                self.result = QtWidgets.QDialog()
                self.result.resize(200,50)
                self.message = QtWidgets.QLabel(self.result)
                self.message.resize(200,50)
                self.message.move(0,0)
                self.message.setText("전화번호는 숫자만 사용가능합니다")
                self.result.show()
                return True
        return False

    def gohome_btn(self):
        self.ui.stackedWidget.setCurrentIndex(self.ui.setpage)


    def gogame_btn(self):
        self.gamePage = GamePage.GamePage(self.ui)
        self.ui.stackedWidget.setCurrentIndex(self.ui.setpage + 8)
        

    def membership_btn(self):
        self.memberShip = MemberShip.MemberShip(self.ui,self.db)
        self.ui.stackedWidget.setCurrentIndex(self.ui.setpage + 7)


if __name__ == "__main__":
    app =QtWidgets.QApplication(sys.argv)
    home = Home()
    sys.exit(app.exec_())
