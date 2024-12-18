import random
import pygame
import time
pygame.init()
pygame.mixer.init()

screen=pygame.display.set_mode((1200,800))
pygame.display.set_caption("WORD SCRAMBLE GAME")

FONT=pygame.font.Font(None,60)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

words={"Easy":["cat","dog","rain","temple","monitor","bottle","door","apple","chair","mouse","house","trees"],
       "Medium":["justify","judge","beautiful","highlight","console","vibrant","serene","peculiar","diligent","lantern"],
       "Hard":["engineering","algorithm","mathematics","astrology","information","development","flabbergasted","photosynthesis","electromagnetism","crystallography","bioluminescence",]}

difficulty=["Easy","Medium","Hard"]
a=random.choice(difficulty)
selected_word=random.choice(words[a])
scramble=''.join(random.sample(selected_word,len(selected_word)))
input_txt=''
score=0
time_limit=30
start_time=time.time()
game_over=False

def display_msg(text,color,y_offset=0):
    msg=FONT.render(text,True,color,y_offset)
    screen.blit(msg,(500,600))

def reset():
    global selected_word,scramble,input_txt,start_time
    selected_word = random.choice(words[a])
    scramble = ''.join(random.sample(selected_word, len(selected_word)))
    input_txt = ''
    start_time=time.time()

bg=pygame.image.load("images.jpg")
bg = pygame.transform.scale(bg, (1200, 800))


running=True
while running:

    elapsed_time=time.time()-start_time
    rem_time=max(0, time_limit-int(elapsed_time))

    if rem_time==0:
        game_over=True

    if rem_time==10 and rem_time>0:
        pygame.mixer.music.load("beep.mp3")
        pygame.mixer.music.play(-1)

    screen_display=FONT.render(f"Scrambled word: {scramble}",True,BLACK)
    screen.blit(screen_display,(350,150))

    time_display=FONT.render(f"Time Left: {rem_time}",True,RED if rem_time<=10 else GREEN)
    screen.blit(time_display,(10,10))

    score_display=FONT.render(f"Score: {score}",True,BLUE)
    screen.blit(score_display,(900,10))

    input_display=FONT.render(f"Your Guess: {input_txt}",True,BLACK)
    screen.blit(input_display,(200,300))

    if game_over:
        go=FONT.render("GAME OVER",True,RED)
        screen.blit(go,(500,500))
        display_msg("TOTAL SCORE", GREEN)
        total_score=FONT.render(f"{score}",True,GREEN)
        screen.blit(total_score,(600,700))
        pygame.display.flip()
        time.sleep(5)
        running=False
        continue

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
                if input_txt.lower()==selected_word:
                    if rem_time>=20:
                        score+=30
                    elif 10 <= rem_time < 20:
                        score+=25
                    else:
                        score+=20
                    reset()
                else:
                    display_msg("TRY AGAIN",color=RED)
                    pygame.display.flip()
                    time.sleep(1)
            elif event.key==pygame.K_BACKSPACE:
                input_txt=input_txt[:-1]
            else:
                input_txt+=event.unicode

    pygame.display.flip()
    screen.blit(bg, (0, 0))
pygame.quit()