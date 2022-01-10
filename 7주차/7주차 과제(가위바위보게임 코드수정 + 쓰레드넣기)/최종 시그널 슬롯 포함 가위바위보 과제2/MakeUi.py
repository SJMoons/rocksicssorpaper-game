from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import MyThread

class MakeUi:    #type,font,dialog 세개를 하나로 합치고 data클래스로 묶어서 사용  대표적으로 이렇게 하는 것 색상값,텍스트값,언어값
    def __init__(self):
        self.setpage = 0
        self.mainWindow = QtWidgets.QMainWindow()
        self.mainWindow.setMinimumSize(QtCore.QSize(531,701))
        self.mainWindow.setMaximumSize(QtCore.QSize(531,701))
        self.mainWindow.resize(528, 707)

        self.centralWidget = QtWidgets.QWidget(self.mainWindow)
        self.centralWidget.setGeometry(0, 10, 531, 701)

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralWidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 10, 531, 691))
        self.stackedWidget.setMinimumSize(QtCore.QSize(531,691))
        self.stackedWidget.setMaximumSize(QtCore.QSize(531,691))
        self.stackedWidget.setStyleSheet("")

        #처음시작 화면
        self.home = QtWidgets.QWidget()
        self.home.setGeometry(QtCore.QRect(0, 0, 531, 691))
        # pixmap = QtGui.QPixmap("homeimage.png")
        # self.home.setPixmap(pixmap)
        # self.homeIcon = QtGui.QPixmap("image/homeimage.png")
        # self.home.setIcon(QtGui.QIcon(self.homeIcon))
        # self.home.setPixmap(QtGui.QPixmap("gamebackground.jpg")) 

        self.home.setStyleSheet(
            "border-image: url(image/gameimage.png);"
        )
        self.gamenametext = QtWidgets.QTextBrowser(self.home)       #폰트 해상도 따라서 유지되고 큐텍스트브라우저는 스크롤이 포함됨
        self.gamenametext.setGeometry(110, 20, 311, 148)
        self.gamenametext.setStyleSheet("font: 36pt \"Arial Rounded MT Bold\";border-image: '';")
        self.gamenametext.setText("가위바위보 game")
        self.gamenametext.setAlignment(QtCore.Qt.AlignCenter)

        self.windowList = []
        for index in range(0, 1):
            tmpWindow = QtWidgets.QLineEdit(self.home)
            yPos= 450 + (50*index)
            tmpWindow.setGeometry(120, yPos, 220, 40)
            tmpWindow.setStyleSheet("border-image: '';")
            tmpWindow.setPlaceholderText("아이디")
            self.windowList.append(tmpWindow)

        self.pwWindow = QtWidgets.QLineEdit(self.home)
        self.pwWindow.setGeometry(120, 500, 220, 40)
        self.pwWindow.setStyleSheet("border-image: '';")
        self.pwWindow.setPlaceholderText("비밀번호")
        self.pwWindow.setEchoMode(2)

        self.findingidpwList = []
        self.nameList = ["아이디 찾기","비밀번호 찾기"]
        for index in range(0,2):
            findingBtn = QtWidgets.QPushButton(self.home)
            xPos = 120 + (110*index)
            findingBtn.setGeometry(xPos , 550, 101, 31)
            findingBtn.setStyleSheet("border-image: '';")
            self.findingidpwList.append(findingBtn)
            findingBtn.setText(self.nameList[index])

        self.loginmemberbtnList = []
        self.nameList=["Login","회원가입"]   #color: rgb(0, 85, 255);
        for index in range(0,2):
            loginmemberBtn = QtWidgets.QPushButton(self.home)
            yPos = 450 + (100*index)
            if index == 0:
                loginmemberBtn.setGeometry(350, yPos, 91, 91)
                loginmemberBtn.setStyleSheet("color: rgb(0, 85, 255);")
                loginmemberBtn.setStyleSheet("border-image: '';")
                loginmemberBtn.setText(self.nameList[index])
                self.loginmemberbtnList.append(loginmemberBtn)
            elif index == 1:
                loginmemberBtn.setGeometry(350, yPos, 91, 31)
                loginmemberBtn.setStyleSheet("border-image: '';")
                loginmemberBtn.setText(self.nameList[index])
                self.loginmemberbtnList.append(loginmemberBtn)


        self.stackedWidget.addWidget(self.home)
            
        #로그인 후 계정관리 게임하러 가기 선택 페이지
        self.manageAndgame = QtWidgets.QWidget()
        
        self.managegameList = []
        self.nameList = ["계정관리","게임하러 가기"]
        for index in range(0,2):
            managegameBtn = QtWidgets.QPushButton(self.manageAndgame)
            managegameBtn.setStyleSheet("background-color: rgb(52, 177, 200);font: 12pt \"맑은 고딕\";")
            xPos = 60 + (260*index)
            if index == 0:
                managegameBtn.setGeometry(xPos, 190, 151, 101)
                managegameBtn.setText(self.nameList[index])
                self.managegameList.append(managegameBtn)
            if index == 1:
                managegameBtn.setGeometry(xPos, 190, 151, 101)
                managegameBtn.setText(self.nameList[index])
                self.managegameList.append(managegameBtn)


        self.gobackbutton = QtWidgets.QPushButton(self.manageAndgame)
        self.gobackbutton.setGeometry(QtCore.QRect(400, 610, 93, 41))
        self.gobackbutton.setText("뒤로가기")

        self.stackedWidget.addWidget(self.manageAndgame)

        #계정관리 페이지
        self.managePage = QtWidgets.QWidget()


        self.existList = []
        for index in range(0,5):
            existInform = QtWidgets.QTextBrowser(self.managePage)
            existInform.setStyleSheet("background-color: rgb(251, 255, 224);")
            yPos = 90 + (70*index)
            existInform.setGeometry(50, yPos, 111, 51)
            self.existList.append(existInform)

        # self.existList = []
        # for index in range(0,5):
        #     existInform = QtWidgets.QLabel(self.managePage)
        #     yPos = 90 + (70*index)
        #     existInform.setGeometry(50, yPos, 111, 51)
        #     self.existList.append(existInform)
        #     self.existList[index].setPixmap(QtGui.QPixmap("homeimage.png"))

        self.updateList = []
        for index in range(0,5):
            updateInform = QtWidgets.QLineEdit(self.managePage)
            yPos = 90 + (70*index)
            updateInform.setGeometry(202, yPos, 151, 51)
            self.updateList.append(updateInform)

        self.updateBtnList = []
        self.nameList = ["아이디 수정","이름 수정","전화번호 수정","나이 수정","주소 수정"]
        for index in range(0,5):
            updateBtn = QtWidgets.QPushButton(self.managePage)
            yPos = 90 + (70*index)
            updateBtn.setGeometry(400, yPos, 93, 51)
            updateBtn.setText(self.nameList[index])
            self.updateBtnList.append(updateBtn)
            
        self.memberDeleteGoHomeList = []
        self.nameList = ["계정삭제","홈화면으로"]
        for index in range(0,2):
            memberDelateGohomeBtn = QtWidgets.QPushButton(self.managePage)
            xPos = 100 + (190*index)
            if index == 0:
                memberDelateGohomeBtn.setGeometry(xPos, 520, 201, 51)
                memberDelateGohomeBtn.setText(self.nameList[index])
                self.memberDeleteGoHomeList.append(memberDelateGohomeBtn)
            if index == 1:
                memberDelateGohomeBtn.setGeometry(xPos, 520, 93, 51)
                memberDelateGohomeBtn.setText(self.nameList[index])
                self.memberDeleteGoHomeList.append(memberDelateGohomeBtn)

        self.stackedWidget.addWidget(self.managePage)

        #아이디 찾는 페이지
        self.idfinding = QtWidgets.QWidget()
        self.namephoneList = []
        for index in range(0,2):
            namephoneWindow = QtWidgets.QLineEdit(self.idfinding)
            yPos = 110 + (100*index)
            namephoneWindow.setGeometry(80, yPos, 221, 41)
            self.namephoneList.append(namephoneWindow)
        
        self.namephoneLabelList = []
        self.nameList = ["이름","전화번호"]
        for index in range(0,2):
            namephoneLabel = QtWidgets.QLabel(self.idfinding)
            namephoneLabel.setStyleSheet("font: 15pt \"맑은 고딕\";")
            yPos = 70+(100*index)
            if index == 0:
                namephoneLabel.setGeometry(80, yPos, 51, 31)
                namephoneLabel.setText(self.nameList[index])
                self.namephoneLabelList.append(namephoneLabel)
            if index == 1:
                namephoneLabel.setGeometry(80, yPos, 91, 31)
                namephoneLabel.setText(self.nameList[index])
                self.namephoneLabelList.append(namephoneLabel)

        self.nextpushbutton = QtWidgets.QPushButton(self.idfinding)
        self.nextpushbutton.setGeometry(QtCore.QRect(80, 270, 141, 41))
        self.nextpushbutton.setStyleSheet("font: 14pt \"한컴 고딕\";")
        self.nextpushbutton.setText("다음")

        self.gobackbutton2 = QtWidgets.QPushButton(self.idfinding)
        self.gobackbutton2.setGeometry(QtCore.QRect(400, 610, 93, 41))
        self.gobackbutton2.setText("뒤로가기")

        self.idfindlabel = QtWidgets.QLabel(self.idfinding)
        self.idfindlabel.setGeometry(QtCore.QRect(430, 20, 91, 21))
        self.idfindlabel.setStyleSheet("font: 10pt \"나눔고딕\";")
        self.idfindlabel.setText("아이디 찾기")

        self.stackedWidget.addWidget(self.idfinding)

        #아이디알려주는 페이지
        self.idprint = QtWidgets.QWidget()
        self.idlistlabel = QtWidgets.QLabel(self.idprint)
        self.idlistlabel.setGeometry(QtCore.QRect(80, 20, 391, 31))
        self.idlistlabel.setStyleSheet("font: 9pt \"맑은 고딕\";")
        self.idlistlabel.setText("고객님의 정보와 일치하는 ID 목록입니다.")

        self.idrealprintlabel = QtWidgets.QTextBrowser(self.idprint)
        self.idrealprintlabel.setGeometry(QtCore.QRect(150, 90, 211, 31))
        self.idrealprintlabel.setStyleSheet("background-color: rgb(251, 255, 224);")

        self.idprintlabel = QtWidgets.QLabel(self.idprint)
        self.idprintlabel.setGeometry(QtCore.QRect(430, 80, 91, 21))
        self.idprintlabel.setStyleSheet("font: 10pt \"나눔고딕\";")
        self.idprintlabel.setText("아이디 출력")

        self.gohomepushbutton = QtWidgets.QPushButton(self.idprint)
        self.gohomepushbutton.setGeometry(QtCore.QRect(150, 160, 211, 41))
        self.gohomepushbutton.setStyleSheet("font: 14pt \"한컴 고딕\";")
        self.gohomepushbutton.setText("홈화면으로 돌아가기")

        self.stackedWidget.addWidget(self.idprint)

        #비밀번호 찾기 페이지
        self.pwfinding = QtWidgets.QWidget()

        self.idphoneLabelList = []
        self.nameList = ["아이디","전화번호"]
        for index in range(0,2):
            idphoneLabel = QtWidgets.QLabel(self.pwfinding)
            yPos = 70+(100*index)
            if index == 0:
                idphoneLabel.setGeometry(80, yPos, 51, 31)
                idphoneLabel.setStyleSheet("font: 9pt \"맑은 고딕\";")
                idphoneLabel.setText(self.nameList[index])
                self.idphoneLabelList.append(idphoneLabel)
            if index == 1:
                idphoneLabel.setGeometry(80, yPos, 91, 31)
                idphoneLabel.setStyleSheet("font: 9pt \"맑은 고딕\";")
                idphoneLabel.setText(self.nameList[index])
                self.idphoneLabelList.append(idphoneLabel)

        self.idphoneList = []
        for index in range(0,2):
            idphoneWindow = QtWidgets.QLineEdit(self.pwfinding)
            yPos = 110 + (100*index)
            idphoneWindow.setGeometry(80, yPos, 221, 41)
            self.idphoneList.append(idphoneWindow)

        self.nextpushbutton2 = QtWidgets.QPushButton(self.pwfinding)
        self.nextpushbutton2.setGeometry(QtCore.QRect(80, 270, 141, 41))
        self.nextpushbutton2.setStyleSheet("font: 14pt \"한컴 고딕\";")
        self.nextpushbutton2.setText("다음")

        self.gobackbutton3 = QtWidgets.QPushButton(self.pwfinding)
        self.gobackbutton3.setGeometry(QtCore.QRect(400, 610, 93, 41))
        self.gobackbutton3.setText("뒤로가기")

        self.idfindlabel = QtWidgets.QLabel(self.pwfinding)
        self.idfindlabel.setGeometry(QtCore.QRect(430, 20, 91, 21))
        self.idfindlabel.setStyleSheet("font: 10pt \"나눔고딕\";")
        self.idfindlabel.setText("비밀번호 찾기")
        
        self.stackedWidget.addWidget(self.pwfinding)

        #새로운 비밀번호 만드는 페이지
        self.newpw = QtWidgets.QWidget()

        self.newpwlabel = QtWidgets.QLabel(self.newpw)
        self.newpwlabel.setGeometry(QtCore.QRect(390, 20, 131, 21))
        self.newpwlabel.setStyleSheet("font: 10pt \"나눔고딕\";")
        self.newpwlabel.setText("새로운 비밀번호")
        
        self.newpwinputlabel = QtWidgets.QLabel(self.newpw)
        self.newpwinputlabel.setGeometry(QtCore.QRect(90, 40, 351, 31))
        self.newpwinputlabel.setStyleSheet("font: 9pt \"맑은 고딕\";")
        self.newpwinputlabel.setText("새로운 PW를 입력하세요.")
        
        self.newpwrealinputlabel = QtWidgets.QLineEdit(self.newpw)
        self.newpwrealinputlabel.setGeometry(QtCore.QRect(160, 110, 211, 31))
        self.newpwrealinputlabel.setStyleSheet("background-color: rgb(251, 255, 224);\n"
        "")
        self.newpwrealinputlabel.setEchoMode(2)

        self.pwconfirmpushbutton = QtWidgets.QPushButton(self.newpw)
        self.pwconfirmpushbutton.setGeometry(QtCore.QRect(190, 170, 141, 41))
        self.pwconfirmpushbutton.setStyleSheet("font: 14pt \"한컴 고딕\";")
        self.pwconfirmpushbutton.setText("확인")

        self.stackedWidget.addWidget(self.newpw)

        #회원가입 페이지
        self.membership = QtWidgets.QWidget()

        self.membershiplabel = QtWidgets.QLabel(self.membership)
        self.membershiplabel.setGeometry(QtCore.QRect(460, 20, 64, 21))
        self.membershiplabel.setStyleSheet("font: 10pt \"나눔고딕\";")
        self.membershiplabel.setText("회원가입")

        nameList = ["아이디","비밀번호","이름","휴대전화","나이","주소"]
        for index in range(0,6):
            membershipLabel = QtWidgets.QLabel(self.membership)
            yPos = 40 + (90*index)
            membershipLabel.setGeometry(30, yPos, 91, 31)
            membershipLabel.setText(nameList[index])

        self.membershipList = []
        for index in range(0,6):
            memberinputLabel = QtWidgets.QLineEdit(self.membership)
            yPos = 80 + (90*index)
            memberinputLabel.setGeometry(30, yPos, 241, 41)
            self.membershipList.append(memberinputLabel)

        self.pwlist = QtWidgets.QLineEdit(self.membership)
        self.pwlist.setGeometry(30,170,241,41)
        self.pwlist.setEchoMode(2)

        self.membershipmakepushbutton = QtWidgets.QPushButton(self.membership)
        self.membershipmakepushbutton.setGeometry(QtCore.QRect(30, 590, 270, 41))
        self.membershipmakepushbutton.setStyleSheet("font: 14pt \"한컴 고딕\";")
        self.membershipmakepushbutton.setText("가입하기")

        self.idoverlapconfirm = QtWidgets.QPushButton(self.membership)
        self.idoverlapconfirm.setGeometry(QtCore.QRect(280, 80, 111, 41))
        self.idoverlapconfirm.setStyleSheet("font: 9pt \"맑은 고딕\";")
        self.idoverlapconfirm.setText("아이디 중복확인")

        self.gobackbutton4 = QtWidgets.QPushButton(self.membership)
        self.gobackbutton4.setGeometry(QtCore.QRect(400, 590, 93, 41))
        self.gobackbutton4.setText("뒤로 가기")

        self.stackedWidget.addWidget(self.membership)

        #게임 페이지

        self.gamepage = QtWidgets.QWidget()

        nameList = ["가위","바위","보"]
        for index in range(0,3):
            gameLabel = QtWidgets.QLabel(self.gamepage)
            gameLabel.setAlignment(QtCore.Qt.AlignCenter)
            gameLabel.setStyleSheet("font: 24pt \"나눔 고딕\";")
            xPos = 56 + (162*index)
            gameLabel.setGeometry(xPos, 230, 91, 41)
            gameLabel.setText(nameList[index])

        self.gameList = []
        for index in range(0,3):
            gameBtn = QtWidgets.QPushButton(self.gamepage)
            xPos = 30 + (160*index)
            gameBtn.setGeometry(xPos, 290, 141, 141)
            self.gameList.append(gameBtn)

        self.result = []
        for index in range(0,2):
            result = QtWidgets.QTextBrowser(self.gamepage)
            result.setStyleSheet("background-color: rgb(251, 255, 224);font: 25pt \"한컴 고딕\";")
            yPos = 40 + (440*index)
            result.setGeometry(180,yPos,161,141)
            self.result.append(result)
        
        self.gobackbutton5 = QtWidgets.QPushButton(self.gamepage)
        self.gobackbutton5.setGeometry(30, 580, 93, 41)
        self.gobackbutton5.setText("뒤로 가기")

        self.gameoverbutton = QtWidgets.QPushButton(self.gamepage)
        self.gameoverbutton.setGeometry(420, 550, 93, 71)
        self.gameoverbutton.setStyleSheet(
            "background-color: rgb(225,124,48);font: 10pt \"맑은 고딕\";"
        )
        self.gameoverbutton.setText("게임종료")

        self.stackedWidget.addWidget(self.gamepage)
        # self.stackedWidget.setCurrentIndex(self.setpage)
        self.mainWindow.show()




