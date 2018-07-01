from tkinter import*                  #필수
import random                         #랜덤 함수
from tkinter import messagebox        #메세지 박스
import pygame #모듈
import sys#


window = Tk()
window.title("눈치 게임 시작!")  # 윈도우 창 제목 설정
window.geometry("500x600")       #초기 크기 지정
window.resizable(width = FALSE, height = FALSE)   # 크기 변경 못함


def playgame():
    from 눈치게임6 import playGame

label1 = Label(window,text="눈치 게임을 시작합니다.",font=("바탕",30))
_start = Button(window, text="눈치게임 시작!", command = playgame)# 시작 버튼
_exit= Button(window, text="게임 종료",command= quit)    # 종료 버튼




### 함수를 호출해야 창에 나타난다.###

label1.place(x=40,y=150)
_start.place(x=45,y=250, width = 400, height = 80)
_exit.place(x=45,y=350, width = 400, height = 80)



    

window.mainloop() #윈도우를 부를때 필수 함수



