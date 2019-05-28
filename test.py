from tkinter import*
import random

class Samok:
    def __init__(self):
        window = Tk()
        self.turn =True
        self.imageList = [PhotoImage(file='circle.gif'),PhotoImage(file='cross.gif'),PhotoImage(file='empty.gif')]
        self.buttonList = []
        frame1=Frame(window)
        frame1.pack()
        for r in range(6):
            for c in range(7):
                self.buttonList.append(Button(frame1,text=' ',image=self.imageList[2],
                                              command=lambda Row=r,Col=c: self.pressed(Row,Col)))
                self.buttonList[-1].grid(row=r,column=c)

        frame2=Frame(window)
        frame2.pack()
        self.button = Button(frame2,text="다시생성",command=self.again)
        self.button.pack()

        self.winButtons=[]

        window.mainloop()

    def again(self):
        for i in range(6*7):
            self.buttonList[i].configure(image=self.imageList[2],text=' ')
            self.winButtons=[]
        self.turn = True

    def pressed(self,Row,Col):
        for r in range(5,-1,-1):
            if self.buttonList[r*7+Col]["text"] == ' ':
                if self.turn:   # O 차례
                    self.buttonList[r*7+Col].configure(image=self.imageList[0],text='O')
                else:           # X 차례
                    self.buttonList[r*7+Col].configure(image=self.imageList[1],text='X')
                self.turn = not self.turn
                break
        self.check()
    def check(self):
        #행
        for r in range(6):
            for c in range(3):
                if 'O' == self.buttonList[r*7+c]["text"] == self.buttonList[r*7+c+1]["text"] == \
                    self.buttonList[r*7+c+2]["text"] == self.buttonList[r*7+c+3]["text"]:
                    self.button.configure(text="O 이김")
                    self.winButtons=[self.buttonList[r*7+c],self.buttonList[r*7+c+1],self.buttonList[r*7+c+2],self.buttonList[r*7+c+3]]
                elif 'X' == self.buttonList[r*7+c]["text"] == self.buttonList[r*7+c+1]["text"] == \
                    self.buttonList[r*7+c+2]["text"] == self.buttonList[r*7+c+3]["text"]:
                    self.button.configure(text="X 이김")
                    self.winButtons=[self.buttonList[r*7+c],self.buttonList[r*7+c+1],self.buttonList[r*7+c+2],self.buttonList[r*7+c+3]]
        #열
        for c in range(7):
            for r in range(3):
                if 'O' == self.buttonList[r*7+c]["text"] == self.buttonList[(r+1)*7+c]["text"] == \
                    self.buttonList[(r+2)*7+c]["text"] == self.buttonList[(r+3)*7+c]["text"]:
                    self.button.configure(text="O 이김")
                    self.winButtons=[self.buttonList[r*7+c],self.buttonList[(r+1)*7+c],self.buttonList[(r+2)*7+c],self.buttonList[(r+3)*7+c]]
                elif 'X' == self.buttonList[r * 7 + c]["text"] == self.buttonList[(r + 1) * 7 + c]["text"] == \
                    self.buttonList[(r + 2) * 7 + c]["text"] == self.buttonList[(r + 3) * 7 + c]["text"]:
                    self.button.configure(text="X 이김")
                    self.winButtons=[self.buttonList[r*7+c],self.buttonList[(r+1)*7+c],self.buttonList[(r+2)*7+c],self.buttonList[(r+3)*7+c]]

        # 위/
        for i in range(3):
            for j in range(i+1):
                for k in range(3,-1,-1):
                    if 'O' == self.buttonList[j*7+k+i]["text"] ==self.buttonList[(j+1)*7 +(k+i-1)]["text"] ==\
                    self.buttonList[(j+2)*7+(k+i-2)]["text"] == self.buttonList[(j+3)*7+(k+i-3)]["text"]:
                        self.button.configure(text="O 이김")
                        self.winButtons = [self.buttonList[j*7+k+i], self.buttonList[(j+1)*7 +(k+i-1)], self.buttonList[(j+2)*7+(k+i-2)], self.buttonList[(j+3)*7+(k+i-3)]]
                    elif 'X' == self.buttonList[j*7+k+i]["text"] ==self.buttonList[(j+1)*7 +(k+i-1)]["text"] ==\
                    self.buttonList[(j+2)*7+(k+i-2)]["text"] == self.buttonList[(j+3)*7+(k+i-3)]["text"]:
                        self.button.configure(text="X 이김")
                        self.winButtons = [self.buttonList[j*7+k+i], self.buttonList[(j+1)*7 +(k+i-1)], self.buttonList[(j+2)*7+(k+i-2)], self.buttonList[(j+3)*7+(k+i-3)]]

        # 밑/
        for i in range(3):
            for j in range(2-i,-1,-1):
                for k in range(3):
                    if 'O' == self.buttonList[j*7+(6-k-i)]["text"] == self.buttonList[(j+1)*7+(6-k-i-1)]["text"] ==\
                    self.buttonList[(j+2)*7+(6-k-i-2)]["text"] == self.buttonList[(j+3)*7+(6-k-i-3)]["text"]:
                        self.button.configure(text="O 이김")
                        self.winButtons = [self.buttonList[j*7+(6-k-i)],self.buttonList[(j+1)*7+(6-k-i-1)],self.buttonList[(j+2)*7+(6-k-i-2)],self.buttonList[(j+3)*7+(6-k-i-3)]]
                    elif 'X' == self.buttonList[j*7+(6-k-i)]["text"] == self.buttonList[(j+1)*7+(6-k-i-1)]["text"] ==\
                    self.buttonList[(j+2)*7+(6-k-i-2)]["text"] == self.buttonList[(j+3)*7+(6-k-i-3)]["text"]:
                        self.button.configure(text="X 이김")
                        self.winButtons = [self.buttonList[j*7+(6-k-i)],self.buttonList[(j+1)*7+(6-k-i-1)],self.buttonList[(j+2)*7+(6-k-i-2)],self.buttonList[(j+3)*7+(6-k-i-3)]]
        # 밑\
        for i in range(3,6):
            for j in range(5-i,-1,-1):
                for k in range(3):
                    if 'O' == self.buttonList[j*7 +k+(i-3)]["text"] ==self.buttonList[(j+1)*7+k+(i-3)+1]["text"]==\
                    self.buttonList[(j+2)*7+k+(i-3)+2]["text"] ==self.buttonList[(j+3)*7+k+(i-3)+3]["text"]:
                        self.button.configure(text="O 이김")
                        self.winButtons = [self.buttonList[j*7 +k+(i-3)],self.buttonList[(j+1)*7+k+(i-3)+1],self.buttonList[(j+2)*7+k+(i-3)+2],self.buttonList[(j+3)*7+k+(i-3)+3]]
                    elif 'X' == self.buttonList[j*7 +k+(i-3)]["text"] ==self.buttonList[(j+1)*7+k+(i-3)+1]["text"]==\
                    self.buttonList[(j+2)*7+k+(i-3)+2]["text"] ==self.buttonList[(j+3)*7+k+(i-3)+3]["text"]:
                        self.button.configure(text="X 이김")
                        self.winButtons = [self.buttonList[j*7 +k+(i-3)],self.buttonList[(j+1)*7+k+(i-3)+1],self.buttonList[(j+2)*7+k+(i-3)+2],self.buttonList[(j+3)*7+k+(i-3)+3]]

        # 위\
        for i in range(3,0,-1):
            for j in range(-i+4):
                for k in range(3):
                    if 'O' ==self.buttonList[j*7+k+(-i+3)]["text"] ==self.buttonList[(j+1)*7+k+(-i+3)+1]["text"]==\
                    self.buttonList[(j+2)*7+k+(-i+3)+2]["text"]==self.buttonList[(j+3)*7+k+(-i+3)+3]["text"]:
                        self.button.configure(text="O 이김")
                        self.winButtons = [self.buttonList[j*7+k+(-i+3)],self.buttonList[(j+1)*7+k+(-i+3)+1],self.buttonList[(j+2)*7+k+(-i+3)+2],self.buttonList[(j+3)*7+k+(-i+3)+3]]
                    elif 'X' ==self.buttonList[j*7+k+(-i+3)]["text"] ==self.buttonList[(j+1)*7+k+(-i+3)+1]["text"]==\
                    self.buttonList[(j+2)*7+k+(-i+3)+2]["text"]==self.buttonList[(j+3)*7+k+(-i+3)+3]["text"]:
                        self.button.configure(text="X 이김")
                        self.winButtons = [self.buttonList[j*7+k+(-i+3)],self.buttonList[(j+1)*7+k+(-i+3)+1],self.buttonList[(j+2)*7+k+(-i+3)+2],self.buttonList[(+3)*7+k+(-i+3)+3]]

Samok()