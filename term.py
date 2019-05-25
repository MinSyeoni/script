import urllib
import http.client
from tkinter import *
from tkinter import font
import tkinter.messagebox
# -*- encoding: cp949 -*-

import mimetypes
#import mysmtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText


import urllib
import http.client
from tkinter import *
from tkinter import font
import tkinter.messagebox

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

g_Tk = Tk()
g_Tk.geometry("420x630+750+200") #tk크기
DataList=[]

InitTopText()
g_Tk.mainloop()