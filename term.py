import urllib
import http.client
from tkinter import *
from tkinter import font
import tkinter.ttk
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
#import spam

from io import BytesIO
import urllib.request
import urllib.parse


class Hospital:
    def __init__(self):
        self.g_Tk = Tk()
        self.g_Tk.geometry("1000x700+850+500")
        self.g_Tk.resizable(False, False)
        self.image = PhotoImage(file = "background.png") #배경이미지
        self.label = Label(self.g_Tk,image = self.image)
        self.label.pack()
        self.InitTopText()
        self.initVariable()
        self.setXML("","",1)
        self.setXML2("","")
        self.setXML3("","")
        self.setXML4()

        self.initInterface()

        self.g_Tk.mainloop()
    def initVariable(self):
        self.page = 1
        self.name = ""
        self.area = ""
        self.type= ""
        self.items=[]
        self.onText = FALSE
        self.hospital=[]
        self.dateStart=''
        self.dataEnd=''


        #그래프 관련 변수

        #self.member.reverse()
        #self.count.reverse()

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
        self.searchFont = font.Font(self.g_Tk, size=14,family='Consolas')
        self.search2Font = font.Font(self.g_Tk, size=12, family='Consolas')
        #self.MainText = Label(self.g_Tk,font = self.TempFont,text="< 병원정보서비스 App >")
        self.typeText = Label(self.g_Tk, font=self.search2Font, text="종류 선택")
        self.cityText = Label(self.g_Tk,font = self.search2Font,text="시/도 입력")
        self.townText = Label(self.g_Tk, font=self.search2Font, text="이름 입력")
        self.searchText = Label(self.g_Tk, font=self.search2Font, text="click!")
        self.listText = Label(self.g_Tk, font=self.searchFont, text="[ 병원 리스트 ]")
        self.graphText = Label(self.g_Tk, font=self.searchFont, text="[ 지역별 병원 그래프 ]")
        #글자들 위치
        #self.MainText.place(x=90)
        self.typeText.place(x=70, y=290)
        self.cityText.place(x=195,y=290)
        self.townText.place(x=295,y=290)
        self.searchText.place(x=385, y=290)
        self.listText.place(x=75,y=400)
        self.graphText.place(x=630,y=400)

    def InitInputCityLabel(self):  # 같은 도내 병원타입 검색을 위한 시도 입력창
        self.TempFont = font.Font(self.g_Tk,size=16,family='Consolas')
        self.areaEntry=StringVar()
        self.InputLabel = Entry(self.g_Tk,textvariable=self.areaEntry,font=self.TempFont,width=7,borderwidth=2,relief='ridge')
        self.InputLabel.pack()
        self.InputLabel.place(x=190,y=330)

    def InitInputnameLabel(self):#지도 검색을 위한 이름입력창
        self.TempFont = font.Font(self.g_Tk,size=16,family='Consolas')
        self.nameEntry=StringVar()
        self.InputLabel = Entry(self.g_Tk,textvariable=self.nameEntry,font=self.TempFont,width=7,borderwidth=2,relief='ridge')
        self.InputLabel.pack()
        self.InputLabel.place(x=285,y=330)

    #def GraphButton(self): #그래프 생성 버튼
        #self.TempFont = font.Font(self.g_Tk, size=11,family='Consolas')
        #self.renderStickGraphButton = Button(self.g_Tk,font=self.TempFont,text="그래프 생성",command=self.clean)
        #self.renderStickGraphButton.pack()
        #self.renderStickGraphButton.place(x=160,y=365)

    def nextButton(self):
        self.tempFont = font.Font(self.g_Tk, size=10, family='Consolas')
        self.nextButton = Button(self.g_Tk, font=self.tempFont,  text=">", command=self.setNext)
        self.nextButton.pack()
        self.nextButton.place(x=205, y=400)

    def backButton(self):
        self.tempFont = font.Font(self.g_Tk, size=10, family='Consolas')
        self.nextButton = Button(self.g_Tk, font=self.tempFont,  text="<", command=self.setBack)
        self.nextButton.pack()
        self.nextButton.place(x=50, y=400)

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
        self.SearchButton = Button(self.g_Tk,font=self.TempFont,text="",command=self.SearchButtonAction)
        self.SearchButton.pack()
        self.buttonImage = PhotoImage(file = "search.png")
        self.SearchButton.config(image=self.buttonImage,compound=RIGHT)
        self.SearchButton.place(x=400,y=325)

    def InitSearchButton(self): # 지도버튼
        self.TempFont = font.Font(self.g_Tk, size=11,family='Consolas')
        self.SearchButton = Button(self.g_Tk,font=self.TempFont,text=" 지도 ",command=self.map)
        self.SearchButton.pack()
        self.mapImage = PhotoImage(file = "map.png")
        self.SearchButton.config(image=self.mapImage,compound=RIGHT)
        self.SearchButton.place(x=235,y=395)

    def SearchListBox(self):
        self.TempFont = font.Font(self.g_Tk, size=14, family='Consolas') # weight='bold' 삭제
        self.ListboxScrollbar=Scrollbar(self.g_Tk)
        self.ListboxScrollbar.pack()
        self.ListboxScrollbar.place(x=155,y=320)

        self.SearchBox=Listbox(self.g_Tk,font=self.TempFont,activestyle='none',
                                width=10,height=2,borderwidth=2,relief='ridge',
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
        self.typwEntry2 = StringVar()
        self.SearchBox.pack()
        self.SearchBox.place(x=50,y=320)
        self.ListboxScrollbar.config(command=self.SearchBox.yview)

    def SearchButtonAction(self):

        self.graphview()

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


    def SearchHospital1(self):
        type="B"
        page=1
        area = self.areaEntry.get()
        self.setXML(area,type,page)
        self.printAll()
    def SearchHospital2(self):
        type="C"
        page = 1
        area = self.areaEntry.get()
        self.setXML(area, type, page)
        self.printAll()
    def SearchHospital3(self):
        type="D"
        page = 1
        area = self.areaEntry.get()
        self.setXML(area, type, page)
        self.printAll()
    def SearchHospital4(self):
        type="E"
        page = 1
        area = self.areaEntry.get()
        self.setXML(area, type, page)
        self.printAll()
    def SearchHospital5(self):
        type="G"
        page = 1
        area = self.areaEntry.get()
        self.setXML(area, type, page)
        self.printAll()

    def SearchHospital6(self):
        type="I"
        page = 1
        area = self.areaEntry.get()
        self.setXML(area, type, page)
        self.printAll()

    def SearchHospital7(self):
        type = "M"
        page = 1
        area = self.areaEntry.get()
        self.setXML(area, type, page)
        self.printAll()

    def SearchHospital8(self):
        type = "N"
        page = 1
        area = self.areaEntry.get()
        self.setXML(area, type, page)
        self.printAll()
    def SearchHospital9(self):
        type = "R"
        page = 1
        area = self.areaEntry.get()
        self.setXML(area, type, page)
        self.printAll()
    def SearchHospital10(self):
        type = "A"
        page = 1
        area = self.areaEntry.get()
        self.setXML(area, type, page)
        self.printAll()

    def InitGmailButton(self): #지메일 버튼
        self.TempFont = font.Font(self.g_Tk, size=11,family='Consolas')
        self.SearchButton = Button(self.g_Tk,font=self.TempFont,text=" G-mail ",command=self.sendMain)
        self.SearchButton.pack()
        self.gmailImage = PhotoImage(file = "gmail.png")
        self.SearchButton.config(image=self.gmailImage,compound=RIGHT)
        self.SearchButton.place(x=330,y=395)

    def InitRenderListText(self): #병원 리스트 틀
        self.frame = Frame(self.g_Tk)
        self.frame.place(x=50,y=450)
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
    def setXML(self,area,type,page): #시도,이름 검색 시 xmlset
        self.url="http://apis.data.go.kr/B552657/HsptlAsembySearchService/getHsptlMdcncListInfoInqire?serviceKey=9Y0EzZk6MfXyi1eqXZje8fT1ff5xBnYcTohB2nMJOEWdUAM7cASbKYdJjW1ZjOaZ5ddX1fSFG%2BPKHc16GrmaOw%3D%3D" \
                 + "&Q0=" + urllib.parse.quote_plus(area) + "&QZ=" + urllib.parse.quote_plus(type) + "&pageNo=" + str(page) + "&numOfRows=10"
        self.tree = ET.ElementTree(file=urllib.request.urlopen(self.url))
        self.tree.write("DATA_Q.xml",encoding="utf-8")
        self.data=self.tree.getroot()
        self.doc=parse("DATA_Q.xml")
        self.root=self.doc.getroot()

    def setNext(self):
        self.page += 1
        area=self.areaEntry.get()
        type=self.typwEntry2.get()
        self.iSearchIndex = self.SearchBox.curselection()[0]
        if self.iSearchIndex == 0:
            type=" "
        elif self.iSearchIndex == 1:
            type = 'B'
        elif self.iSearchIndex == 2:
            type='C'
        elif self.iSearchIndex == 3:
            type='D'
        elif self.iSearchIndex == 4:
            type='E'
        elif self.iSearchIndex == 5:
            tpye='G'
        elif self.iSearchIndex == 6:
            type='I'
        elif self.iSearchIndex == 7:
            type='M'
        elif self.iSearchIndex == 8:
            type='N'
        elif self.iSearchIndex == 9:
            type='R'
        elif self.iSearchIndex == 10:
            type='A'
        elif self.iSearchIndex == 11:
            type=''
        self.setXML(area,type,self.page)
        self.printAll()


    def setBack(self):
        self.page -= 1
        area = self.areaEntry.get()
        type = self.typwEntry2.get()
        self.iSearchIndex = self.SearchBox.curselection()[0]
        if self.iSearchIndex == 0:
            type = " "
        elif self.iSearchIndex == 1:
            type = 'B'
        elif self.iSearchIndex == 2:
            type = 'C'
        elif self.iSearchIndex == 3:
            type = 'D'
        elif self.iSearchIndex == 4:
            type = 'E'
        elif self.iSearchIndex == 5:
            tpye = 'G'
        elif self.iSearchIndex == 6:
            type = 'I'
        elif self.iSearchIndex == 7:
            type = 'M'
        elif self.iSearchIndex == 8:
            type = 'N'
        elif self.iSearchIndex == 9:
            type = 'R'
        elif self.iSearchIndex == 10:
            type = 'A'
        elif self.iSearchIndex == 11:
            type = ''
        self.setXML(area, type, self.page)
        self.printAll()




    def sendMain(self):#추후 이메일 내용 추가
        self.name = self.nameEntry.get()
        self.area = self.areaEntry.get()
        self.setXML2(self.name, self.area)
        for item in self.root.iter("item"):
            self.Addr = item.findtext("dutyAddr")
            self.dutyDivNam = item.findtext("dutyDivNam")
            self.dutyName=item.findtext("dutyName")
            self.dutyEtc=item.findtext("dutyEtc")
            self.dutyTel1=item.findtext("dutyTel1")
        self.host = "smtp.gmail.com"  # Gmail STMP 서버 주소.
        self.port = "587"
        self.senderAddr = "py6646@naver.com"  # 보내는 사람 email 주소.
        self.recipientAddr = "py6646@gmail.com"  # 받는 사람 email 주소.
        #self.html=self.RenderText
        self.msg = MIMEMultipart('alternative')
        self.msg['Subject'] = "병원 정보"
        self.msg['From'] = self.senderAddr
        self.msg['To'] = self.recipientAddr
        self.dataStr="이름 : "+self.dutyName+'\n'+"병원타입 : "+self.dutyDivNam+'\n'+"병원 주소 : "+self.Addr+'\n'+"진료과목 : "+ self.dutyEtc+'\n'+"병원 대표 번호 : "+self.dutyTel1+'\n'+"지도로 검색한 병원 상세정보입니다."
        self.part=MIMEText(self.dataStr)
        self.msg.attach(self.part)

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
        self.map_osm=folium.Map(location=[self.x,self.y],zoom_start=15)
        folium.Marker([self.x,self.y], popup=self.name).add_to(self.map_osm)
        self.map_osm.save('osm.html')

    def setXML2(self, name,area): #지도
        self.url = "http://apis.data.go.kr/B552657/HsptlAsembySearchService/getHsptlMdcncListInfoInqire?serviceKey=9Y0EzZk6MfXyi1eqXZje8fT1ff5xBnYcTohB2nMJOEWdUAM7cASbKYdJjW1ZjOaZ5ddX1fSFG%2BPKHc16GrmaOw%3D%3D" \
                 + "&Q0=" + urllib.parse.quote_plus(self.area)+ "&QN=" + urllib.parse.quote_plus(name)+ "&pageNo=1&numOfRows=10"
        self.tree = ET.ElementTree(file=urllib.request.urlopen(self.url))
        self.tree.write("DATA_Q.xml", encoding="utf-8")
        self.data = self.tree.getroot()

        self.doc = parse("DATA_Q.xml")
        self.root = self.doc.getroot()

    def setXML3(self, area, type):  #그래프 관련

        self.url = "http://apis.data.go.kr/B552657/HsptlAsembySearchService/getHsptlMdcncListInfoInqire?serviceKey=9Y0EzZk6MfXyi1eqXZje8fT1ff5xBnYcTohB2nMJOEWdUAM7cASbKYdJjW1ZjOaZ5ddX1fSFG%2BPKHc16GrmaOw%3D%3D" \
                   + "&Q0=" + urllib.parse.quote_plus(self.area) + "&QZ=" + urllib.parse.quote_plus(self.type) + "&pageNo=1&numOfRows=500"
        self.tree = ET.ElementTree(file=urllib.request.urlopen(self.url))
        self.tree.write("gra.xml", encoding="utf-8")
        self.data = self.tree.getroot()

        self.doc = parse("gra.xml")
        self.root = self.doc.getroot()

    def setXML4(self):
        self.url = "http://apis.data.go.kr/B552657/HsptlAsembySearchService/getHsptlMdcncListInfoInqire?serviceKey=9Y0EzZk6MfXyi1eqXZje8fT1ff5xBnYcTohB2nMJOEWdUAM7cASbKYdJjW1ZjOaZ5ddX1fSFG%2BPKHc16GrmaOw%3D%3D" \
                   + "&Q0=" + urllib.parse.quote_plus(self.area) + "&QZ=" + urllib.parse.quote_plus(self.type) + "&pageNo=" + str(
            self.page) + "&numOfRows=10"
        self.tree = ET.ElementTree(file=urllib.request.urlopen(self.url))
        self.tree.write("DATA_Q.xml", encoding="utf-8")
        self.data = self.tree.getroot()
        self.doc = parse("DATA_Q.xml")
        self.root = self.doc.getroot()

    def printAll(self):  # 검색에 따른 xml 출력
        self.RenderText.configure(state="normal")
        self.RenderText.delete(0.0, END)
        for item in self.root.iter("item"):
            self.RenderText.insert(INSERT, "\n[", INSERT, item.findtext("dutyDivNam"), INSERT, "]", INSERT,
                                   item.findtext("dutyAddr"))
            self.RenderText.insert(INSERT, chr(10))
            self.RenderText.insert(INSERT, "병원 이름: ", INSERT, item.findtext("dutyName"), INSERT)
            self.RenderText.insert(INSERT, chr(10))
        self.RenderText.configure(state="disabled")

    #def clean(self):
        #print("아니")

    def graphview(self): #그래프 액션
        self.area = self.areaEntry.get()

        self.ACount = self.getCount(self.area, 'B') #병원
        self.BCount = self.getCount(self.area, 'C')#의원
        self.CCount = self.getCount(self.area, 'D')#요양병원
        self.DCount = self.getCount(self.area, 'E')#한방병원
        self.ECount = self.getCount(self.area, 'G')#한의원
        self.FCount = self.getCount(self.area, 'I')#기타
        self.GCount = self.getCount(self.area, 'M')#치과병원
        self.HCount = self.getCount(self.area, 'N')#치과의원
        self.ICount = self.getCount(self.area, 'R')#보건소
        self.JCount = self.getCount(self.area, 'A')#종합병원
        print(self.ACount)
        print(self.BCount)
        print(self.CCount)
        print(self.DCount)
        print(self.ECount)
        print(self.FCount)
        print(self.GCount)
        print(self.HCount)
        print(self.ICount)
        print(self.JCount)


        self.count = [self.ACount, self.BCount, self.CCount, self.DCount, self.ECount,
                      self.FCount, self.GCount, self.HCount, self.ICount, self.JCount]

        self.c_width = 330  # Define it's width
        self.c_height = 270  # Define it's height
        self.c = Canvas(self.g_Tk, width=self.c_width, height=self.c_height, bg='white')

        self.c.pack()
        self.c.place(x=570, y=425)

        self.y_stretch = 15  # The highest y = max_data_value * y_stretch
        self.y_gap = 5  # The gap between lower canvas edge and x axis
        self.x_stretch = 10  # Stretch x wide enough to fit the variables
        self.x_width = 20  # The width of the x-axis
        self.x_gap = 20  # The gap between left canvas edge and y axis

        for x, y in enumerate(self.count):
            # coordinates of each bar

            # Bottom left coordinate
            self.x0 = x * self.x_stretch + x * self.x_width + self.x_gap

            # Top left coordinates
            self.y0 = self.c_height - (y * self.y_stretch + self.y_gap)

            # Bottom right coordinates
            self.x1 = x * self.x_stretch + x * self.x_width + self.x_width + self.x_gap

            # Top right coordinates
            self.y1 = self.c_height - self.y_gap

            # Draw the bar
            self.c.create_rectangle(self.x0, self.y0, self.x1, self.y1, fill="red")
            self.c.create_text(self.x0 + 10, 100, text=str(y))


        #self.c.create_rectangle(20, 260, 55,  200, fill="red")
        #self.c.create_rectangle(75, 260, 110, 80, fill="red")
        #self.c.create_rectangle(130, 260, 165, 80, fill="red")
        #self.c.create_rectangle(185, 260, 220, 80, fill="red")
        #self.c.create_rectangle(240, 260, 275, 80, fill="red")
        #self.c.create_rectangle(295, 260, 330, 80, fill="red")
        #self.c.create_rectangle(350, 260, 385, 80, fill="red")
        #self.c.create_rectangle(405, 260, 440, 80, fill="red")
        #self.c.create_rectangle(460, 260, 495, 80, fill="red")

        self.c.create_text(30, 250, text="병원")
        self.c.create_text(60, 250, text="의원")
        self.c.create_text(90, 250, text="요양")
        self.c.create_text(120, 250, text="한방")
        self.c.create_text(150, 250, text="한의원")
        self.c.create_text(182, 250, text="기타")
        self.c.create_text(210, 250, text="치과")
        self.c.create_text(240, 250, text="치과의")
        self.c.create_text(275, 250, text="보건소")
        self.c.create_text(305, 250, text="종합")




        #self.TempFont = font.Font(self.g_Tk, size=11, family='Consolas')
        #self.SearchButton = Button(self.g_Tk, font=self.TempFont, text="", command=self.SearchButtonAction)
        #self.SearchButton.pack()
        #self.buttonImage = PhotoImage(file="search.png")
        #self.SearchButton.config(image=self.buttonImage, compound=RIGHT)
        #self.SearchButton.place(x=400, y=325)

    #def graph(self):
        # self.Hospitaltype = ['의원', '요양병원', '한방병원', '한의원', '기타', '치과병원', '치과의원', '보건소', '종합병원']
        #self.area = "경기도"

        #self.ACount = self.getCount(self.area, 'B')
        #self.BCount = self.getCount(self.area, 'C')
        #self.CCount = self.getCount(self.area, 'D')
        #self.DCount = self.getCount(self.area, 'E')
        #self.ECount = self.getCount(self.area, 'G')
        #self.FCount = self.getCount(self.area, 'I')
        #self.GCount = self.getCount(self.area, 'M')
        #self.HCount = self.getCount(self.area, 'N')
        #self.ICount = self.getCount(self.area, 'R')
        #self.JCount = self.getCount(self.area, 'A')
        #print(self.ACount)
        #print(self.BCount)
        #print(self.CCount)

        #self.count = [self.ACount, self.BCount, self.CCount, self.DCount, self.ECount,
                      #self.FCount, self.GCount, self.HCount, self.ICount, self.JCount]

        #self.menber = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']


        #plt.bar(self.menber,self.count)
        #plt.title("HOSPTER")
        #plt.show()
    def getCount(self, area, type):
        self.tmp=0
        self.setXML3(area, type)
        for item in self.root.iter("item"):
            if item.findtext("dutyDiv") == type:
                self.tmp +=1
        return self.tmp




Hospital()
