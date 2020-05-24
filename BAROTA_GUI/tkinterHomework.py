import tkinter
import BAROTA

class trainTk:
    def __init__(self):
        self.trainDB = BAROTA.train()
        self.window = tkinter.Tk()
        self.window.title("빠른 기차 예매 프로그램")
        self.window.geometry("640x400+100+100")
        self.window.resizable(False,False)


        self.selectMenuLabel = tkinter.Label(self.window,  text="메뉴")#, relief = "solid")
        self.selectMenuLabel.place(x=500,y=10)
        self.selectMenuListbox = tkinter.Listbox(self.window, selectmode='extended', 
        width = 30, height=0)
        self.selectMenuListbox.insert(0, '메뉴를 선택하세요')
        self.selectMenuListbox.insert(1,'1. 빠른시간 기차 검색 및 예매')
        self.selectMenuListbox.insert(2,'2. 전체 기차 리스트 출력')
        self.selectMenuListbox.insert(3,'3. 나의 예매 현황 출력 및 예매 취소')
        self.selectMenuListbox.insert(4,'4. 프로그램 종료')
        self.selectMenuListbox.place(x=400, y=30)

        # 안내창
        self.guideTextLabel = tkinter.Label(self.window,  text="안내창")#, relief = "solid")
        self.guideTextLabel.place(x=490,y=130)
        self.guideText = tkinter.Text(self.window, width = 30, height = 10)
        self.guideText.place(x=400,y=150)

        # 명령창
        self.commandInputTextLabel = tkinter.Label(self.window,  text="입력창")#, relief = "solid")
        self.commandInputTextLabel.place(x=490,y=290)
        self.commandInputText = tkinter.Text(self.window, width = 30, height = 5)
        self.commandInputText.place(x=400, y=315)

        # 정보창(왼쪽)
        self.trainDataTextLabel = tkinter.Label(self.window,  text="정보창")#, relief = "solid")
        self.trainDataTextLabel.place(x=160,y=10)
        self.trainDataText = tkinter.Text(self.window, width = 50, height = 27)
        self.trainDataText.place(x=10, y=30)

        # 이후 실행
        self.guideText.insert(tkinter.END, "명령창에 명령 번호를 입력 후 버튼을 클릭하세요.\n")
        self.commandInputText.bind("<Return>", self.program_start)

        self.window.mainloop()

    def program_start(self, event):    
        selectMenuNonPorcessing = self.commandInputText.get(1.0,'end')
        self.selectMenu = int(selectMenuNonPorcessing.rstrip())
        if self.selectMenu == 1:
            self.trainDB.menu_1()
        elif self.selectMenu == 2:
            self.trainDB.menu_2()
        elif self.selectMenu == 3:
            self.trainDB.menu_3()
        elif self.selectMenu == 4:
            self.trainDB.menu_4()

if __name__ == "__main__":    
    BAROTAProgram = trainTk()
