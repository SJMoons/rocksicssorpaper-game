#아이디 비밀번호 찾기, 당신은 로봇입니까? 보안숫자 입력 로그인실패시 다시 로그인

import time
import sqlite3

class MyDb:
    def __init__(self):
        self.conn = None
        self.cur = None
        self.initDatabase()

    def initDatabase(self):
        self.conn = sqlite3.connect("test.db")
        self.cur = self.conn.cursor()

    def create(self, table, column, data):    # 테이블명 (string) / 컬럼명 (list) / 값 (list)
        self.sql = "INSERT INTO " + table + "("
        for index in range(0, len(column)):
            self.sql += column[index]
            if index < len(column)-1:
                self.sql += ", "
        self.sql += ")"
        # INSERT INTO user (id, pw)
        self.sql += "VALUES("
        for index in range(0, len(column)):
            self.sql += "'" + data[index] + "'"
            if index < len(column)-1:
                self.sql += ", "
        self.sql += ");"
        self.cur.execute(self.sql)
        self.conn.commit()
        # VALUES('" + id + "', '" + pw + "');

    def delete(self, table,  column, data):
        self.sql = "DELETE FROM "+ table + " WHERE "
        for index in range(0, len(column)):
            self.sql += column[index]
            if index < len(column)-1:
                self.sql += ", "
        # self.sql += ""

        self.sql += "="
        for index in range(0, len(column)):
            self.sql += "'" + data[index] + "'"
            if index < len(column)-1:
                self.sql += ", "
        self.sql += ";"
        self.cur.execute(self.sql)
        self.conn.commit()
    
    def read(self, table, column, data):
        self.sql = "SELECT" + " * " + "FROM " + table + " WHERE("
        for index in range(0,len(column)):
            self.sql += column[index]
            if index < len(column)-1:
                self.sql += ", "
        self.sql += ") = " + "("
        for index in range(0, len(column)):
            self.sql += "'" + data[index] + "'"
            if index < len(column)-1:
                self.sql += ", "
        self.sql += ");"
        self.cur.execute(self.sql)
        result = self.cur.fetchall()
        return result

    # 테이블명 / 컬럼 / 컬럼에 대한 데이터 순으로


    def update(self, table, column, data, column2, data2):
        self.sql = "UPDATE " + table + " SET " 
        for index in range(0,len(column)):
            self.sql += "" + column[index] + "" +"="
            if index < len(column)-1:
                self.sql += ", "

        for index in range(0,len(column)):
            self.sql += "'" + data[index] + "'"
            if index < len(column)-1:
                self.sql += ", "
        self.sql += " "
        self.sql += "WHERE "

        for index in range(0, len(column2)):
            self.sql += "" + column2[index] + "" + "="
            if index < len(column2)-1:
                self.sql += ", "

        for index in range(0, len(column2)):
            self.sql += "'" + data2[index] + "'"
            if index < len(column2)-1:
                self.sql += ", "
        self.sql += ";"
        self.cur.execute(self.sql)
        self.conn.commit()

    #함수 4개 crud /매개변수3개씩 테이블명, 리스트(컬럼), 컬럼에 대한 값
    #빈 리스트를 만들어놓고 필요한 컬럼값에 매개변수를 넣어본다
    #출력은 프로그램 흐름을 관장하는 클래스로...
    #서로다른 테이블을 연결해줘야됨, ex)회원가입 테이블에 아이디 넣어주기
    #무한반복으로 바꿔주기, 회원가입테이블에 아이디 추가

