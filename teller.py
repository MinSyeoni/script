#!/usr/bin/python
# coding=utf-8

import sys
import time
import sqlite3
import telepot
from pprint import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from datetime import date, datetime, timedelta
import traceback

import noti

items = []
type = dict()

def initApiData(): # ?
    items.clear()

def replyAptData(type, user, area):
    print(user, type, area)
    res_list = noti.getData( type, area )
    msg = ''
    for r in res_list:
        print( str(datetime.now()).split('.')[0], r )
        if len(r+msg)+1>noti.MAX_MSG_LENGTH:
            noti.sendMessage( user, msg )
            msg = r+'\n'
        else:
            msg += r+'\n'
    if msg:
        noti.sendMessage( user, msg )
    else:
        noti.sendMessage( user, '%s 해당하는 병원정보가 없습니다.'%type )

def save( user, loc_param ):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    try:
        cursor.execute('INSERT INTO users(user, location) VALUES ("%s", "%s")' % (user, loc_param))
    except sqlite3.IntegrityError:
        noti.sendMessage( user, '이미 해당 정보가 저장되어 있습니다.' )
        return
    else:
        noti.sendMessage( user, '저장되었습니다.' )
        conn.commit()

def check( user ):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    cursor.execute('SELECT * from users WHERE user="%s"' % user)
    for data in cursor.fetchall():
        row = 'id:' + str(data[0]) + ', location:' + data[1]
        noti.sendMessage( user, row )

def printList(user,key): #???????????
    msg = ''
    for d in type[key].keys():
        msg += d + '\n'
    if msg:
        noti.sendMessage(user, msg)
    else:
        noti.sendMessage(user, '해당하는 데이터가 없습니다.')

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        noti.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
        return

    text = msg['text']
    args = text.split(' ')

    #if text.startswith('병원') and len(args)>1:
    #    print('try to 병원', args[1])
    #    replyAptData( args[1], chat_id, args[1])
    #elif text.startswith('의원') and len(args)>1:
    #    print('try to 지역', args[1])
    #    replyAptData( '201705', chat_id, args[1] )
    #elif text.startswith('저장')  and len(args)>1:
    #    print('try to 저장', args[1])
    #    save( chat_id, args[1] )
    #elif text.startswith('확인'):
    #    print('try to 확인')
    #    check( chat_id )

    if text.startswith('시작'):
        noti.sendMessage(chat_id, '< 스크립트언어 >\n병원 정보 조회 서비스 챗봇입니다\n시/도 병원 이름을 입력하세요.\n ex)경기도 치과')
    elif text.startswith(''): #수정
        pass
    else:
        noti.sendMessage(chat_id, '시/도 병원 이름을 입력하세요') #마찬가지


today = date.today()
current_month = today.strftime('%Y%m')

print( '[',today,']received token :', noti.TOKEN )

bot = telepot.Bot(noti.TOKEN)
pprint( bot.getMe() )

bot.message_loop(handle)

print('Listening...')

while 1:
  time.sleep(10)
