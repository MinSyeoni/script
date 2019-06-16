import urllib
import http.client
from tkinter import *
from tkinter import font
import folium
from xml.etree import ElementTree
import tkinter.messagebox
from xml.etree.ElementTree import parse
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt #그래프
import numpy as np
import matplotlib.font_manager as fm
import mimetypes
import smtplib
import smtplib, os, pickle  # smtplib: 메일 전송을 위한 패키지
from email import encoders  # 파일전송을 할 때 이미지나 문서 동영상 등의 파일을 문자열로 변환할 때 사용할 패키지
from email.mime.text import MIMEText   # 본문내용을 전송할 때 사용되는 모듈
from email.mime.multipart import MIMEMultipart   # 메시지를 보낼 때 메시지에 대한 모듈
from email.mime.base import MIMEBase
from http.client import HTTPSConnection
from http.server import BaseHTTPRequestHandler, HTTPServer
import tkinter.messagebox
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from io import BytesIO
import urllib.request
import urllib.parse

#페이지 수정필요


class Hospital:
    def __init__(self):
        self.g_Tk = Tk()
        self.g_Tk.geometry("1000x700+850+500")

        self.InitTopText()
        self.initVariable()
        self.setXML()
        self.initInterface()



        self.g_Tk.mainloop()
    def initVariable(self):
        self.page = 1
        self.name = ""
        self.area = ""
        self.type=""
        self.x=0
        self.y=0
        self.onText = FALSE



    def initInterface(self):
        self.InitInputCityLabel()
        self.InitInputnameLabel()
        self.SearchListBox()
        self.InitSearchButton2()
        self.InitGmailButton()
        self.nextButton()
        self.backButton()
        self.InitSearchButton()
        #self.GraphButton()
        self.InitRenderListText()

    def InitTopText(self):
        self.TempFont = font.Font(self.g_Tk,size=17,weight='bold',family='Consolas')
        self.searchFont = font.Font(self.g_Tk, size=11,family='Consolas')
        self.MainText = Label(self.g_Tk,font = self.TempFont,text="< 병원정보서비스 App >")
        #self.cityText = Label(self.g_Tk,font = self.searchFont,text="시/도")
        #self.townText = Label(self.g_Tk, font=self.searchFont, text="이름")
        self.listText = Label(self.g_Tk, font=self.searchFont, text="[ 병원 리스트 ]")
        self.graphText = Label(self.g_Tk, font=self.searchFont, text="[ 지역별 병원 그래프 ]")
        #글자들 위치
        self.MainText.place(x=90)
        #self.cityText.place(x=30,y=40)
        #self.townText.place(x=170,y=40)
        self.listText.place(x=35,y=115)
        self.graphText.place(x=10,y=370)

    def InitInputCityLabel(self):  # 같은 도내 병원타입 검색을 위한 시도 입력창
        self.TempFont = font.Font(self.g_Tk,size=15,family='Consolas')
        self.areaEntry=StringVar()
        self.InputLabel = Entry(self.g_Tk,textvariable=self.areaEntry,font=self.TempFont,width=7,borderwidth=2,relief='ridge')
        self.InputLabel.pack()
        self.InputLabel.place(x=10,y=65)

    def InitInputnameLabel(self):#지도 검색을 위한 이름입력창
        self.TempFont = font.Font(self.g_Tk,size=15,family='Consolas')
        self.nameEntry=StringVar()
        self.InputLabel = Entry(self.g_Tk,textvariable=self.nameEntry,font=self.TempFont,width=7,borderwidth=2,relief='ridge')
        self.InputLabel.pack()
        self.InputLabel.place(x=100,y=65)

    def nextButton(self):
        self.tempFont = font.Font(self.g_Tk, size=10, family='Consolas')
        self.nextButton = Button(self.g_Tk, font=self.tempFont,  text=">", command=self.setNext)
        self.nextButton.pack()
        self.nextButton.place(x=150, y=115)

    def backButton(self):
        self.tempFont = font.Font(self.g_Tk, size=10, family='Consolas')
        self.nextButton = Button(self.g_Tk, font=self.tempFont,  text="<", command=self.setBack)
        self.nextButton.pack()
        self.nextButton.place(x=10, y=115)

    #def GraphButton(self): #그래프 생성 버튼
    #    self.TempFont = font.Font(self.g_Tk, size=11,family='Consolas')
    #    self.renderStickGraphButton = Button(self.g_Tk,font=self.TempFont,text="그래프 생성",command=self.renderStickGraph)
    #    self.renderStickGraphButton.pack()
    #    self.renderStickGraphButton.place(x=160,y=365)


    def InitInputTownLabel(self): #이름 검색라벨로 변경
        self.TempFont = font.Font(self.g_Tk,size=20,family='Consolas')
        self.nameEntry=StringVar()
        self.InputLabel = Entry(self.g_Tk, textvariable=self.nameEntry, font=self.TempFont,width=7,borderwidth=2,relief='ridge')
        self.InputLabel.pack()
        self.InputLabel.place(x=700,y=265)


    def InitSearchButton2(self): # 검색버튼
        self.TempFont = font.Font(self.g_Tk, size=11,family='Consolas')
        self.SearchButton = Button(self.g_Tk,font=self.TempFont,text="검색",command=self.SearchButtonAction)
        self.SearchButton.pack()
        self.SearchButton.place(x=400,y=65)

    def InitSearchButton(self): # 지도버튼
        self.TempFont = font.Font(self.g_Tk, size=11,family='Consolas')
        self.SearchButton = Button(self.g_Tk,font=self.TempFont,text="지도",command=self.map)
        self.SearchButton.pack()
        self.SearchButton.place(x=300,y=65)

    def SearchListBox(self):
        self.TempFont = font.Font(self.g_Tk, size=17, weight='bold', family='Consolas')
        self.ListboxScrollbar=Scrollbar(self.g_Tk)
        self.ListboxScrollbar.pack()
        self.ListboxScrollbar.place(x=150,y=50)

        self.SearchBox=Listbox(self.g_Tk,font=self.TempFont,activestyle='none',
                                width=20,height=2,borderwidth=12,relief='ridge',
                                yscrollcommand=self.ListboxScrollbar.set)
        self.SearchBox.insert(0, "    ")
        self.SearchBox.insert(1,"병원")
        self.SearchBox.insert(2, "의원")
        self.SearchBox.insert(3, "요양병원")
        self.SearchBox.insert(4, "한방병원")
        self.SearchBox.insert(5, "한의원")
        self.SearchBox.insert(6, "기타")
        self.SearchBox.insert(7, "치과병원")
        self.SearchBox.insert(8, "치과의원")
        self.SearchBox.insert(9, "보건소")
        self.SearchBox.insert(10, "종합병원")
        self.SearchBox.insert(11, "    ")
        self.typeEntry = self.SearchBox.activate(1)
        self.SearchBox.pack()
        self.SearchBox.place(x=600,y=100)
        self.ListboxScrollbar.config(command=self.SearchBox.yview)

    def SearchButtonAction(self):
        self.RenderText.configure(state="normal")
        self.RenderText.delete(0.0, END)
        self.iSearchIndex = self.SearchBox.curselection()[0]
        if self.iSearchIndex == 0:
            self.SearchListBox()
        elif self.iSearchIndex == 1:
            self.SearchHospital1()
        elif self.iSearchIndex == 2:
            self.SearchHospital2()
        elif self.iSearchIndex == 3:
            self.SearchHospital3()
        elif self.iSearchIndex == 4:
            self.SearchHospital4()
        elif self.iSearchIndex == 5:
            self.SearchHospital5()
        elif self.iSearchIndex == 6:
            self.SearchHospital6()
        elif self.iSearchIndex == 7:
            self.SearchHospital7()
        elif self.iSearchIndex == 8:
            self.SearchHospital8()
        elif self.iSearchIndex == 9:
            self.SearchHospital9()
        elif self.iSearchIndex == 10:
            self.SearchHospital10()
        elif self.iSearchIndex == 11:
            self.SearchListBox()
        self.RenderText.configure(state="disabled")

    def SearchHospital1(self):
        self.type="B"
        self.area = self.areaEntry.get()
        self.setXML()
        self.printAll()
    def SearchHospital2(self):
        self.type="C"
        self.area = self.areaEntry.get()
        self.setXML()
        self.printAll()
        return self.type
    def SearchHospital3(self):
        self.type="D"
        self.area = self.areaEntry.get()
        self.setXML()
        self.printAll()
        return self.type
    def SearchHospital4(self):
        self.type="E"
        self.area = self.areaEntry.get()
        self.setXML()
        self.printAll()
        return self.type
    def SearchHospital5(self):
        self.type="G"
        self.area = self.areaEntry.get()
        self.setXML()
        self.printAll()
        return self.type
    def SearchHospital7(self):
        self.type="H"
        self.area = self.areaEntry.get()
        self.setXML()
        self.printAll()
        return self.type
    def SearchHospital6(self):
        self.type="I"
        self.area = self.areaEntry.get()
        self.setXML()
        self.printAll()
        return self.type

    def SearchHospital7(self):
        self.type = "M"
        self.area = self.areaEntry.get()
        self.setXML()
        self.printAll()

    def SearchHospital8(self):
        self.type = "N"
        self.area = self.areaEntry.get()
        self.setXML()
        self.printAll()
    def SearchHospital9(self):
        self.type = "R"
        self.area = self.areaEntry.get()
        self.setXML()
        self.printAll()
    def SearchHospital10(self):
        self.type = "A"
        self.area = self.areaEntry.get()
        self.setXML()
        self.printAll()


    def InitGmailButton(self): #지메일 버튼
        self.TempFont = font.Font(self.g_Tk, size=11,family='Consolas')
        self.SearchButton = Button(self.g_Tk,font=self.TempFont,text="G-mail",command=self.sendMain)
        self.SearchButton.pack()
        self.SearchButton.place(x=330,y=65)

    def InitRenderListText(self): #병원 리스트 틀
        self.frame = Frame(self.g_Tk)
        self.frame.place(x=10,y=145)
        self.RenderTextScrollbar = Scrollbar(self.frame) #스크롤바
        self.RenderTextScrollbar.pack(side=RIGHT,fill=Y)
        #TempFont = font.Font(self.g_Tk,size=10,family='Consolas')
        #리스트박스
        self.RenderText = Text(self.frame,width=53,height=16,borderwidth=2,relief='ridge',yscrollcommand=self.RenderTextScrollbar.set)
        self.RenderText.pack()
        self.RenderTextScrollbar.config(command=self.RenderText.yview)
        #self.RenderTextScrollbar.pack(side=RIGHT,fill=BOTH)
        #self.RenderText.configure(state='disabled')




    #데이터 값 지정
    def setXML(self): #시도,이름 검색 시 xmlset
        self.url="http://apis.data.go.kr/B552657/HsptlAsembySearchService/getHsptlMdcncListInfoInqire?serviceKey=9Y0EzZk6MfXyi1eqXZje8fT1ff5xBnYcTohB2nMJOEWdUAM7cASbKYdJjW1ZjOaZ5ddX1fSFG%2BPKHc16GrmaOw%3D%3D" \
                 + "&Q0=" + urllib.parse.quote_plus(self.area) + "&QZ=" + urllib.parse.quote_plus(self.type) + "&pageNo=" + str(self.page) + "&numOfRows=10"
        self.tree = ET.ElementTree(file=urllib.request.urlopen(self.url))
        self.tree.write("DATA_Q.xml",encoding="utf-8")
        self.data=self.tree.getroot()
        print(self.page)
        print(self.data)
        self.doc=parse("DATA_Q.xml")
        print(self.doc)
        self.root=self.doc.getroot()
        print(self.root)


    def setNext(self):
        self.page += 1
        self.setXML()
        self.printAll()
        print("아")
    def setBack(self):
        self.page -= 1
        self.setXML()
        self.printAll()
        print()
        print("아")

    def sendMain(self):#추후 이메일 내용 추가
        self.name = self.nameEntry.get()
        self.area = self.areaEntry.get()
        self.setXML2(self.name, self.area)
        for item in self.root.iter("item"):
            self.Addr = item.findtext("dutyAddr")
            self.dutyDivNam = item.findtext("dutyDivNam")
            self.dutyName=item.findtext("dutyName")

        self.host = "smtp.gmail.com"  # Gmail STMP 서버 주소.
        self.port = "587"
        self.senderAddr = "py6646@naver.com"  # 보내는 사람 email 주소.
        self.recipientAddr = "py6646@gmail.com"  # 받는 사람 email 주소.
        #self.html=self.RenderText
        self.msg = MIMEMultipart('alternative')
        self.msg['Subject'] = "병원 정보"
        self.msg['From'] = self.senderAddr
        self.msg['To'] = self.recipientAddr
        self.dataStr="이름 : "+self.dutyName+'\n'+"병원타입 : "+self.dutyDivNam+'\n'+"병원 주소 : "+self.Addr+'\n'+"지도로 검색한 상세정보입니다."
        self.part=MIMEText(self.dataStr)
        self.msg.attach(self.part)
        #self.part_html=MIMEText(self.html,'html',_charset='UTF-8')
        #self.msg.attach(self.part_html)
        #self.part2=MIMEText(self.root)
        #self.msg.attach(self.part2)
        # 메일을 발송한다.
        self.s = smtplib.SMTP(self.host, self.port)
        # s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
        self.s.ehlo()
        self.s.starttls()
        self.s.ehlo()
        self.s.login("py6646@gmail.com", "py122134tkddn!")
        self.s.sendmail(self.senderAddr, [self.recipientAddr], self.msg.as_string())
        self.s.close()
        #tkinter.messagebox.showinfo("g-mail","전송완료!")

    def map(self):
        self.name=self.nameEntry.get()
        self.area=self.areaEntry.get()
        self.setXML2(self.name,self.area)
        for item in self.root.iter("item"):
            self.x = item.findtext("wgs84Lat")
            self.y = item.findtext("wgs84Lon")
            print(self.x)
            print(self.y)
        print(self.name)
        print(self.area)
        self.map_osm=folium.Map(location=[self.x,self.y],zoom_start=15)
        folium.Marker([self.x,self.y], popup=self.name).add_to(self.map_osm)
        self.map_osm.save('osm.html')

    def setXML2(self, name,area):
        print(name)
        print(area)
        self.url = "http://apis.data.go.kr/B552657/HsptlAsembySearchService/getHsptlMdcncListInfoInqire?serviceKey=9Y0EzZk6MfXyi1eqXZje8fT1ff5xBnYcTohB2nMJOEWdUAM7cASbKYdJjW1ZjOaZ5ddX1fSFG%2BPKHc16GrmaOw%3D%3D" \
                 + "&Q0=" + urllib.parse.quote_plus(self.area)+ "&QN=" + urllib.parse.quote_plus(name)+ "&pageNo=1&numOfRows=10"
        self.tree = ET.ElementTree(file=urllib.request.urlopen(self.url))
        self.tree.write("DATA_Q.xml", encoding="utf-8")
        self.data = self.tree.getroot()

        self.doc = parse("DATA_Q.xml")
        self.root = self.doc.getroot()



    def printAll(self): #검색에 따른 xml 출력

        for item in self.root.iter("item"):
            self.RenderText.insert(INSERT,"\n[",INSERT,item.findtext("dutyDivNam"),INSERT,"]",INSERT,item.findtext("dutyAddr"))
            self.RenderText.insert(INSERT, chr(10))
            self.RenderText.insert(INSERT, "병원 이름: ",INSERT,item.findtext("dutyName"),INSERT)
            self.RenderText.insert(INSERT, chr(10))



Hospital()
