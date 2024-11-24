import pygame,sys
import math
import numpy as np
import random

pygame.init()
row_size=6
column_size=7
screen = pygame.display.set_mode(((column_size+8)*100,(row_size+1)*100))
pygame.display.set_caption("Main Menu")
board = np.zeros((row_size, column_size))


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW=(225,225,0)
RED=(225,0,0)
ORANGE=(255,130,71)
PINK=(255,0,255)
BACKGROUND=(83,134,139)

font = pygame.font.Font("font.ttf", 55)

def draw_button(text, rect, color):
    pygame.draw.rect(screen, color, rect)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

def show_play_again():
    play_again_font = pygame.font.Font("font.ttf", 75)
    text = play_again_font.render("再玩一次", True, PINK)
    screen.blit(text, (975, 415))  
    yes_button = pygame.Rect(950, 500, 150, 75)
    no_button = pygame.Rect(1150, 500, 150, 75)
    background1=pygame.Rect(955, 505, 140, 65)
    background2 = pygame.Rect(1155, 505, 140, 65)
    draw_button("", yes_button, WHITE)
    draw_button("是", background1, ORANGE)
    draw_button("", no_button, WHITE)
    draw_button("否", background2, ORANGE)
    pygame.display.update()
    
    return yes_button, no_button

def confirm_choose():
    play_again_font = pygame.font.Font("font.ttf", 75)
    text = play_again_font.render("確認選擇", True, PINK)
    screen.blit(text, (935, 425))  
    yes_button = pygame.Rect(900, 500, 150, 75)
    no_button = pygame.Rect(1125, 500, 150, 75)
    background1=pygame.Rect(905, 505, 140, 65)
    background2=pygame.Rect(1130, 505, 140, 65)
    draw_button("", yes_button, WHITE)
    draw_button("是", background1, ORANGE)
    draw_button("", no_button, WHITE)
    draw_button("否", background2, ORANGE)
    pygame.display.update()
    
    return yes_button, no_button

def show_message(message, font_size):
    font = pygame.font.Font("font.ttf", font_size)
    text = font.render(message, True, (255, 0, 0))
    screen.blit(text, ((screen.get_width() - text.get_width()) // 2, ((screen.get_height() - text.get_height()) // 2)-25))
    pygame.display.flip()
    
def confirm_exit():
    window_width = 400
    window_height = 200
    window_x = (screen.get_width() - window_width) // 2
    window_y = (screen.get_height() - window_height) // 2

    confirm_rect = pygame.Rect(window_x, window_y, window_width, window_height)
    yes_button = pygame.Rect(window_x + 50, window_y + 100, 100, 50)
    no_button = pygame.Rect(window_x + 250, window_y + 100, 100, 50)

    pygame.draw.rect(screen, (200, 200, 200), confirm_rect)
    draw_button("是", yes_button, (0, 255, 0))
    draw_button("否", no_button, (255, 0, 0))
    show_message("離開遊戲", 40)
    pygame.display.update()

    return yes_button, no_button

def draw_item():
    pygame.draw.rect(screen,BACKGROUND,(700,0,1000,800))
    button_width = 200
    button_height = 85
    back_button=pygame.Rect(700,10, button_width, button_height)
    item_1=pygame.Rect(925,100, 300, button_height)
    item_2=pygame.Rect(925,200, 300, button_height)
    item_3=pygame.Rect(925,300, 300, button_height)
    item_4=pygame.Rect(925,400, 300, button_height)
    item_5=pygame.Rect(925,500, 300, button_height)
    background6=pygame.Rect(705,15, button_width-10, button_height-10)
    background1=pygame.Rect(930,105, 290, button_height-10)
    background2=pygame.Rect(930,205, 290, button_height-10)
    background3=pygame.Rect(930,305, 290, button_height-10)
    background4=pygame.Rect(930,405, 290, button_height-10)
    background5=pygame.Rect(930,505, 290, button_height-10)
    draw_button("", back_button, WHITE)
    draw_button("返回", background6, (255,130,71))
    draw_button("", item_1, WHITE)
    draw_button("交換", background1, (255,130,71))
    draw_button("", item_2, WHITE)
    draw_button("連續行動", background2, (255,130,71))
    draw_button("", item_3, WHITE)
    draw_button("刪除棋子", background3, (255,130,71))
    draw_button("", item_4, WHITE)
    draw_button("刪除一行", background4, (255,130,71))
    draw_button("", item_5, WHITE)
    draw_button("刪除一列", background5, (255,130,71))
    pygame.display.update()
    
def whoseturn(turn,check_use_item):
    pygame.draw.rect(screen,BACKGROUND,(700,0,1000,800))
    button_width = 200
    button_height = 85
    font = pygame.font.Font("font.ttf", 85)
    item_button=pygame.Rect(1280,610, button_width, button_height)
    draw_background1=pygame.Rect(1285,615, button_width-10, button_height-10)
    draw_button("", item_button, WHITE)
    draw_button("道具", draw_background1, (255,130,71))
    if(turn==1 and check_use_item==-1):
        text1 = font.render("輪到玩家二", True, PINK, BACKGROUND)
        screen.blit(text1, (825, 150))
    elif(turn==-1 and check_use_item==-1):
        text1 = font.render("輪到玩家一", True, PINK, BACKGROUND)
        screen.blit(text1, (825, 150))
    elif(turn==1 and check_use_item==1):
        text1 = font.render("輪到玩家一", True, PINK, BACKGROUND)
        screen.blit(text1, (825, 150))
    elif(turn==-1 and check_use_item==1):
        text1 = font.render("輪到玩家二", True, PINK, BACKGROUND)
        screen.blit(text1, (825, 150))
    pygame.display.update()
    
def item_number1(turn):
    exchange=[]
    pygame.draw.rect(screen,BACKGROUND,(700,0,1000,800))
    button_width = 200
    button_height = 85
    back_button=pygame.Rect(700,10, button_width, button_height)
    background1=pygame.Rect(705,15, button_width-10, button_height-10)
    draw_button("", back_button, WHITE)
    draw_button("返回", background1, (255,130,71))
    font = pygame.font.Font("font.ttf", 50)
    text1 = font.render("使用道具一:交換", True, PINK, BACKGROUND)
    text2=font.render("選擇兩個棋子", True, PINK, BACKGROUND)
    screen.blit(text1, (875, 100))
    screen.blit(text2, (875, 170))
    pygame.display.update()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    draw_item()
                    return -5,0
                if len(exchange)!=4:
                    y=int((event.pos[1]-100)/100)
                    x=int(event.pos[0]/100)
                    if x<7 and y<8:
                        if board[y][x]!=0:      
                            exchange.append(x)
                            exchange.append(y)
                        else:
                            font = pygame.font.Font("font.ttf", 50)
                            text1 = font.render("這格沒有棋子，重選一個", True, PINK, BACKGROUND)
                            screen.blit(text1, (875, 250))
                            pygame.display.update()
                            pygame.time.wait(2000)
                            text1 = font.render("這格沒有棋子，重選一個", True, BACKGROUND, BACKGROUND)
                            screen.blit(text1, (875, 250))
                            pygame.display.update()
                if len(exchange)==4:
                    position_information=""
                    position_information+="("+str(exchange[0]+1)+","+str(exchange[1]+1)+")"+" 和 "+"("+str(exchange[2]+1)+","+str(exchange[3]+1)+")"
                    font = pygame.font.Font("font.ttf", 50)
                    text1 = font.render("你選擇了 "+position_information, True, PINK, BACKGROUND)
                    screen.blit(text1, (875, 250))
                    pygame.display.update()
                    yes_button, no_button = confirm_choose()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if yes_button.collidepoint(event.pos):
                            temp=board[exchange[1]][exchange[0]]
                            board[exchange[1]][exchange[0]]=board[exchange[3]][exchange[2]]
                            board[exchange[3]][exchange[2]]=temp
                            print_the_piece()
                            pygame.display.update()
                            player,win=check_win(turn)
                            return  player,win
                        elif no_button.collidepoint(event.pos):
                            pygame.draw.rect(screen,BACKGROUND,(700,0,1000,600))
                            draw_button("", back_button, WHITE)
                            draw_button("返回", background1, (255,130,71))
                            font = pygame.font.Font("font.ttf", 50)
                            text1 = font.render("using Item 1:exchange", True, PINK, BACKGROUND)
                            text2=font.render("choose two piece", True, PINK, BACKGROUND)
                            text3=font.render("你可以再選一次", True, PINK, BACKGROUND)
                            screen.blit(text1, (875, 100))
                            screen.blit(text2, (875, 170))
                            screen.blit(text3, (875, 240))
                            pygame.display.update()
                            pygame.time.wait(2000)
                            text3=font.render("你可以再選一次", True, BACKGROUND, BACKGROUND)
                            screen.blit(text3, (875, 240))
                            pygame.display.update()
                            exchange=[]
                            continue
                    
def item_number2(turn):
    continues=[]
    pygame.draw.rect(screen,BACKGROUND,(700,0,1000,800))
    button_width = 200
    button_height = 85
    back_button=pygame.Rect(700,10, button_width, button_height)
    background1=pygame.Rect(705,15, button_width-10, button_height-10)
    draw_button("", back_button, WHITE)
    draw_button("返回", background1, (255,130,71))
    font = pygame.font.Font("font.ttf", 50)
    text1 = font.render("使用道具二:連續行動", True, PINK, BACKGROUND)
    text2=font.render("選兩行", True, PINK, BACKGROUND)
    screen.blit(text1, (875, 100))
    screen.blit(text2, (875, 170))
    pygame.display.update()
    pygame.display.update()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    draw_item()
                    return -5,0   
                if len(continues)!=2:
                    x=int(event.pos[0]/100)
                    if x<7:
                        continues.append(x)
                if len(continues)==2:
                    position_information=""
                    position_information+="行:"+str(continues[0])+" 和 "+str(continues[1])
                    font = pygame.font.Font("font.ttf", 50)
                    text1 = font.render("你選擇了"+position_information, True, PINK, BACKGROUND)
                    screen.blit(text1, (875, 250))
                    pygame.display.update()
                    yes_button, no_button = confirm_choose()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if yes_button.collidepoint(event.pos):
                            place_piece(continues[0],turn)
                            place_piece(continues[1],turn)
                            print_the_piece()
                            pygame.display.update()
                            player,win=check_win(turn)
                            return  player,win
                        elif no_button.collidepoint(event.pos):
                            pygame.draw.rect(screen,BACKGROUND,(700,0,1000,600))
                            draw_button("", back_button, WHITE)
                            draw_button("返回", background1, (255,130,71))
                            font = pygame.font.Font("font.ttf", 50)
                            text1 = font.render("使用道具二:連續行動", True, PINK, BACKGROUND)
                            text2=font.render("選兩行", True, PINK, BACKGROUND)
                            text3=font.render("你可以再選一次", True, PINK, BACKGROUND)
                            screen.blit(text1, (875, 100))
                            screen.blit(text2, (875, 170))
                            screen.blit(text3, (875, 240))
                            pygame.display.update()
                            pygame.time.wait(2000)
                            text3=font.render("你可以再選一次", True, BACKGROUND, BACKGROUND)
                            screen.blit(text3, (875, 240))
                            pygame.display.update()
                            continues=[]
                            continue
                    
def item_number3(turn):
    delete=[]
    pygame.draw.rect(screen,BACKGROUND,(700,0,1000,800))
    button_width = 200
    button_height = 85
    back_button=pygame.Rect(700,10, button_width, button_height)
    background1=pygame.Rect(705,15, button_width-10, button_height-10)
    draw_button("", back_button, WHITE)
    draw_button("返回", background1, (255,130,71))
    font = pygame.font.Font("font.ttf", 50)
    text1 = font.render("使用道具三:刪除棋子", True, PINK, BACKGROUND)
    text2=font.render("選一個棋子", True, PINK, BACKGROUND)
    screen.blit(text1, (875, 100))
    screen.blit(text2, (875, 170))
    pygame.display.update()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    draw_item()
                    return -5,0   
                if len(delete)!=2:
                    x=int(event.pos[0]/100)
                    y=int((event.pos[1]-100)/100)
                    if x<7 and y<8:
                        if board[y][x]!=0:      
                            delete.append(x)
                            delete.append(y)
                        else:
                            font = pygame.font.Font("font.ttf", 50)
                            text1 = font.render("這格沒有棋子，重選一個", True, PINK, BACKGROUND)
                            screen.blit(text1, (875, 250))
                            pygame.display.update()
                            pygame.time.wait(2000)
                            text1 = font.render("這格沒有棋子，重選一個", True, BACKGROUND, BACKGROUND)
                            screen.blit(text1, (875, 250))
                            pygame.display.update()
                if len(delete)==2:
                    position_information=""
                    position_information+="("+str(delete[0]+1)+","+str(delete[1]+1)+") 上的棋子"
                    font = pygame.font.Font("font.ttf", 50)
                    text1 = font.render("你選擇了 "+position_information, True, PINK, BACKGROUND)
                    screen.blit(text1, (875, 250))
                    pygame.display.update()
                    yes_button, no_button = confirm_choose()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if yes_button.collidepoint(event.pos):
                            board[y][x]=0
                            print_the_piece()
                            pygame.display.update()
                            pygame.time.wait(2000)
                            for i in range(delete[1],0,-1):
                                board[i][delete[0]]=board[i-1][delete[0]]
                            board[0][delete[0]]=0
                            print_the_piece()
                            pygame.display.update()
                            player,win=check_win(-2)
                            return  player,win
                        elif no_button.collidepoint(event.pos):
                            pygame.draw.rect(screen,BACKGROUND,(700,0,1000,600))
                            draw_button("", back_button, WHITE)
                            draw_button("返回", background1, (255,130,71))
                            font = pygame.font.Font("font.ttf", 50)
                            text1 = font.render("使用道具三:刪除棋子", True, PINK, BACKGROUND)
                            text2=font.render("選一個棋子", True, PINK, BACKGROUND)
                            text3=font.render("你可以再選一次", True, PINK, BACKGROUND)
                            screen.blit(text1, (875, 100))
                            screen.blit(text2, (875, 170))
                            screen.blit(text3, (875, 240))
                            pygame.display.update()
                            pygame.time.wait(2000)
                            text3=font.render("你可以再選一次", True, BACKGROUND, BACKGROUND)
                            screen.blit(text3, (875, 240))
                            pygame.display.update()
                            delete=[]
                            continue
                        
def item_number4(turn):
    delete_column=[]
    pygame.draw.rect(screen,BACKGROUND,(700,0,1000,800))
    button_width = 200
    button_height = 85
    back_button=pygame.Rect(700,10, button_width, button_height)
    background1=pygame.Rect(705,15, button_width-10, button_height-10)
    draw_button("", back_button, WHITE)
    draw_button("返回", background1, (255,130,71))
    font = pygame.font.Font("font.ttf", 50)
    text1 = font.render("使用道具四:刪除一行", True, PINK, BACKGROUND)
    text2=font.render("選擇一行", True, PINK, BACKGROUND)
    screen.blit(text1, (875, 100))
    screen.blit(text2, (875, 170))
    pygame.display.update()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    draw_item()
                    return -5,0   
                if len(delete_column)!=1:
                    x=int(event.pos[0]/100)
                    if x<7:
                        flag=1
                        for i in range(6):
                            if board[i][x]!=0:
                                flag=0
                                break
                        if flag==0:
                            delete_column.append(x)
                        else:
                            font = pygame.font.Font("font.ttf", 50)
                            text1 = font.render("這一行沒有棋子，重選一次", True, PINK, BACKGROUND)
                            screen.blit(text1, (750, 250))
                            pygame.display.update()
                            pygame.time.wait(2000)
                            text1 = font.render("這一行沒有棋子，重選一次", True, BACKGROUND, BACKGROUND)
                            screen.blit(text1, (750, 250))
                            pygame.display.update()
                if len(delete_column)==1:
                    position_information=""
                    position_information+="行:"+str(delete_column[0]+1)
                    font = pygame.font.Font("font.ttf", 50)
                    text1 = font.render("你選擇了 "+position_information, True, PINK, BACKGROUND)
                    screen.blit(text1, (875, 250))
                    pygame.display.update()
                    yes_button, no_button = confirm_choose()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if yes_button.collidepoint(event.pos):
                            for i in range(row_size):
                                board[i][delete_column[0]]=0
                            print_the_piece()
                            pygame.display.update()
                            player,win=check_win(turn)
                            return  player,win
                        elif no_button.collidepoint(event.pos):
                            pygame.draw.rect(screen,BACKGROUND,(700,0,1000,600))
                            draw_button("", back_button, WHITE)
                            draw_button("返回", background1, (255,130,71))
                            font = pygame.font.Font("font.ttf", 50)
                            text1 = font.render("使用道具四:刪除一行", True, PINK, BACKGROUND)
                            text2=font.render("選擇一行", True, PINK, BACKGROUND)
                            text3=font.render("你可以再選一次", True, PINK, BACKGROUND)
                            screen.blit(text1, (875, 100))
                            screen.blit(text2, (875, 170))
                            screen.blit(text3, (875, 240))
                            pygame.display.update()
                            pygame.time.wait(2000)
                            text3=font.render("你可以再選一次", True, BACKGROUND, BACKGROUND)
                            screen.blit(text3, (875, 240))
                            pygame.display.update()
                            delete_column=[]
                            continue
                        
def item_number5(turn):
    delete_row=[]
    pygame.draw.rect(screen,BACKGROUND,(700,0,1000,800))
    button_width = 200
    button_height = 85
    back_button=pygame.Rect(700,10, button_width, button_height)
    background1=pygame.Rect(705,15, button_width-10, button_height-10)
    draw_button("", back_button, WHITE)
    draw_button("返回", background1, (255,130,71))
    font = pygame.font.Font("font.ttf", 50)
    text1 = font.render("使用道具五:刪除一列", True, PINK, BACKGROUND)
    text2=font.render("選擇一列", True, PINK, BACKGROUND)
    screen.blit(text1, (875, 100))
    screen.blit(text2, (875, 170))
    pygame.display.update()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    draw_item()
                    return -5,0  
                if len(delete_row)!=1:
                    y=int(event.pos[1]/100)
                    if y<7 and y>=1:
                        flag=1
                        for i in range(7):
                            if board[y-1][i]!=0:
                                flag=0
                                break
                        if flag==0:
                            delete_row.append(y)
                        else:
                            font = pygame.font.Font("font.ttf", 50)
                            text1 = font.render("這一列沒有棋子，重選一次", True, PINK, BACKGROUND)
                            screen.blit(text1, (750, 250))
                            pygame.display.update()
                            pygame.time.wait(2000)
                            text1 = font.render("這一列沒有棋子，重選一次", True, BACKGROUND, BACKGROUND)
                            screen.blit(text1, (750, 250))
                            pygame.display.update()
                if len(delete_row)==1:
                    position_information=""
                    position_information+="列:"+str(delete_row[0])
                    font = pygame.font.Font("font.ttf", 50)
                    text1 = font.render("你選擇了 "+position_information, True, PINK, BACKGROUND)
                    screen.blit(text1, (875, 250))
                    pygame.display.update()
                    yes_button, no_button = confirm_choose()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if yes_button.collidepoint(event.pos):
                            for i in range(column_size):
                                for j in range(delete_row[0]-1,0,-1):
                                    board[j][i]=board[j-1][i]
                                board[j-1][i]=0
                            print_the_piece()
                            pygame.display.update()
                            player,win=check_win(turn)
                            return  player,win
                        elif no_button.collidepoint(event.pos):
                            pygame.draw.rect(screen,BACKGROUND,(700,0,1000,600))
                            draw_button("", back_button, WHITE)
                            draw_button("返回", background1, (255,130,71))
                            font = pygame.font.Font("font.ttf", 50)
                            text1 = font.render("使用道具五:刪除一列", True, PINK, BACKGROUND)
                            text2=font.render("選擇一列", True, PINK, BACKGROUND)
                            text3=font.render("你可以再選一次", True, PINK, BACKGROUND)
                            screen.blit(text1, (875, 100))
                            screen.blit(text2, (875, 170))
                            screen.blit(text3, (875, 240))
                            pygame.display.update()
                            pygame.time.wait(2000)
                            text3=font.render("你可以再選一次", True, BACKGROUND, BACKGROUND)
                            screen.blit(text3, (875, 240))
                            pygame.display.update()
                            delete_row=[]
                            continue
def randomevent(turn):
    pygame.draw.rect(screen,BACKGROUND,(700,0,1000,800))
    event=random.randint(1,3)
    block=[-1,-1]
    if event==1:
        pos=[]
        temp=[]
        font = pygame.font.Font("font.ttf", 50)
        text1 = font.render("隨機事件", True, PINK, BACKGROUND)
        text2=font.render("隨機刪除一個棋子", True, PINK, BACKGROUND)
        screen.blit(text1, (875, 100))
        screen.blit(text2, (875, 170))
        pygame.display.update()
        pygame.time.wait(2000)
        for i in range(5,0,-1):
            for j in range(6,0,-1):
                if board[i][j]!=0:
                    temp.append(j)
                    temp.append(i)
                    pos.append(temp)
                    temp=[]
        choose=random.randint(0,len(pos)-1)
        x=pos[choose][0]
        y=pos[choose][1]
        message="刪除在 ("+str(x+1)+","+str(y+1)+") 上的棋子"
        text3=font.render(message, True, PINK, BACKGROUND)
        screen.blit(text3, (875, 240))
        board[y][x]=0
        print_the_piece()
        pygame.display.update()
        pygame.time.wait(2000)
        for i in range(y,0,-1):
            board[i][x]=board[i-1][x]
        board[0][x]=0
        pygame.draw.rect(screen,BACKGROUND,(700,0,1000,800))
        if turn==1:
            font = pygame.font.Font("font.ttf", 85)
            text1 = font.render("輪到玩家二", True, PINK, BACKGROUND)
            screen.blit(text1, (825, 150))
        elif turn==-1:
            font = pygame.font.Font("font.ttf", 85)
            text1 = font.render("輪到玩家一", True, PINK, BACKGROUND)
            screen.blit(text1, (825, 150))
        print_the_piece()
        pygame.display.update()
        player,win=check_win(-2)
        return win,0,block
    if event==2:
        font = pygame.font.Font("font.ttf", 50)
        text1 = font.render("隨機事件", True, PINK, BACKGROUND)
        text2=font.render("跳過一個玩家的回合", True, PINK, BACKGROUND)
        screen.blit(text1, (875, 100))
        screen.blit(text2, (875, 170))
        pygame.display.update()
        pygame.time.wait(2000)
        skip=random.randint(1,2)
        if skip==1:
            message="跳過玩家一的回合"
        elif skip==2:
            message="跳過玩家二的回合"
        text3=font.render(message, True, PINK, BACKGROUND)
        screen.blit(text3, (875, 240))
        pygame.display.update()
        pygame.time.wait(2000)
        text1 = font.render("隨機事件", True, BACKGROUND, BACKGROUND)
        text2=font.render("跳過一個玩家的回合", True, BACKGROUND, BACKGROUND)
        text3=font.render(message, True, BACKGROUND, BACKGROUND)
        screen.blit(text1, (875, 100))
        screen.blit(text2, (875, 170))
        screen.blit(text3, (875, 240))
        pygame.display.update()
        return 0,skip,block
    if event==3:
        block=[]
        font = pygame.font.Font("font.ttf", 50)
        text1 = font.render("隨機事件", True, PINK, BACKGROUND)
        text2=font.render("封鎖下棋位置", True, PINK, BACKGROUND)
        screen.blit(text1, (875, 100))
        screen.blit(text2, (875, 170))
        pygame.display.update()
        pygame.time.wait(2000)
        while(True):
            block.append(random.randint(0,6))
            if (len(block)==2 and block[0]==block[1]):
                block=[]
            elif (len(block)==2 and block[0]!=block[1]):
                break
        block.sort()
        message="封鎖行:"+str(block[0]+1)+" 和 "+str(block[1]+1)
        text3=font.render(message, True, PINK, BACKGROUND)
        screen.blit(text3, (875, 240))
        pygame.display.update()
        pygame.time.wait(2000)
        text1 = font.render("隨機事件", True, BACKGROUND, BACKGROUND)
        text2=font.render("封鎖下棋位置", True, BACKGROUND, BACKGROUND)
        text3=font.render(message, True, BACKGROUND, BACKGROUND)
        screen.blit(text1, (875, 100))
        screen.blit(text2, (875, 170))
        screen.blit(text3, (875, 240))
        font=pygame.font.SysFont("arial",50)
        for i in range(7):
            if i==block[0] or i==block[1]:
                number=font.render(str(i+1),True,RED,WHITE)
                screen.blit(number,(35+i*100,25))
        if turn==1:
            font = pygame.font.Font("font.ttf", 85)
            text1 = font.render("輪到玩家二", True, PINK, BACKGROUND)
            screen.blit(text1, (825, 150))
        elif turn==-1:
            font = pygame.font.Font("font.ttf", 85)
            text1 = font.render("輪到玩家一", True, PINK, BACKGROUND)
            screen.blit(text1, (825, 150))
        pygame.display.update()
        return 0,0,block
    
def print_the_piece():
    for i in range(row_size):
        for j in range(column_size):
            if board[i][j] == 1:
                pygame.draw.circle(screen, YELLOW, (j * 100 + 50, (i + 1) * 100 + 50), 45)
            elif board[i][j] == 2:
                pygame.draw.circle(screen, RED, (j * 100 + 50, (i + 1) * 100 + 50), 45)
            elif board[i][j]==0:
                pygame.draw.circle(screen, BLACK, (j * 100 + 50, (i + 1) * 100 + 50), 45)
                
def item(turn):
    pygame.draw.rect(screen,BACKGROUND,(700,0,1000,800))
    button_width = 200
    button_height = 85
    back_button=pygame.Rect(700,10, button_width, button_height)
    item_1=pygame.Rect(925,100, 300, button_height)
    item_2=pygame.Rect(925,200, 300, button_height)
    item_3=pygame.Rect(925,300, 300, button_height)
    item_4=pygame.Rect(925,400, 300, button_height)
    item_5=pygame.Rect(925,500, 300, button_height)
    background6=pygame.Rect(705,15, button_width-10, button_height-10)
    background1=pygame.Rect(930,105, 290, button_height-10)
    background2=pygame.Rect(930,205, 290, button_height-10)
    background3=pygame.Rect(930,305, 290, button_height-10)
    background4=pygame.Rect(930,405, 290, button_height-10)
    background5=pygame.Rect(930,505, 290, button_height-10)
    draw_button("", back_button, WHITE)
    draw_button("返回", background6, (255,130,71))
    draw_button("", item_1, WHITE)
    draw_button("交換", background1, (255,130,71))
    draw_button("", item_2, WHITE)
    draw_button("連續行動", background2, (255,130,71))
    draw_button("", item_3, WHITE)
    draw_button("刪除棋子", background3, (255,130,71))
    draw_button("", item_4, WHITE)
    draw_button("刪除一行", background4, (255,130,71))
    draw_button("", item_5, WHITE)
    draw_button("刪除一列", background5, (255,130,71))
    pygame.display.update()
    running = True
    check_use_item=1
    while running:
        check_use_item=1
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if item_1.collidepoint(event.pos):
                    player,win=item_number1(turn)
                    check_use_item=-1
                    if check_use_item==-1 and player!=-5:
                        whoseturn(turn,check_use_item)
                        running = False
                        return turn*check_use_item,win
                    elif player==-5:
                        continue
                elif item_2.collidepoint(event.pos):
                    player,win=item_number2(turn)
                    check_use_item=-1
                    if check_use_item==-1 and player!=-5:
                        whoseturn(turn,check_use_item)
                        running = False
                        return turn*check_use_item,win
                    elif player==-5:
                        continue
                elif item_3.collidepoint(event.pos):
                    player,win=item_number3(turn)
                    check_use_item=-1
                    if check_use_item==-1 and player!=-5:
                        whoseturn(turn,check_use_item)
                        running = False
                        return turn*check_use_item,win
                    elif player==-5:
                        continue
                elif item_4.collidepoint(event.pos):
                    player,win=item_number4(turn)
                    check_use_item=-1
                    if check_use_item==-1 and player!=-5:
                        whoseturn(turn,check_use_item)
                        running = False
                        return turn*check_use_item,win
                    elif player==-5:
                        continue
                elif item_5.collidepoint(event.pos):
                    player,win=item_number5(turn)
                    check_use_item=-1
                    if check_use_item==-1 and player!=-5:
                        whoseturn(turn,check_use_item)
                        running = False
                        return turn*check_use_item,win
                    elif player==-5:
                        continue
                elif back_button.collidepoint(event.pos):
                    whoseturn(turn,check_use_item)
                    running = False
                    return turn*1,0

def win_message(player):
    if player == 1:
        pygame.draw.rect(screen,BACKGROUND,(700,0,1000,800))
        pygame.display.update()
        font = pygame.font.Font("font.ttf", 100)
        number1 = font.render("玩家一獲勝", True, PINK, BACKGROUND)
        screen.blit(number1, (850, 275))
        return 
    elif player==2:
        pygame.draw.rect(screen,BACKGROUND,(700,0,1000,800))
        pygame.display.update()
        font = pygame.font.Font("font.ttf", 100)
        number1 = font.render("玩家二獲勝", True, PINK, BACKGROUND)
        screen.blit(number1, (850, 275))
        return 

def place_piece(column,player):
    flag=1
    position=[]
    for i in range(row_size-1,-1,-1):
        if board[i][column]==0:
            flag=1
            break
        elif board[i][column]==1 or board[i][column]==2:
            flag=0
    if flag==1:
        for i in range(row_size-1,-1,-1):
            if(board[i][column]==0 and player==1):
                board[i][column]=1
                position.append(i)
                position.append(column)
                return position
            elif(board[i][column]==0 and player==-1):
                board[i][column]=2
                position.append(i)
                position.append(column)
                return position
    else:
        position.append(-1)
        return position
    
def check_win(player):
    time=0
    for i in range(6): 
        for j in range(7):
            if board[i][j]!=0:
                time+=1
    if time==42:
        return -1,1
    if(player==1):
        for i in range(6): 
            for j in range(7):
                if j+1<7 and j+2<7 and j+3<7:
                    if board[i][j]==1 and board[i][j+1]==1 and board[i][j+2]==1 and board[i][j+3]==1:
                        return 1,1
            
        for i in range(6):
            for j in range(7):
                if i+1<6 and i+2<6 and i+3<6:
                    if board[i][j]==1 and board[i+1][j]==1 and board[i+2][j]==1 and board[i+3][j]==1:
                        return 1,1
                    
        for i in range(6):
            for j in range(7):
                if i+1<6 and i+2<6 and i+3<6 and j+1<7 and j+2<7 and j+3<7:
                    if board[i][j]==1 and board[i+1][j+1]==1 and board[i+2][j+2]==1 and board[i+3][j+3]==1:
                        return 1,1         

        for i in range(6):
            for j in range(7):
                if i+1<6 and i+2<6 and i+3<6 and j-1>=0 and j-2>=0 and j-3>=0:
                    if board[i][j]==1 and board[i+1][j-1]==1 and board[i+2][j-2]==1 and board[i+3][j-3]==1:
                        return 1,1
                    
    if(player==-1):
        for i in range(6): 
            for j in range(7):
                if j+1<7 and j+2<7 and j+3<7:
                    if board[i][j]==2 and board[i][j+1]==2 and board[i][j+2]==2 and board[i][j+3]==2:
                        return 2,1
            
        for i in range(6):
            for j in range(7):
                if i+1<6 and i+2<6 and i+3<6:
                    if board[i][j]==2 and board[i+1][j]==2 and board[i+2][j]==2 and board[i+3][j]==2:
                        return 2,1
                    
        for i in range(6):
            for j in range(7):
                if i+1<6 and i+2<6 and i+3<6 and j+1<7 and j+2<7 and j+3<7:
                    if board[i][j]==2 and board[i+1][j+1]==2 and board[i+2][j+2]==2 and board[i+3][j+3]==2:
                        return 2,1         

        for i in range(6):
            for j in range(7):
                if i+1<6 and i+2<6 and i+3<6 and j-1>=0 and j-2>=0 and j-3>=0:
                    if board[i][j]==2 and board[i+1][j-1]==2 and board[i+2][j-2]==2 and board[i+3][j-3]==2:
                        return 2,1  
    if(player==-2):
        for i in range(6): 
            for j in range(7):
                if j+1<7 and j+2<7 and j+3<7:
                    if board[i][j]==1 and board[i][j+1]==1 and board[i][j+2]==1 and board[i][j+3]==1:
                        return 1,1
            
        for i in range(6):
            for j in range(7):
                if i+1<6 and i+2<6 and i+3<6:
                    if board[i][j]==1 and board[i+1][j]==1 and board[i+2][j]==1 and board[i+3][j]==1:
                        return 1,1
                    
        for i in range(6):
            for j in range(7):
                if i+1<6 and i+2<6 and i+3<6 and j+1<7 and j+2<7 and j+3<7:
                    if board[i][j]==1 and board[i+1][j+1]==1 and board[i+2][j+2]==1 and board[i+3][j+3]==1:
                        return 1,1         

        for i in range(6):
            for j in range(7):
                if i+1<6 and i+2<6 and i+3<6 and j-1>=0 and j-2>=0 and j-3>=0:
                    if board[i][j]==1 and board[i+1][j-1]==1 and board[i+2][j-2]==1 and board[i+3][j-3]==1:
                        return 1,1
        for i in range(6): 
            for j in range(7):
                if j+1<7 and j+2<7 and j+3<7:
                    if board[i][j]==2 and board[i][j+1]==2 and board[i][j+2]==2 and board[i][j+3]==2:
                        return 2,1
            
        for i in range(6):
            for j in range(7):
                if i+1<6 and i+2<6 and i+3<6:
                    if board[i][j]==2 and board[i+1][j]==2 and board[i+2][j]==2 and board[i+3][j]==2:
                        return 2,1
                    
        for i in range(6):
            for j in range(7):
                if i+1<6 and i+2<6 and i+3<6 and j+1<7 and j+2<7 and j+3<7:
                    if board[i][j]==2 and board[i+1][j+1]==2 and board[i+2][j+2]==2 and board[i+3][j+3]==2:
                        return 2,1         

        for i in range(6):
            for j in range(7):
                if i+1<6 and i+2<6 and i+3<6 and j-1>=0 and j-2>=0 and j-3>=0:
                    if board[i][j]==2 and board[i+1][j-1]==2 and board[i+2][j-2]==2 and board[i+3][j-3]==2:
                        return 2,1  
                    
    return 0,0
def draw_the_board(board,confirm,turn,mode):
        screen.fill(BACKGROUND)
        font=pygame.font.Font("font.ttf",85)
        if confirm==1 and turn==1:
            text1 = font.render("輪到玩家一", True, PINK,BACKGROUND)             
            screen.blit(text1,(825,150))
        elif confirm==0 and turn==1:
            text1 = font.render("輪到玩家一", True, PINK,BACKGROUND)             
            screen.blit(text1,(825,150))
        elif confirm==0 and turn==-1:
            text1 = font.render("輪到玩家二", True, PINK,BACKGROUND)             
            screen.blit(text1,(825,150))
        pygame.draw.rect(screen,WHITE,(0,0,(row_size+1)*100,column_size*100+150))
        pygame.draw.rect(screen,BLUE,(0,100,(row_size+1)*100,column_size*100+150))
        for i in range(row_size+1):
            for j in range(column_size):
                pygame.draw.circle(screen,(0,0,0),(i*100+50,(j+1)*100+50),45)
        for i in range(100,700,100):
            pygame.draw.line(screen,BLUE, (i, 100), (i, 0), 3)

        button_width = 200
        button_height = 85
        if mode==2:
            item_button=pygame.Rect(1280,610, button_width, button_height)
            draw_background1=pygame.Rect(1285,615, button_width-10, button_height-10)
            draw_button("", item_button, WHITE)
            draw_button("道具", draw_background1, (255,130,71))

            
def show_number(board):
    font=pygame.font.SysFont("arial",50)
    number1=font.render("1",True,(131,111,255),WHITE)
    number2=font.render("2",True,(131,111,255),WHITE)
    number3=font.render("3",True,(131,111,255),WHITE)
    number4=font.render("4",True,(131,111,255),WHITE)
    number5=font.render("5",True,(131,111,255),WHITE)
    number6=font.render("6",True,(131,111,255),WHITE)
    number7=font.render("7",True,(131,111,255),WHITE)
    screen.blit(number1,(35,25))
    screen.blit(number2,(135,25))
    screen.blit(number3,(235,25))
    screen.blit(number4,(335,25))
    screen.blit(number5,(435,25))
    screen.blit(number6,(535,25))
    screen.blit(number7,(635,25))
    
def show_cannot_place():
    font=pygame.font.Font("font.ttf",85)
    text1 = font.render("AAAAAAAAAAAAAAAAAAAAA", True, BACKGROUND, BACKGROUND)
    screen.blit(text1,(825,275))
    pygame.display.update()
    text1 = font.render("這行已滿!", True, PINK,BACKGROUND)
    screen.blit(text1,(825,275))
    pygame.display.update()
    pygame.time.wait(2000)
    text2=font.render("這行已滿!",True,BACKGROUND,BACKGROUND)
    screen.blit(text2,(825,275))
    pygame.display.update()
    
def draw_message():
    font = pygame.font.Font("font.ttf", 100)
    number1 = font.render("平手", True, PINK, BACKGROUND)
    screen.blit(number1, (850, 275))
    return 

def mode_select():
    while True:
        screen.fill(BACKGROUND)
        classic_mode=pygame.Rect(200,450,300,65)
        item_mode=pygame.Rect(600,450,300,65)
        event_mode=pygame.Rect(1000,450,300,65)
        back_button=pygame.Rect(10,10,150,65)
        draw_background1=pygame.Rect(15,15,140,55)
        draw_background2=pygame.Rect(205,455,290,55)
        draw_background3=pygame.Rect(605,455,290,55)
        draw_background4=pygame.Rect(1005,455,290,55)
        image=pygame.image.load("mode1.png")
        image = pygame.transform.scale(image, (300,300))
        screen.blit(image,(200,145))
        image1=pygame.image.load("mode2.png")
        image1 = pygame.transform.scale(image1, (300,300))
        screen.blit(image1,(600,145))
        image2=pygame.image.load("mode3.png")
        image2 = pygame.transform.scale(image2, (300,300))
        screen.blit(image2,(1000,145))
        draw_button('', classic_mode, WHITE)
        draw_button('經典模式', draw_background2, (255,130,71))
        draw_button('', item_mode, WHITE)
        draw_button('道具模式', draw_background3, (255,130,71))
        draw_button('', back_button, WHITE)
        draw_button('返回',draw_background1,(255,130,71))
        draw_button('', event_mode, WHITE)
        draw_button('事件模式',draw_background4,(255,130,71))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if classic_mode.collidepoint(event.pos):
                    play_classic_mode()
                elif item_mode.collidepoint(event.pos):
                    play_item_mode()
                elif event_mode.collidepoint(event.pos):
                    play_event_mode()
                elif back_button.collidepoint(event.pos):
                    return
def play_classic_mode():
    for i in range(6):
        for j in range(7):
            board[i][j]=0
    turn = 1
    screen = pygame.display.set_mode(((column_size + 8) * 100, (row_size + 1) * 100))
    confirm=1
    draw_the_board(board,confirm,turn,1)
    show_number(board)
    pygame.display.set_caption("Connect 4")
    pygame.display.update()
    player1_win = 0
    player2_win = 0
    confirm_exit_flag = False
    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    yes_button, no_button = confirm_exit()
                    confirm_exit_flag = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if confirm_exit_flag:
                    if yes_button.collidepoint(event.pos):
                        return
                    elif no_button.collidepoint(event.pos):
                        confirm_exit_flag = False
                        confirm=0
                        draw_the_board(board,confirm,turn,1)
                        show_number(board)
                        pygame.display.update()
                        print_the_piece()
                        pygame.display.update()
                else:
                    if turn == 1:
                        posx = event.pos[0]
                        if posx <= 700:
                            column = int(math.ceil(posx / 100))
                            pos = place_piece(column - 1, turn)
                            if pos[0] != -1:
                                font = pygame.font.Font("font.ttf", 85)
                                text1 = font.render("輪到玩家二", True, PINK, BACKGROUND)
                                screen.blit(text1, (825, 150))
                                pygame.display.update()
                                pygame.draw.circle(screen, YELLOW, (pos[1] * 100 + 50, (pos[0] + 1) * 100 + 50), 45)
                                player1_win,win = check_win(turn)
                            else:
                                show_cannot_place()
                            if player1_win==-1:
                                draw_message()
                                while True:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            pygame.quit()
                                            sys.exit()
                                        elif event.type == pygame.MOUSEBUTTONDOWN:
                                            if yes_button.collidepoint(event.pos):
                                                play_classic_mode()
                                            elif no_button.collidepoint(event.pos):
                                                return
                            elif player1_win == 1:
                                win_message(player1_win)
                                pygame.display.update()
                                yes_button, no_button = show_play_again()
                                while True:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            pygame.quit()
                                            sys.exit()
                                        elif event.type == pygame.MOUSEBUTTONDOWN:
                                            if yes_button.collidepoint(event.pos):
                                                play_classic_mode()
                                            elif no_button.collidepoint(event.pos):
                                                return
                            if pos[0] != -1:
                                turn *= -1
                            else:
                                turn = 1
                    elif turn == -1:
                        posx = event.pos[0]
                        if posx <= 700:
                            column = int(math.ceil(posx / 100))
                            pos = place_piece(column - 1, turn)
                            if pos[0] != -1:
                                font = pygame.font.Font("font.ttf",85)
                                text1 = font.render("輪到玩家二", True, BLACK, BACKGROUND)
                                screen.blit(text1, (825,150))
                                font = pygame.font.Font("font.ttf", 85)
                                text1 = font.render("輪到玩家一", True, (255,0,255), BACKGROUND)
                                screen.blit(text1, (825,150))
                                pygame.display.update()
                                pygame.draw.circle(screen,RED, (pos[1]*100+ 50,(pos[0]+1)*100+50),45)
                                player2_win,win = check_win(turn)
                            else:
                                show_cannot_place()
                            if player2_win==-1:
                                draw_message()
                                while True:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            pygame.quit()
                                            sys.exit()
                                        elif event.type == pygame.MOUSEBUTTONDOWN:
                                            if yes_button.collidepoint(event.pos):
                                                play_classic_mode()
                                            elif no_button.collidepoint(event.pos):
                                                return
                            elif player2_win == 2:
                                win_message(player2_win)
                                pygame.display.update()
                                yes_button, no_button = show_play_again()
                                while True:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            pygame.quit()
                                            sys.exit()
                                        elif event.type == pygame.MOUSEBUTTONDOWN:
                                            if yes_button.collidepoint(event.pos):
                                                play_classic_mode()
                                            elif no_button.collidepoint(event.pos):
                                                return
                            if pos[0] != -1:
                                turn *= -1
                            else:
                                turn = -1
            pygame.display.update()
            
def play_item_mode():
    for i in range(6):
        for j in range(7):
            board[i][j]=0
    turn = 1
    screen = pygame.display.set_mode(((column_size + 8) * 100, (row_size + 1) * 100))
    confirm=1
    draw_the_board(board,confirm,turn,2)
    show_number(board)
    pygame.display.set_caption("Connect 4")
    pygame.display.update()
    player1_win = 0
    player2_win = 0
    confirm_exit_flag = False
    game = True
    button_width = 200
    button_height = 85
    item_button=pygame.Rect(1280,640, button_width, button_height)
    
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    yes_button, no_button = confirm_exit()
                    confirm_exit_flag = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if confirm_exit_flag:
                    if yes_button.collidepoint(event.pos):
                        return
                    elif no_button.collidepoint(event.pos):
                        confirm_exit_flag = False
                        confirm=0
                        draw_the_board(board,confirm,turn,2)
                        show_number(board)
                        pygame.display.update()
                        print_the_piece()
                        pygame.display.update()
                else:
                    if turn == 1:
                        skip=0
                        if item_button.collidepoint(event.pos):
                            skip=1
                            turn,win=item(turn)
                            if win!=0:
                                win_message(win)
                                yes_button, no_button = show_play_again()
                                while True:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            pygame.quit()
                                            sys.exit()
                                        elif event.type == pygame.MOUSEBUTTONDOWN:
                                            if yes_button.collidepoint(event.pos):
                                                play_item_mode()
                                            elif no_button.collidepoint(event.pos):
                                                return   
                        if skip!=1:
                            posx = event.pos[0]
                            if posx <= 700:
                                column = int(math.ceil(posx / 100))
                                pos = place_piece(column - 1, turn)
                                if pos[0] != -1:
                                    font = pygame.font.Font("font.ttf", 85)
                                    text1 = font.render("輪到玩家二", True, PINK, BACKGROUND)
                                    screen.blit(text1, (825, 150))
                                    pygame.display.update()
                                    pygame.draw.circle(screen, YELLOW, (pos[1] * 100 + 50, (pos[0] + 1) * 100 + 50), 45)
                                    player1_win,win = check_win(turn)
                                else:
                                    show_cannot_place()
                                if player1_win==-1:
                                    draw_message()
                                    while True:
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                pygame.quit()
                                                sys.exit()
                                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                                if yes_button.collidepoint(event.pos):
                                                    play_item_mode()
                                                elif no_button.collidepoint(event.pos):
                                                    return
                                elif player1_win == 1:
                                    win_message(player1_win)
                                    pygame.display.update()
                                    yes_button, no_button = show_play_again()
                                    while True:
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                pygame.quit()
                                                sys.exit()
                                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                                if yes_button.collidepoint(event.pos):
                                                    play_item_mode()
                                                elif no_button.collidepoint(event.pos):
                                                    return
                                if pos[0] != -1:
                                    turn *= -1
                                else:
                                    turn = 1
                    elif turn == -1:
                        skip=0
                        if item_button.collidepoint(event.pos):
                            skip=1
                            turn,win=item(turn)
                            if win!=0:
                                win_message(win)
                                yes_button, no_button = show_play_again()
                                while True:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            pygame.quit()
                                            sys.exit()
                                        elif event.type == pygame.MOUSEBUTTONDOWN:
                                            if yes_button.collidepoint(event.pos):
                                                play_item_mode()
                                            elif no_button.collidepoint(event.pos):
                                                return
                        if skip!=1:
                            posx = event.pos[0]
                            if posx <= 700:
                                column = int(math.ceil(posx / 100))
                                pos = place_piece(column - 1, turn)
                                if pos[0] != -1:
                                    font = pygame.font.Font("font.ttf",85)
                                    text1 = font.render("輪到玩家二", True, BLACK, BACKGROUND)
                                    screen.blit(text1, (825,150))
                                    font = pygame.font.Font("font.ttf", 85)
                                    text1 = font.render("輪到玩家一", True, (255,0,255), BACKGROUND)
                                    screen.blit(text1, (825,150))
                                    pygame.display.update()
                                    pygame.draw.circle(screen,RED, (pos[1]*100+ 50,(pos[0]+1)*100+50),45)
                                    player2_win,win = check_win(turn)
                                else:
                                    show_cannot_place()
                                if player2_win==-1:
                                    draw_message()
                                    while True:
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                pygame.quit()
                                                sys.exit()
                                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                                if yes_button.collidepoint(event.pos):
                                                    play_item_mode()
                                                elif no_button.collidepoint(event.pos):
                                                    return
                                elif player2_win == 2:
                                    win_message(player2_win)
                                    pygame.display.update()
                                    yes_button, no_button = show_play_again()
                                    while True:
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                pygame.quit()
                                                sys.exit()
                                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                                if yes_button.collidepoint(event.pos):
                                                    play_item_mode()
                                                elif no_button.collidepoint(event.pos):
                                                    return
                                if pos[0] != -1:
                                    turn *= -1
                                else:
                                    turn = -1
            pygame.display.update()
def play_event_mode():
    for i in range(6):
        for j in range(7):
            board[i][j]=0
    skip=0
    gameround=0
    turn = 1
    screen = pygame.display.set_mode(((column_size + 8) * 100, (row_size + 1) * 100))
    confirm=1
    draw_the_board(board,confirm,turn,1)
    show_number(board)
    pygame.display.set_caption("Connect 4")
    pygame.display.update()
    player1_win = 0
    player2_win = 0
    confirm_exit_flag = False
    game = True
    block=[-1,-1]
    eventround=-100
    while game:
        for event in pygame.event.get():
            if  turn==-1 and skip==2:
                skip=0
                turn*=-1
                font = pygame.font.Font("font.ttf", 85)
                text1 = font.render("玩家二回合跳過", True, (255,0,255), BACKGROUND)
                screen.blit(text1, (825,150))
                pygame.display.update()
                pygame.time.wait(900)
                text1 = font.render("玩家二回合跳過", True, BACKGROUND, BACKGROUND)
                screen.blit(text1, (825,150))
                pygame.display.update()
                text1 = font.render("輪到玩家一", True, PINK, BACKGROUND)
                screen.blit(text1, (825, 150))
                pygame.display.update()
            if  turn==1 and skip==1:
                skip=0
                turn*=-1
                font = pygame.font.Font("font.ttf", 85)
                text1 = font.render("玩家一回合跳過", True, (255,0,255), BACKGROUND)
                screen.blit(text1, (825,150))
                pygame.display.update()
                pygame.time.wait(900)
                text1 = font.render("玩家一回合跳過", True, BACKGROUND, BACKGROUND)
                screen.blit(text1, (825,150))
                pygame.display.update()
                text1 = font.render("輪到玩家二", True, PINK, BACKGROUND)
                screen.blit(text1, (825, 150))
                pygame.display.update()
            if gameround-eventround==2:
                eventround=-10
                font=pygame.font.SysFont("arial",50)
                for i in range(7):
                    if i==block[0] or i==block[1]:
                        number=font.render(str(i+1),True,(131,111,255),WHITE)
                        screen.blit(number,(35+i*100,25))
                font = pygame.font.Font("font.ttf", 60)
                pygame.draw.rect(screen,BACKGROUND,(700,0,1300,1300))
                text1 = font.render("事件結束", True, PINK, BACKGROUND)
                screen.blit(text1, (825, 150))
                pygame.display.update()
                pygame.time.wait(2000)
                text1 = font.render("事件結束", True, BACKGROUND, BACKGROUND)
                screen.blit(text1, (825, 150))
                if turn==1:
                    text1 = font.render("輪到玩家一", True, PINK, BACKGROUND)
                    screen.blit(text1, (825, 150))
                    pygame.display.update()
                elif turn==-1:
                    text1 = font.render("輪到玩家二", True, PINK, BACKGROUND)
                    screen.blit(text1, (825, 150))
                    pygame.display.update()
                block=[-1,-1]
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    yes_button, no_button = confirm_exit()
                    confirm_exit_flag = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if confirm_exit_flag:
                    if yes_button.collidepoint(event.pos):
                        return
                    elif no_button.collidepoint(event.pos):
                        confirm_exit_flag = False
                        confirm=0
                        draw_the_board(board,confirm,turn,1)
                        show_number(board)
                        pygame.display.update()
                        print_the_piece()
                        pygame.display.update()
                else:
                    if turn == 1 and skip!=1:
                        posx = event.pos[0]
                        if posx <= 700 and (int(posx/100)==block[0] or int(posx/100)==block[1]):
                            pygame.draw.rect(screen,BACKGROUND,(700,0,1300,1300))
                            font = pygame.font.Font("font.ttf", 60)
                            text1 = font.render("事件影響，此行不能下", True, PINK, BACKGROUND)
                            screen.blit(text1, (825, 150))
                            pygame.display.update()
                            pygame.time.wait(2000)
                            font = pygame.font.Font("font.ttf", 85)
                            pygame.draw.rect(screen,BACKGROUND,(700,0,1300,1300))
                            text1 = font.render("輪到玩家一", True, PINK, BACKGROUND)
                            screen.blit(text1, (825, 150))
                            pygame.display.update()
                        elif posx <= 700 and int(posx/100)!=block[0] and int(posx/100)!=block[1]:
                            column = int(math.ceil(posx / 100))
                            pos = place_piece(column - 1, turn)
                            if pos[0] != -1:
                                gameround+=1
                                font = pygame.font.Font("font.ttf", 85)
                                text1 = font.render("輪到玩家二", True, PINK, BACKGROUND)
                                screen.blit(text1, (825, 150))
                                pygame.display.update()
                                pygame.draw.circle(screen, YELLOW, (pos[1] * 100 + 50, (pos[0] + 1) * 100 + 50), 45)
                                player1_win,win = check_win(turn)
                            else:
                                show_cannot_place()
                            if player1_win==-1:
                                draw_message()
                                while True:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            pygame.quit()
                                            sys.exit()
                                        elif event.type == pygame.MOUSEBUTTONDOWN:
                                            if yes_button.collidepoint(event.pos):
                                                play_event_mode()
                                            elif no_button.collidepoint(event.pos):
                                                return
                            elif player1_win == 1:
                                win_message(player1_win)
                                pygame.display.update()
                                yes_button, no_button = show_play_again()
                                while True:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            pygame.quit()
                                            sys.exit()
                                        elif event.type == pygame.MOUSEBUTTONDOWN:
                                            if yes_button.collidepoint(event.pos):
                                                play_event_mode()
                                            elif no_button.collidepoint(event.pos):
                                                return
                            if gameround%6==0:
                                win,skip,block=randomevent(turn)
                                if block[0]!=-1:
                                    eventround=gameround
                            if win!=0:
                                win_message(win)
                                yes_button, no_button = show_play_again()
                                while True:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            pygame.quit()
                                            sys.exit()
                                        elif event.type == pygame.MOUSEBUTTONDOWN:
                                            if yes_button.collidepoint(event.pos):
                                                play_event_mode()
                                            elif no_button.collidepoint(event.pos):
                                                return   
                            if pos[0] != -1:
                                turn *= -1
                            else:
                                turn = 1
                            if turn==-1 and skip==1:
                                font = pygame.font.Font("font.ttf",85)
                                text1 = font.render("輪到玩家二", True, PINK, BACKGROUND)
                                pygame.time.wait(900)
                                screen.blit(text1, (825, 150))
                                pygame.display.update()
                            elif turn==-1 and skip==2:
                                font = pygame.font.Font("font.ttf",85)
                                text1 = font.render("玩家二回合跳過", True, (255,0,255), BACKGROUND)
                                screen.blit(text1, (825,150))
                                pygame.display.update()
                                pygame.time.wait(2000)
                                text1 = font.render("玩家二回合跳過", True, BACKGROUND, BACKGROUND)
                                screen.blit(text1, (825,150))
                                pygame.display.update()
                                text1 = font.render("輪到玩家一", True, PINK, BACKGROUND)
                                screen.blit(text1, (825, 150))
                                pygame.display.update() 
                                turn*=-1
                                skip=0
                    elif turn == -1 and skip!=2:
                        posx = event.pos[0]
                        if posx <= 700 and (int(posx/100)==block[0] or int(posx/100)==block[1]):
                            pygame.draw.rect(screen,BACKGROUND,(700,0,1300,1300))
                            font = pygame.font.Font("font.ttf", 60)
                            text1 = font.render("事件影響，此行不能下", True, PINK, BACKGROUND)
                            screen.blit(text1, (825, 150))
                            pygame.display.update()
                            pygame.time.wait(2000)
                            font = pygame.font.Font("font.ttf", 85)
                            pygame.draw.rect(screen,BACKGROUND,(700,0,1300,1300))
                            text1 = font.render("輪到玩家二", True, PINK, BACKGROUND)
                            screen.blit(text1, (825, 150))
                            pygame.display.update()
                            if eventround==2:
                                block=[-1,-1]
                                eventround=0
                                for i in range(7):
                                    if i==block[0] or i==block[1]:
                                        number=font.render(str(i+1),True,RED,WHITE)
                                        screen.blit(number,(35+i*100,25))
                                pygame.display.update()
                        if posx <= 700 and int(posx/100)!=block[0] and int(posx/100)!=block[1]:
                            column = int(math.ceil(posx / 100))
                            pos = place_piece(column - 1, turn)
                            if pos[0] != -1:
                                gameround+=1
                                font = pygame.font.Font("font.ttf",85)
                                text1 = font.render("輪到玩家二", True, BLACK, BACKGROUND)
                                screen.blit(text1, (825,150))
                                font = pygame.font.Font("font.ttf", 85)
                                text1 = font.render("輪到玩家一", True, (255,0,255), BACKGROUND)
                                screen.blit(text1, (825,150))
                                pygame.display.update()
                                pygame.draw.circle(screen,RED, (pos[1]*100+ 50,(pos[0]+1)*100+50),45)
                                player2_win,win = check_win(turn)
                            else:
                                show_cannot_place()
                            if player2_win==-1:
                                draw_message()
                                while True:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            pygame.quit()
                                            sys.exit()
                                        elif event.type == pygame.MOUSEBUTTONDOWN:
                                            if yes_button.collidepoint(event.pos):
                                                play_event_mode()
                                            elif no_button.collidepoint(event.pos):
                                                return
                            elif player2_win == 2:
                                win_message(player2_win)
                                pygame.display.update()
                                yes_button, no_button = show_play_again()
                                while True:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            pygame.quit()
                                            sys.exit()
                                        elif event.type == pygame.MOUSEBUTTONDOWN:
                                            if yes_button.collidepoint(event.pos):
                                                play_event_mode()
                                            elif no_button.collidepoint(event.pos):
                                                return
                            if gameround%6==0:
                                win,skip,block=randomevent(turn)
                                if block[0]!=-1:
                                    eventround=gameround
                            if win!=0:
                                win_message(win)
                                yes_button, no_button = show_play_again()
                                while True:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            pygame.quit()
                                            sys.exit()
                                        elif event.type == pygame.MOUSEBUTTONDOWN:
                                            if yes_button.collidepoint(event.pos):
                                                play_event_mode()
                                            elif no_button.collidepoint(event.pos):
                                                return   
                            if pos[0] != -1:
                                turn *= -1
                            else:
                                turn = -1
                            if turn==1 and skip==1:
                                font = pygame.font.Font("font.ttf",85)
                                text1 = font.render("玩家一回合跳過", True, (255,0,255), BACKGROUND)
                                screen.blit(text1, (825,150))
                                pygame.display.update()
                                pygame.time.wait(2000)
                                text1 = font.render("玩家一回合跳過", True, BACKGROUND, BACKGROUND)
                                screen.blit(text1, (825,150))
                                pygame.display.update()
                                text1 = font.render("輪到玩家二", True, PINK, BACKGROUND)
                                screen.blit(text1, (825, 150))
                                pygame.display.update()
                                turn*=-1
                                skip=0 
                            elif turn==1 and skip==2:
                                font = pygame.font.Font("font.ttf",85)
                                text1 = font.render("輪到玩家一", True, PINK, BACKGROUND)
                                screen.blit(text1, (825, 150))
                                pygame.display.update() 
            pygame.display.update()
def main():            
    while True:
        screen.fill(BACKGROUND)
        font = pygame.font.SysFont("Comic Sans MS",150)
        text1 = font.render("Connect 4", True, BLACK, BACKGROUND)
        screen.blit(text1, (430,0))
        
        screen_width, screen_height = screen.get_size()
        center_x = screen_width // 2
        center_y = screen_height // 2
        
        button_width = 300
        button_height = 85
        
        start_button = pygame.Rect(center_x - button_width // 2, center_y - 150+75, button_width, button_height)
        exit_button = pygame.Rect(center_x - button_width // 2, center_y + 150-75, button_width, button_height)
        draw_background1=pygame.Rect(center_x - button_width // 2+10, center_y - 150+10+75, button_width-20, button_height-20)
        draw_background3=pygame.Rect(center_x - button_width // 2+10, center_y - 150+10+300-75, button_width-20, button_height-20)
        
        draw_button("", start_button, WHITE)
        draw_button("開始遊戲",draw_background1,(255,130,71))
        draw_button("", exit_button, WHITE)
        draw_button("退出遊戲", draw_background3, (255,130,71))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    mode_select()
                elif exit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main()