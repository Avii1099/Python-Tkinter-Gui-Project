#importing modules
import pygame
import random
import time

#initializing window
pygame.init()
WIDTH = 800
HEIGHT = 600
black=(0,0,0)
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))#setting game display size
pygame.display.set_caption('DataFlair- Keyboard Jump Game')
background = pygame.image.load('keyback.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))  #scale image 
font = pygame.font.Font('comic.ttf', 40)


## function to get words randomly
word_speed = 0.5
score = 0
def new_word():
    global displayword, yourword, x_cor, y_cor, text, word_speed
    x_cor = random.randint(300,700)     #randomly choose x-cor between 300-700
    y_cor = 200  #y-cor
    word_speed += 0.10
    yourword = ''
    words = open("words.txt").read().split(', ')
    displayword = random.choice(words)
new_word()


#function to draw text
font_name = pygame.font.match_font('comic.ttf')
def draw_text(display, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, black)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    gameDisplay.blit(text_surface, text_rect)

 
#function to show front screen and gameover screen
def game_front_screen():
    gameDisplay.blit(background, (0,0))
    if not game_over :
        draw_text(gameDisplay, "GAME OVER!", 90, WIDTH / 2, HEIGHT / 4)
        draw_text(gameDisplay,"Score : " + str(score), 70, WIDTH / 2, HEIGHT /2)
    else:
        draw_text(gameDisplay, "Press a key to begin!", 54, WIDTH / 2, 500)
    pygame.display.flip()
    waiting = True
    while waiting:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False


#main loop
game_over = True
game_start = True
while True:
    if game_over:
        if game_start:
            game_front_screen()
        game_start = False
    game_over = False

    
    background = pygame.image.load('teacher-background.jpg')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    character = pygame.image.load('char.jpg')
    character = pygame.transform.scale(character, (50,50))
    wood = pygame.image.load('wood-.png')
    wood = pygame.transform.scale(wood, (90,50))


    gameDisplay.blit(background, (0,0))

    y_cor += word_speed
    gameDisplay.blit(wood,(x_cor-50,y_cor+15))
    gameDisplay.blit(character,(x_cor-100,y_cor))
    draw_text(gameDisplay, str(displayword), 40, x_cor, y_cor)
    draw_text(gameDisplay, 'Score:'+str(score), 40, WIDTH/2 , 5)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            yourword += pygame.key.name(event.key)

            if displayword.startswith(yourword):
                if displayword == yourword:
                    score += len(displayword)
                    new_word()
            else:
                game_front_screen()
                time.sleep(2)
                pygame.quit()
                
    if y_cor < HEIGHT-5:
        pygame.display.update()
    else:
        game_front_screen()

