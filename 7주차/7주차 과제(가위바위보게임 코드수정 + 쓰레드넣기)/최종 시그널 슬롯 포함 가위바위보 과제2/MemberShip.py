from os import name
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import MakeUi
import MyDb

class MemberShip:
    def __init__(self,revui,revdb):
        self.ui = revui
        self.db = revdb
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
        self.ui.membershipmakepushbutton.clicked.connect(self.membership_makebutton)
        self.ui.idoverlapconfirm.clicked.connect(self.membership_idbtn)
        self.ui.gobackbutton4.clicked.connect(self.goback_btn)

        
        self.idcheck = 0

    def membership_idbtn(self):
        self.idcheck += 1
        self.idInput = self.ui.membershipList[0].text()
        self.recvId = self.db.read("userinformation",["id"],[self.idInput])

        if  len(self.recvId) > 0:
            self.result = QtWidgets.QDialog()
            self.result.resize(200,50)
            self.message = QtWidgets.QLabel(self.result)
            self.message.resize(200,50)
            self.message.move(0,0)
            self.message.setText("사용하실 수 없는 아이디입니다")
            self.result.show()
        elif len(self.idInput) == 0:
            self.result = QtWidgets.QDialog()
            self.result.resize(200,50)
            self.message = QtWidgets.QLabel(self.result)
            self.message.resize(200,50)
            self.message.move(0,0)
            self.message.setText("아이디를 적어주세요")
            self.result.show()
        else:
            self.result = QtWidgets.QDialog()
            self.result.resize(200,50)
            self.message = QtWidgets.QLabel(self.result)
            self.message.resize(200,50)
            self.message.move(0,0)
            self.message.setText("사용하실 수 있는 아이디입니다")
            self.result.show()
            self.ui.membershipList[0].setDisabled(True)  #아이디 입력 막기

    def membership_makebutton(self):  
        self.idInput = self.ui.membershipList[0].text()
        self.pwInput = self.ui.pwlist.text()
        self.nameInput = self.ui.membershipList[2].text()
        self.phonenumInput = self.ui.membershipList[3].text()
        self.ageInput = self.ui.membershipList[4].text()
        self.adressInput = self.ui.membershipList[5].text()
        phonenumList = self.db.read("userinformation",["phonenum"],[self.phonenumInput])
        

        if len(self.idInput) == 0 :
            self.result = QtWidgets.QDialog()
            self.result.resize(200,50)
            self.message = QtWidgets.QLabel(self.result)
            self.message.resize(200,50)
            self.message.move(0,0)
            self.message.setText("아이디를 적어주세요")
            self.result.show()

        elif len(self.pwInput) == 0:
            self.result = QtWidgets.QDialog()
            self.result.resize(200,50)
            self.message = QtWidgets.QLabel(self.result)
            self.message.resize(200,50)
            self.message.move(0,0)
            self.message.setText("비밀번호를 적어주세요")
            self.result.show()

        elif len(self.nameInput) == 0:
            self.result = QtWidgets.QDialog()
            self.result.resize(200,50)
            self.message = QtWidgets.QLabel(self.result)
            self.message.resize(200,50)
            self.message.move(0,0)
            self.message.setText("이름을 적어주세요")
            self.result.show()
        
        elif self.korean_check():
            pass


        elif len(self.phonenumInput) == 0:
            self.result = QtWidgets.QDialog()
            self.result.resize(200,50)
            self.message = QtWidgets.QLabel(self.result)
            self.message.resize(200,50)
            self.message.move(0,0)
            self.message.setText("전화번호를 적어주세요")
            self.result.show()

        elif self.phone_check():
            pass

        elif len(phonenumList) > 0:
            self.result = QtWidgets.QDialog()
            self.result.resize(200,50)
            self.message = QtWidgets.QLabel(self.result)
            self.message.resize(200,50)
            self.message.move(0,0)
            self.message.setText("이미 있는 전화번호입니다.")
            self.result.show()


        elif len(self.ageInput) == 0:
            self.result = QtWidgets.QDialog()
            self.result.resize(200,50)
            self.message = QtWidgets.QLabel(self.result)
            self.message.resize(200,50)
            self.message.move(0,0)
            self.message.setText("나이를 적어주세요")
            self.result.show()

        elif len(self.adressInput) == 0:
            self.result = QtWidgets.QDialog()
            self.result.resize(200,50)
            self.message = QtWidgets.QLabel(self.result)
            self.message.resize(200,50)
            self.message.move(0,0)
            self.message.setText("주소를 적어주세요")
            self.result.show()

        elif self.idcheck == 0:
            self.result = QtWidgets.QDialog()
            self.result.resize(200,50)
            self.message = QtWidgets.QLabel(self.result)
            self.message.resize(200,50)
            self.message.move(0,0)
            self.message.setText("아이디 중복체크를 해주세요")
            self.result.show()

        elif len(self.recvId) > 0:
            self.result = QtWidgets.QDialog()
            self.result.resize(200,50)
            self.message = QtWidgets.QLabel(self.result)
            self.message.resize(200,50)
            self.message.move(0,0)
            self.message.setText("사용하실 수 없는 아이디입니다.")
            self.result.show()

   
            
        else:                    
            self.db.create("user",["id","pw"],[self.idInput,self.pwInput])
            self.db.create("userinformation",["id","name","phonenum","age","address"],[self.idInput,self.nameInput,self.phonenumInput,self.ageInput,self.adressInput])
            self.result = QtWidgets.QDialog()
            self.result.resize(200,50)
            self.message = QtWidgets.QLabel(self.result)
            self.message.resize(200,50)
            self.message.move(0,0)
            self.message.setText("회원가입이 완료되었습니다 감사합니다")
            self.result.show()
            self.ui.stackedWidget.setCurrentIndex(self.ui.setpage)

    def korean_check(self):
        for index in range(0,len(list(self.nameInput))):
            if self.nameInput[index] in self.characterList:
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
        for index in range(0,len(list(self.phonenumInput))):
            if self.phonenumInput[index] in self.phoneCheckList:
                self.result = QtWidgets.QDialog()
                self.result.resize(200,50)
                self.message = QtWidgets.QLabel(self.result)
                self.message.resize(200,50)
                self.message.move(0,0)
                self.message.setText("전화번호는 숫자만 사용가능합니다")
                self.result.show()
                return True
        return False
            

    # def length_check(self, min, max):
    #     if len(self.idInput) < min or len(self.idInput) > max:
    #         self.result = QtWidgets.QDialog()
    #         self.result.resize(200,50)
    #         self.message = QtWidgets.QLabel(self.result)
    #         self.message.resize(200,50)
    #         self.message.move(0,0)
    #         self.message.setText("아이디 길이는"+ " " +"최소"+min+"이상")
    #         self.result.show()

    #         len(self.pwInput)
    #         len(self.nameInput)
    #         len(self.phonenumInput)
    #         len(self.ageInput)
    #         len(self.adressInput)
        

    def goback_btn(self):
        self.ui.stackedWidget.setCurrentIndex(self.ui.setpage)