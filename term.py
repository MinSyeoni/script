import urllib
#import folium
import http.client
from tkinter import *
from tkinter import font
from xml.etree.ElementTree import parse
import xml.etree.ElementTree as ET
#import matplotlib.pyplot as plt
import mimetypes
import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from http.client import HTTPSConnection
from http.server import BaseHTTPRequestHandler, HTTPServer
import tkinter.messagebox
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from io import BytesIO
import urllib.request
import urllib.parse
#from PIL import Image,ImageTk



class Hospital:
    def __init__(self):
        self.g_Tk = Tk()
        self.g_Tk.geometry("420x630+750+200")
        self.InitTopText()
        self.InitInputCityLabel()
        self.InitInputDistrictLabel()
        self.InitInputTownLabel()
        self.InitSearchButton()
        self.InitSearchButton2()
        self.InitGmailButton()
        self.InitRenderListText()
        self.g_Tk.mainloop()
        self.initVariable()
        self.setXML()
        self.sendMain()

        #그래프
        self.tmp = 0
        self.seoulCount = self.getCount("서울특별시")
        self.gyeongGiCount = self.getCount("경기도")
        self.busanCount = self.getCount("부산광역시")
        self.gyeongNamCount = self.getCount("경상남도")
        self.daeguCount = self.getCount("대구광역시")
        self.incheonCount = self.getCount("인천광역시")
        self.gyeongBukCount = self.getCount("경상북도")
        self.chungNamCount = self.getCount("충청남도")
        self.jeonBukCount = self.getCount("전라북도")
        self.jeonNamCount = self.getCount("전라남도")
        self.daejeonCount = self.getCount("대전광역시")
        self.gwangjuCount = self.getCount("광주광역시")
        self.gangWonCount = self.getCount("강원도")
        self.chungBukCount = self.getCount("충청북도")
        self.ulsanCount = self.getCount("울산광역시")
        self.jejuCount = self.getCount("제주특별자치도")
        self.sejongCount = self.getCount("세종특별자치시")

        self.member = ['Seoul', 'GyeongGi', 'Busan', 'Gyeongam', 'Daegu', 'Incheon', 'Gyeongbuk', 'Chungnam', 'Jeonbuk',
                       'Jeonnam', 'Daejeon', 'Gwangju', 'Gangwon ', 'Chungbuk', 'Ulsan', 'Jeju', 'Sejong']
        self.count = [self.seoulCount, self.gyeongGiCount, self.busanCount, self.gyeongNamCount, self.daeguCount,
                      self.incheonCount, self.gyeongBukCount, self.chungNamCount, self.jeonBukCount,
                      self.jeonNamCount, self.daejeonCount, self.gwangjuCount, self.gangWonCount, self.chungBukCount,
                      self.ulsanCount, self.jejuCount, self.sejongCount]
        self.member.reverse()
        self.count.reverse()

    def initVariable(self):
        self.page = 1
        self.name = ""
        self.area = ""
        self.onText = FALSE

    def InitTopText(self):
        self.TempFont = font.Font(self.g_Tk,size=17,weight='bold',family='Consolas')
        self.searchFont = font.Font(self.g_Tk, size=11,family='Consolas')
        self.MainText = Label(self.g_Tk,font = self.TempFont,text="< 병원정보서비스 App >")
        self.cityText = Label(self.g_Tk,font = self.searchFont,text="시/도")
        self.districtText = Label(self.g_Tk, font=self.searchFont, text="구/군")
        self.townText = Label(self.g_Tk, font=self.searchFont, text="이름")
        self.mapText = Label(self.g_Tk, font=self.searchFont, text="[ 병원 지도 ]")
        self.listText = Label(self.g_Tk, font=self.searchFont, text="[ 병원 리스트 ]")
        self.graphText = Label(self.g_Tk, font=self.searchFont, text="[ 지역별 병원 그래프 ]")
        #글자들 위치
        self.MainText.place(x=90)
        self.cityText.place(x=30,y=40)
        self.districtText.place(x=120,y=40)
        self.townText.place(x=200,y=40)
        self.mapText.place(x=10,y=100)
        self.listText.place(x=10,y=320)
        self.graphText.place(x=10,y=470)

    def InitInputCityLabel(self): #시도 입력창
        self.TempFont = font.Font(self.g_Tk,size=15,family='Consolas')
        self.areaEntry=StringVar()
        print("아")
        self.InputLabel = Entry(self.g_Tk,textvariable=self.areaEntry,font=self.TempFont,width=7,borderwidth=2,relief='ridge')
        self.InputLabel.pack()
        self.InputLabel.place(x=10,y=65)

    def nextButton(self):
        self.tempFont = font.Font(self.g_Tk, size=12, family='Consolas')
        self.nextButton = Button(self.g_Tk, font=self.tempFont,  text=">", command=self.setNext)
        self.nextButton.pack()
        self.nextButton.place(x=10, y=95)

    def previousButton(self):
        self.tempFont = font.Font(self.g_Tk, size=12,  family='Consolas')
        self.previousButton = Button(self.g_Tk, font=self.tempFont, text="<",
                                     command=self.setPrevious)
        self.previousButton.pack()
        self.previousButton.place(x=20, y=105)

    def InitInputDistrictLabel(self): #구군 입력창 #구현하려면 가능한데 UI수정필요해서 버립시다.
        self.TempFont = font.Font(self.g_Tk,size=15,family='Consolas')

        self.InputLabel = Entry(self.g_Tk,font=self.TempFont,width=7,borderwidth=2,relief='ridge')
        self.InputLabel.place(x=100,y=65)

    def InitInputTownLabel(self): #이름 검색라벨로 변경
        self.TempFont = font.Font(self.g_Tk,size=15,family='Consolas')
        self.nameEntry=StringVar()
        self.InputLabel = Entry(self.g_Tk, textvariable=self.nameEntry, font=self.TempFont,width=7,borderwidth=2,relief='ridge')
        self.InputLabel.pack()
        self.InputLabel.place(x=190,y=65)

    def InitSearchButton(self): #검색 버튼
        self.TempFont = font.Font(self.g_Tk, size=11,family='Consolas')
        self.SearchButton = Button(self.g_Tk,font=self.TempFont,text="시",command=self.setArea)
        self.SearchButton.pack()
        self.SearchButton.place(x=280,y=65)

    def InitSearchButton2(self): #이름검색 위치변경 필요
        self.TempFont = font.Font(self.g_Tk, size=11,family='Consolas')
        self.SearchButton = Button(self.g_Tk,font=self.TempFont,text="이름",command=self.setName)
        self.SearchButton.pack()
        self.SearchButton.place(x=280,y=105)


    def InitGmailButton(self): #지메일 버튼
        self.TempFont = font.Font(self.g_Tk, size=11,family='Consolas')
        self.SearchButton = Button(self.g_Tk,font=self.TempFont,text="G-mail",command=self.sendMain)
        self.SearchButton.pack()
        self.SearchButton.place(x=330,y=65)

    #def GmailAction(): #지메일 상호작용
        # global value
        # host = "smtp.gmail.com"  # Gmail STMP 서버 주소.
        #port = "587"
        #htmlFileName = "logo.html"
        #senderAddr = "@gmail.com"   # 보내는 사람 email 주소.
        #recipientAddr = "@naver.com"  # 받는 사람 email 주소.
        #msg = MIMEBase("multipart", "alternative")
        #msg['Subject'] = "병원 정보 스크랩"
        #msg['From'] = senderAddr
        #msg['To'] = recipientAddr

        #htmlFD = open(htmlFileName, 'rb')
        #HtmlPart = MIMEText(htmlFD.read(), 'html', _charset='UTF-8')
        #htmlFD.close()
        #msg.attach(HtmlPart)

        #s = mysmtplib.MySMTP(host, port)
        #s.ehlo()
        #s.starttls()
        #s.ehlo()
        #s.login("@gmail.com","") #아이디 비번
        #s.sendmail(senderAddr, [recipientAddr], msg.as_string())
        #s.close()
        #pass

    #def InitMap(): #지도
       # map_osm = folium.Map(location=[37.568477, 126.981611], zoom_start=20)
       # folium.Marker([37.568477, 126.981611], popup='Mt. Hood Meadows').add_to(map_osm)
        #map_osm.save('osm.html')

    #def InitImage(): #이거 왜 안나오냐
     #   url = "http://tong.visitkorea.or.kr/cms/resource/74/2396274_image2_1.JPG"
      #  with urllib.request.urlopen(url) as u:
       #     raw_data = u.read()
        #im = Image.open(BytesIO(raw_data))
        #image = ImageTk.PhotoImage(im)

        #label = Label(g_Tk, image=image, height=100, width=100)
        #label.pack()
        #label.place(x=10, y=120)

    def InitRenderListText(self): #병원 리스트 틀
        global RenderText
        self.RenderTextScrollbar = Scrollbar(self.g_Tk) #스크롤바
        self.RenderTextScrollbar.place(x=300,y=200)
        TempFont = font.Font(self.g_Tk,size=10,family='Consolas')
        #리스트박스
        self.RenderText = Text(self.g_Tk,width=53,height=8,borderwidth=2,relief='ridge',yscrollcommand=self.RenderTextScrollbar.set)
        self.RenderText.place(x=10,y=350)
        self.RenderTextScrollbar.config(command=self.RenderText.yview)
        self.RenderTextScrollbar.pack(side=RIGHT,fill=BOTH)
        self.RenderText.configure(state='disabled')

    def InitGraphList(self): #그래프
        self.canvas = Canvas(self.g_Tk,width=375,height=100,bg='white')
        self.canvas.place(x=10,y=500)
        self.numbers = [x for x in range(1, 21)]

    #데이터 값 지정
    def setXML(self): #시도,이름 검색 시 xmlset
        self.url="http://apis.data.go.kr/B552657/HsptlAsembySearchService/getHsptlMdcncListInfoInqire?serviceKey=9Y0EzZk6MfXyi1eqXZje8fT1ff5xBnYcTohB2nMJOEWdUAM7cASbKYdJjW1ZjOaZ5ddX1fSFG%2BPKHc16GrmaOw%3D%3D" \
                 + "&Q0=" + urllib.parse.quote_plus(self.area) + "&QN=" + urllib.parse.quote_plus(self.name) + "&pageNo=" + str(self.page) + "&numOfRows=10"
        print(urllib.parse.quote_plus(self.area))
        self.tree = ET.ElementTree(file=urllib.request.urlopen(self.url))
        self.tree.write("DATA_Q.xml",encoding="utf-8")
        self.data=self.tree.getroot()
        self.doc=parse("DATA_Q.xml")
        print(self.url)
        self.root=self.doc.getroot()

    def setXML_Graph(self, area):#그래프 형성용 XMLset
        self.url = "http://apis.data.go.kr/B552657/HsptlAsembySearchService/getHsptlMdcncListInfoInqire?serviceKey=9Y0EzZk6MfXyi1eqXZje8fT1ff5xBnYcTohB2nMJOEWdUAM7cASbKYdJjW1ZjOaZ5ddX1fSFG%2BPKHc16GrmaOw%3D%3D" \
                   + "&Q0=" + urllib.parse.quote_plus(area) + "&numOfRows=10"
        self.tree = ET.ElementTree(file=urllib.request.urlopen(self.url))
        self.tree.write("DATA_Q.xml", encoding="utf-8")
        self.data = self.tree.getroot()

        self.doc = parse("DATA_Q.xml")
        self.root = self.doc.getroot()

   # def renderRoundGraph(self):
    #    plt.pie(self.count,
     #           labels=self.member,
      #          shadow=False,
       #         explode=(0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        #        startangle=90,
         #       autopct='%1.1f%%')
       # plt.title('National Pharmacy Distribution Plot')
        #plt.show()
    #def renderStickGraph(self):
     #   plt.bar(self.member, self.count)

#        plt.title('National Pharmacy Distribution Plot')
 #       plt.show()

  #  def getCount(self, area):
   #     self.setXML(area)
    #    for body in self.root.iter("body"):
     #       self.tmp = body.findtext("totalCount")
      #      return self.tmp
    def setNext(self):
        if self.onText:
            self.page += 1
            self.setXML()
            self.printAll()

    def setPrevious(self):
        if self.page > 1 and self.onText:
            self.page -= 1
            self.setXML()
            self.printAll()
    def setArea(self): #시/도 검색
        self.page=1
        self.name=""
        self.area = self.areaEntry.get()
        self.setXML()
        self.printAll()

    def setName(self):
        self.page=1
        self.name=self.nameEntry.get()
        self.area=""
        self.setXML()
        self.printAll()
    def sendMain(self): #메일보내기
        self.host = "smtp.gmail.com"  # Gmail STMP 서버 주소.
        self.port = "587"
        self.html = self.setXML()
        self.msg = MIMEMultipart('alternative')
        self.recipientAddr = "py6646@naver.com"  # 보내는 사람 email 주소.
        self.senderAddr = "py6646@gmail.com"  # 받는 사람 email 주소.

        #self.msg['Subject'] =
        self.msg['From'] = self.senderAddr
        self.msg['To'] = self.recipientAddr
        self.msgPart = MIMEText('Y', 'plain')
        self.bookPart = MIMEText(self.html, 'html', _charset='UTF-8')

        self.msg.attach(self.msgPart)
        self.msg.attach(self.bookPart)
        self.s = smtplib.SMTP(self.host, self.port)
        self.s.ehlo()
        self.s.starttls()
        self.s.ehlo()
        self.s.login("py6646@gmail.com","py122134tkddn!")  # 로긴을 합니다.
        self.s.sendmail(self.senderAddr, [self.recipientAddr], self.msg.as_string())
        self.s.close()

    def printAll(self): #검색에 따른 xml 출력
        self.onText = TRUE
        self.RenderText.configure(state="normal")
        self.RenderText.delete(0.0, END)
        for item in self.root.iter("item"):
            self.RenderText.insert(INSERT,"[",INSERT,item.findtext("dutyDivNam"),INSERT,"]",INSERT,item.findtext("dutyAddr"))
            self.RenderText.insert(INSERT, chr(10))
            self.RenderText.insert(INSERT, "병원 이름: ",INSERT,item.findtext("dutyName"),INSERT)
            self.RenderText.insert(INSERT, chr(10))
        self.RenderText.configure(state="disabled")
#InitImage()
#InitGraphList()
#InitMap()

Hospital()