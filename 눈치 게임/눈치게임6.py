from tkinter import *                               #실행 필수 함수들 
import pygame,random,time, sys, math, threading
import time as t



heart = 3 #목숨
score = 0 #점수

## 함수 선언 부분 ##
def paintEntity(entity,x,y):        #객체를 화면에 그린다.
    monitor.blit(entity,(x,y))

def writeScore(score):          #점수 텍스트 함수
    
    score_txt = FONT2.render("score :"+str(score), True, BLACK)  
    monitor.blit(score_txt, (400, 50))
    
def writeHeart(heart):          #목숨 텍스트 함수
    
    heart_txt = FONT2.render("heart :"+str(heart), True, BLACK)
    monitor.blit(heart_txt, (50, 50))

    
    
    
def playGame():             #게임 플레이 함수
    global monitor, men, menSon, menimage, hand
    

    r=random.randrange(0,256)       #랜덤 배경을 만들기 위한 색 지정
    g=random.randrange(0,256)
    b=random.randrange(0,256)

    pp=[0,0,0,0,0,0]                #사람 랜덤 초
    ppimage=[0,0,0,0,0,0]           #사람 이미지 

      
                          
    for i in range(6):              #리스트로 각각 사람에게 '초'를 준다.
        ranNum=(random.random())+random.randint(0,5)    #정수초 + 실수초
        roundNum= round(ranNum,1)                      #그걸 0.0자리수로 만든다.
        pp[i] = roundNum
        

    for i in range(6):              #이미지를 각각 사람에게 준다.
        ppimage[i]= men
    print(pp[0])              ##삭제, 확인용
    print(pp[1])
    print(pp[2])
    print(pp[3])
    print(pp[4])
    print(pp[5])
    
    
    

    gray=(150,150,150) # 배경 :메모용
    black=(0,0,0)
    red=(200,0,0)
    white=(255,255,255)

    

    
    num = 0    #외치는 숫자
    dt = 0      #타이머.틱
    timer = 0   #타이머
    
    loop = True  #루프가 계속 돌아가게끔
    hand = None  # hand 변수 선언

    while loop:             #무한 루프 
        global heart, heart, score
        pygame.time.Clock().tick(120)
        monitor.fill((90,196,153))     #배경 전환

        for event in pygame.event.get():        #키보드 이벤트 체크
            if event.type in [pygame.QUIT]:
                    pygame.quit()
                    sys.exit()



        # --- Timer ---
        
        timer += dt
        timerSec = (round(timer, 1))    #0.0 으로 만든다.
        click=pygame.mouse.get_pressed()
        
        
        dt = fps_clock.tick(120) / 1000  #프레임 틱을 초로 계산

        
                                                
                    
        #사람 이미지 불러오기 
        paintEntity(ppimage[0],83,200)
        paintEntity(ppimage[1],200,200)
        paintEntity(ppimage[2],317,200)
        paintEntity(ppimage[3],83,350)
        paintEntity(ppimage[4],200,350)
        paintEntity(ppimage[5],317,350)
        
        
        
        
        ### 게임 룰 시작

        
           
        # 시간과 주어진 랜덤함수가 같으면 손을 든다.
        if timerSec == pp[0]:
            
            ppimage[0] = menSon
            
                                   
        if timerSec == pp[1]:
            
            ppimage[1] = menSon
            

        if timerSec == pp[2]:
            
            ppimage[2] = menSon
            
        if timerSec == pp[3]:
            
            ppimage[3] = menSon
            

        if timerSec == pp[4]:
            
            ppimage[4] = menSon
            

        if timerSec == pp[5]:
            
            ppimage[5] = menSon


        ## 클릭하면 손든다.
        handup = 0

        for event in pygame.event.get():
            
            if heart == 0:              #목숨이 0 이면 종료 
                 loop = False
                 showGameOverScreen()
                 break

            elif event.type in [pygame.MOUSEBUTTONDOWN]:  # 마우스 클릭했을 때 
                handup = timerSec

                # 질 때
                if (handup == pp[0]) or (handup == pp[1]) or (handup == pp[2]) or (handup == pp[3]) or (handup == pp[4]) or (handup == pp[5]):  
                    heart -= 1
                    lose_txt = FONT.render('lose!', True, RED)  
                    monitor.blit(lose_txt, (225, 90))
                    loop = False
                    playGame()
                    
                 # 이길 때   
                if (handup != pp[0]) or (handup != pp[1]) or (handup != pp[2]) or (handup != pp[3]) or (handup != pp[4]) or (handup != pp[5]):
                    score += 1
                    win_txt = FONT.render('win!', True, RED)  
                    monitor.blit(win_txt, (225, 90))
                    loop = False
                    playGame()
                    
                    
            # 손을 안들어서 질 때        
            if num == 6 :
                heart -=1
                loop = False
                playGame()
               
                
        
        num_txt = FONT.render(str(num), True, BLACK) # 숫자 외치는 것
        num = ppimage.count(menSon) #손든 이미지 개수 
        click_txt = FONT.render('click!', True, BLACK)  #클릭 텍스트
        monitor.blit(num_txt, (225, 50))   #num 텍스트
        monitor.blit(click_txt, (195, 500))  #클릭 텍스트
        
                       
        writeScore(score) #점수 텍스트
        writeHeart(heart) #목숨 텍스트
        
        print(timerSec)  #삭제용
        pygame.display.update()     #화면을 업데이트 한다
        print('~',end='')           #실행되는지 확인용 

def showGameOverScreen():           #게임 오버 화면
    lose_txt = FONT.render('Game Over!!!', True, RED)  
    monitor.blit(lose_txt, (83, 100))
    
    
    

##전역 변수 부분##

r, g, b = [0]*3                 #랜덤 배경색 변수
swidth,sheight = 500, 600       #화면 크기 변수
monitor = None
men,menSize = None, 0   #사람 객체와 크기 변수
menSon,menSonSize = None, 0 
menimage=['men.png','men.png','men.png','men.png','men.png','men.png']  #이미지 불러오기 
pygame.init()
FONT = pygame.font.Font(None, 60)   #폰트 설정
FONT2 = pygame.font.Font(None, 25)
FONT3 = pygame.font.Font(None, 200)
BLACK = pygame.Color('black')       #아래는 모두 색 설정이다.
RED = pygame.Color('red')
WHITE = pygame.Color('white')
green=(0,200,0)
bgreen=(0,255,0)

##메인 코드 부분 ##

pygame.init()   # 초기화하고 시작한다
monitor = pygame.display.set_mode((swidth,sheight))     #화면 크기
pygame.display.set_caption("눈치 게임 시작")   #이름
fps_clock = pygame.time.Clock()             #시간
men = pygame.image.load("men.png")     #그림 불러와 크기 구한다.
menSize=men.get_rect().size
menSon = pygame.image.load("menSon.png")      #그림 불러와 크기 구한다.
menSonSize=menSon.get_rect().size

while heart != 0:           #메인 실행 코드
    playGame()
    if heart <= 0:
        break
    


