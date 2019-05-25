from tkinter import *

class Horse:
    def horseFinder(self):
        pass

    def gmail(self):
        pass

    def racecourse(self):
        pass

    def __init__(self):
        window = Tk()
        window.title("경마 정보 및 성적 조회")
        self.width = 300
        self.height = 100

        frame1 = Frame(window) # 경마 검색 및 지메일
        frame1.pack()
        Label(frame1,text="경마 종류 입력").pack(side=LEFT)
        e=Entry(frame1,text='')
        e.pack(side=LEFT)
        Button(frame1,text="검색",command=self.horseFinder).pack(side=LEFT)
        Button(frame1,text="G-MAIL",command=self.gmail).pack(side=LEFT)

        Label(frame1, text="   ").pack(side=LEFT)
        Label(frame1, text="경마장 검색").pack(side=LEFT)
        e = Entry(frame1, text='')
        e.pack(side=LEFT)
        Button(frame1, text="검색", command=self.racecourse).pack(side=LEFT)

        frame2 = Frame(window) # 경마 목록
        frame2.pack()
        scrollbar = Scrollbar(frame2)
        scrollbar.pack(side=RIGHT, fill=Y)
        text = Text(frame2, width=40, height=10, wrap=WORD, yscrollcommand=scrollbar.set)
        text.pack()
        scrollbar.config(command=text.yview)

        frame3 = Frame(window)  # 성적 배당 그래프
        frame3.pack()
        Label(frame3, text="경마 성적 및 배당률 그래프").pack(side=LEFT)

        self.canvas = Canvas(window, width=self.width, height=self.height, bg='white')
        self.canvas.pack()

        frame4 = Frame(window)  # 성적 배당 그래프
        frame4.pack(side=RIGHT)

        window.mainloop()

Horse()