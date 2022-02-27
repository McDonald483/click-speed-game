import random
import pygame
import time
pygame.font.init()

WID = 1200
HIG = 600
WIN = pygame.display.set_mode((WID, HIG))
RED = (255,0,0)
WHITE =(255,255,255)
YELLOW = (255,255,0)
GREEN = (0,255,0)
TARGET_SIZE = 10
FONT = pygame.font.SysFont('comicsans', 40)
FONT2 = pygame.font.SysFont('comicsans', 20)
TARGET_X = 200
TARGET_Y = 200
MOUSE_X = 0
MOUSE_Y = 0
CLICKS = 0
TARGETCLICKS = 0
TIME = 15
CLOCK = 0
CLOCK2 = 0


WIN.fill((0,0,0))

def first():
    BEGIN = True 
    while BEGIN:
        START = FONT.render('ARE YOU READY TO PLAY?', 1, WHITE)
        WIN.blit(START, (325, 10))
        START2 = FONT.render('HIT SPACEBAR TO START', 1, WHITE)
        WIN.blit(START2, (325, 100))
        START3 = FONT2.render('THE RULES ARE SIMPLE, CLICK AS MANY RED TARGETS AS YOU CAN AFTER THE THREE CIRCLES DISAPPEAR', 1, WHITE)
        WIN.blit(START3, (10, 150))
        pygame.display.update()
        KEY_PRESSED = pygame.key.get_pressed()
        if KEY_PRESSED[pygame.K_SPACE]:
            WIN.fill((0,0,0))
            BEGIN = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                BEGIN = False 
       

def second():
    RUN = True 
    while RUN:
        global TARGET_SIZE
        START = FONT.render('PLEASE SELECT A DIFFICULTY', 1, WHITE)
        WIN.blit(START, (250, 10))
        START2 = FONT.render('FOR EASY PRESS THE KEY 1', 1, WHITE)
        WIN.blit(START2, (250, 100))
        START2 = FONT.render('FOR MEDIUM PRESS THE KEY 2', 1, WHITE)
        WIN.blit(START2, (250, 190))
        START2 = FONT.render('FOR HARD PRESS THE KEY 3', 1, WHITE)
        WIN.blit(START2, (250, 280))
        pygame.display.update()

        KEY_PRESSED = pygame.key.get_pressed()
        if KEY_PRESSED[pygame.K_1]:
            TARGET_SIZE = 30
            RUN = False
        if KEY_PRESSED[pygame.K_2]:
            TARGET_SIZE = 20
            RUN = False
        if KEY_PRESSED[pygame.K_3]:
            TARGET_SIZE = 10
            RUN = False
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False

def third():
    RUN = True 
    while RUN:
        global CLOCK2
        WIN.fill((0,0,0))
        pygame.draw.circle(WIN, (RED), (WID/2,HIG/2),30)
        pygame.display.update()
        pygame.time.wait(1000)
        pygame.draw.circle(WIN, (YELLOW), (WID/2,HIG/2),30)
        pygame.display.update()
        pygame.time.wait(1000)
        pygame.draw.circle(WIN, (GREEN), (WID/2,HIG/2),30)
        pygame.display.update()
        pygame.time.wait(1000)
        CLOCK2 = round(pygame.time.get_ticks()/1000)
        RUN = False



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False 

def forth():
    RUN = True
    while RUN:
        WIN.fill((0,0,0))
        
        global TARGET_X
        global TARGET_Y
        global CLICKS
        global TIME
        global CLOCK
        global CLOCK2
        global MOUSE_X
        global MOUSE_Y
        global TARGETCLICKS

        CLOCK = 15 - (round(pygame.time.get_ticks()/1000) - CLOCK2)
        pygame.draw.rect(WIN, (RED), (TARGET_X,TARGET_Y,TARGET_SIZE,TARGET_SIZE))
        KEY_PRESSED = pygame.mouse.get_pressed()

        TIMER = FONT.render(str(CLOCK), 1, WHITE)
        WIN.blit(TIMER, (WID/2, 50))
        pygame.display.update()

        
        if KEY_PRESSED[0]:
            MOUSE_X,MOUSE_Y = pygame.mouse.get_pos()
            CLICKS = CLICKS + 1
            
            if MOUSE_X >= TARGET_X and MOUSE_X <= (TARGET_X + TARGET_SIZE) and MOUSE_Y >= TARGET_Y and MOUSE_Y <= (TARGET_Y + TARGET_SIZE):
                TARGETCLICKS = TARGETCLICKS + 1 

            pygame.time.wait(100)
            TARGET_X = random.randint(0,WID - TARGET_SIZE)
            TARGET_Y = random.randint(0,HIG - TARGET_SIZE)


        if CLOCK == 0:
            RUN = False 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False 


def fifth():
    RUN = True 
    while RUN:
        global CLICKS
        global TARGETCLICKS
        if TARGETCLICKS == 0:
            TARGETCLICKS = 1

        WIN.fill((0,0,0))
        TITLE = FONT.render('SUMMARY', 1, WHITE)
        WIN.blit(TITLE, (525, 10))

        TARCLICKS = FONT.render('TARGETS HIT:', 1, WHITE)
        WIN.blit(TARCLICKS, (10, 60))
        TARCLICKS1 = FONT.render(str(TARGETCLICKS),1,WHITE)
        WIN.blit(TARCLICKS1, (300, 60))

        NUMCLICKS = FONT.render('TOTAL CLICKS:', 1, WHITE)
        WIN.blit(NUMCLICKS, (10, 110))
        NUMCLICKS1 = FONT.render(str(CLICKS),1,WHITE)
        WIN.blit(NUMCLICKS1, (315, 110))

        TIMECLICKS = FONT.render('SECONDS BETWEEN CLICKS:', 1, WHITE)
        WIN.blit(TIMECLICKS, (10, 160))
        TIMECLICKS1 = FONT.render(str(round(CLICKS/15,2)),1,WHITE)
        WIN.blit(TIMECLICKS1, (600, 160))
        
        ACCURACY = FONT.render('ACCURACY%:', 1, WHITE)
        WIN.blit(ACCURACY, (10, 210))
        ACCURACY_SCORE = FONT.render(str((round(TARGETCLICKS/CLICKS,2)*100)),1,WHITE)
        WIN.blit(ACCURACY_SCORE, (270, 210))


        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False 



        
        
first()

second()     

third()

forth()

fifth()

