#!/usr/bin/python
# coding=utf-8

import sys
import time
import sqlite3
import telepot
from pprint import pprint
from urllib.request import urlopen
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re
from datetime import date, datetime, timedelta
import traceback

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse

import noti

items = []

type_list = {
    '병원' : 'B',
    '의원' : 'C',
    '요양병원' : 'D',
    '한방병원' : 'E',
    '한의원' : 'G',
    '기타' : 'H',
    '치과병원' : 'I',
    '치과의원' : 'M',
    '보건소' : 'N',
    '종합병원' : 'R'
    }


def initApiData(): # ?
    items.clear()

def replyAptData(user, type, area):
    noti.sendMessage(user, '병원 정보 로딩중입니다')

    url="http://apis.data.go.kr/B552657/HsptlAsembySearchService/getHsptlMdcncListInfoInqire?serviceKey=9Y0EzZk6MfXyi1eqXZje8fT1ff5xBnYcTohB2nMJOEWdUAM7cASbKYdJjW1ZjOaZ5ddX1fSFG%2BPKHc16GrmaOw%3D%3D" \
        + "&Q0=" + urllib.parse.quote_plus(area) + "&QZ=" + urllib.parse.quote_plus(type_list[type]) + "&pageNo=1&numOfRows=30"
    tree = ET.ElementTree(file=urllib.request.urlopen(url))
    tree.write("DATA_Q.xml",encoding="utf-8")
    data=tree.getroot()

    doc = parse("DATA_Q.xml")
    root = doc.getroot()

    msg = ''
    for item in root.iter("item"):
        msg += "["+item.findtext("dutyDivNam")+"]"+item.findtext("dutyAddr")+'\n'
        msg += "병원 이름: "+item.findtext("dutyName")+'\n\n'
    
    if msg:
        noti.sendMessage( user, msg )
    else:
        noti.sendMessage( user, '%s 해당하는 병원정보가 없습니다.'%type )

#def save( user, loc_param ):
    #    conn = sqlite3.connect('users.db')
    #cursor = conn.cursor()
    #cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    #try:
    #   cursor.execute('INSERT INTO users(user, location) VALUES ("%s", "%s")' % (user, loc_param))
    #except sqlite3.IntegrityError:
        #   noti.sendMessage( user, '이미 해당 정보가 저장되어 있습니다.' )
        #return
        #else:
        #noti.sendMessage( user, '저장되었습니다.' )
        #conn.commit()

#def check( user ):
    #   conn = sqlite3.connect('users.db')
    #cursor = conn.cursor()
    #cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    #cursor.execute('SELECT * from users WHERE user="%s"' % user)
    #for data in cursor.fetchall():
        #    row = 'id:' + str(data[0]) + ', location:' + data[1]
        #noti.sendMessage( user, row )

#def printList(user,key): #???????????
#    msg = ''
#    for d in type[key].keys():
#        msg += d + '\n'
#    if msg:
#        noti.sendMessage(user, msg)
#    else:
#        noti.sendMessage(user, '해당하는 데이터가 없습니다.')

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        noti.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
        return

    text = msg['text']
    args = text.split(' ')

    if text.startswith('검색') and len(args)>1:
        print('try to 검색', args[1], args[2])
        replyAptData(chat_id, args[1], args[2])
    elif text.startswith('도움말'):
        noti.sendMessage(chat_id, '---------------------------------\n< 병원 정보 검색방법 >\n검색 병원종류 지역\nex)검색 요양병원 경기도시흥시\n---------------------------------')
    elif text.startswith('병원종류'):
        noti.sendMessage(chat_id, '-------------\n병원\n의원\n요양병원\n한방병원\n한의원\n기타\n치과병원\n치과의원\n보건소\n종합병원\n-------------')
    elif text.startswith('시작'):
        noti.sendMessage(chat_id, '< 스크립트언어 >\n병원 정보 조회 서비스 챗봇입니다\n명령어 : 도움말 / 병원종류')
    else:
        noti.sendMessage(chat_id, '올바른 검색 방법을 사용해주세요')
        noti.sendMessage(chat_id, '검색 병원종류 지역\nex)검색 요양병원 경기도시흥시\n--------------------------\n명령어 : 도움말 / 병원종류')


today = date.today()
current_month = today.strftime('%Y%m')

print( '[',today,']received token :', noti.TOKEN )

bot = telepot.Bot(noti.TOKEN)
pprint( bot.getMe() )

bot.message_loop(handle)

print('Listening...')

while 1:
  time.sleep(10)
