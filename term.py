import urllib
import folium
import http.client
from tkinter import *
from tkinter import font

import tkinter.messagebox
# -*- encoding: cp949 -*-

import mimetypes
#import mysmtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

#conn = http.client.HTTPConnection("apis.data.go.kr")
#conn.request("GET","/B551182/hospAsmRstInfoService/getGnhpSprmAsmRstList?serviceKey=yOJok8JvEqZFYgyzzt59glVlJ1EbfIxYgT5vEz5O%2BqxdhWM%2FhKAuV9knUxKBNWEIS4IOnD%2Fpmxb%2B2lqBShuzJQ%3D%3D")
#req = conn.getresponse()
#print(req.status,req.reason)
#print(req.read().decode('utf-8'))

def InitTopText():
    TempFont = font.Font(g_Tk,size=17,weight='bold',family='Consolas')
    searchFont = font.Font(g_Tk, size=11,family='Consolas')
    MainText = Label(g_Tk,font = TempFont,text="< 병원정보서비스 App >")
    cityText = Label(g_Tk,font = searchFont,text="시/도")
    districtText = Label(g_Tk, font=searchFont, text="구/군")
    townText = Label(g_Tk, font=searchFont, text="읍/면/동")
    mapText = Label(g_Tk, font=searchFont, text="[ 병원 지도 ]")
    listText = Label(g_Tk, font=searchFont, text="[ 병원 리스트 ]")
    graphText = Label(g_Tk, font=searchFont, text="[ 지역별 병원 그래프 ]")
    #글자들 위치
    MainText.place(x=90)
    cityText.place(x=30,y=40)
    districtText.place(x=120,y=40)
    townText.place(x=200,y=40)
    mapText.place(x=10,y=100)
    listText.place(x=10,y=320)
    graphText.place(x=10,y=470)

def InitInputCityLabel(): #시도 입력창
    global InputLabel
    TempFont = font.Font(g_Tk,size=15,family='Consolas')
    InputLabel = Entry(g_Tk,font=TempFont,width=7,borderwidth=2,relief='ridge')
    InputLabel.place(x=10,y=65)

def InitInputDistrictLabel(): #구군 입력창
    global InputLabel
    TempFont = font.Font(g_Tk,size=15,family='Consolas')
    InputLabel = Entry(g_Tk,font=TempFont,width=7,borderwidth=2,relief='ridge')
    InputLabel.place(x=100,y=65)

def InitInputTownLabel(): #읍면동 입력창
    global InputLabel
    TempFont = font.Font(g_Tk,size=15,family='Consolas')
    InputLabel = Entry(g_Tk,font=TempFont,width=7,borderwidth=2,relief='ridge')
    InputLabel.place(x=190,y=65)

def InitSearchButton(): #검색 버튼
    TempFont = font.Font(g_Tk, size=11,family='Consolas')
    SearchButton = Button(g_Tk,font=TempFont,text="검색",command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=280,y=65)

def SearchButtonAction(): #검색 버튼 상호작용
    pass

def InitGmailButton(): #지메일 버튼
    TempFont = font.Font(g_Tk, size=11,family='Consolas')
    SearchButton = Button(g_Tk,font=TempFont,text="G-mail",command=GmailAction)
    SearchButton.pack()
    SearchButton.place(x=330,y=65)

def GmailAction(): #지메일 상호작용
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
    pass

def InitMap(): #지도
    map_osm = folium.Map(location=[37.568477, 126.981611], zoom_start=20)
    folium.Marker([37.568477, 126.981611], popup='Mt. Hood Meadows').add_to(map_osm)
    map_osm.save('osm.html')

def InitRenderListText(): #병원 리스트 틀
    global RenderText
    RenderTextScrollbar = Scrollbar(g_Tk) #스크롤바
    RenderTextScrollbar.place(x=300,y=200)
    TempFont = font.Font(g_Tk,size=10,family='Consolas')
    #리스트박스
    RenderText = Text(g_Tk,width=53,height=8,borderwidth=2,relief='ridge',yscrollcommand=RenderTextScrollbar.set)
    RenderText.place(x=10,y=350)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT,fill=BOTH)
    RenderText.configure(state='disabled')

def InitGraphList(): #그래프
    global canvas, numbers
    canvas = Canvas(g_Tk,width=375,height=100,bg='white')
    canvas.place(x=10,y=500)
    numbers = [x for x in range(1, 21)]

g_Tk = Tk()
g_Tk.geometry("420x630+750+200") #tk크기
DataList=[]

InitTopText()
InitInputCityLabel()
InitInputDistrictLabel()
InitInputTownLabel()
InitSearchButton()
InitGmailButton()
InitRenderListText()
InitGraphList()
InitMap()
g_Tk.mainloop()