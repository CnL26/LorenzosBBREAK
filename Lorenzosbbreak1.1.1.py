#****Lorenzo's_Brick_Breaker_Clone*!
import pygame
import random
import os
import time

WIDTH = 1080
HEIGHT = 1300
FPS = 60

#*Define colors***********************!
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
INDIGO = (75, 0, 130)
VIOLET = (238, 130, 238)
SILVER = (192, 192, 192)
GOLD = (255, 215, 0)

Expl_colors = (RED, ORANGE, YELLOW)
ball_ptcl_color = (BLUE, INDIGO, CYAN)
brick_colors = (ORANGE, RED, YELLOW, GREEN, BLUE)
bg_anim_clr = (RED, BLUE, GREEN, CYAN, YELLOW, SILVER, GOLD, WHITE)

# setup assests folders(optional for graphics)
game_folder = os.path.dirname(__file__)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Lorenzo's BrickBreaker")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 70)
#ball variables************************!
dx = 12
dy = 12

#paddle variables
move = False

score = 0
lives = 3

#Game Rects*************************!
player = pygame.Rect(390, 1230 , 250, 30)
b_radius = 50
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT / 2 - 15, b_radius, b_radius)
border_rect = pygame.Rect(0, 0, WIDTH, HEIGHT)

#Background Animation**************!
numbers = 25
x = [0] * numbers
y = [0] * numbers
bg_xspd = [0] * numbers
bg_yspd = [0] * numbers
bg_radius = [0] * numbers

for i in range(len(x)):
	x[i] = random.randrange(0, WIDTH)
	y[i] = random.randrange(0, HEIGHT)
	bg_radius[i] = random.randrange(1, 9)
	bg_yspd[i] = bg_radius[i]/6
	bg_xspd[i] = 0

def bg_anim():
    for i in range(len(x)):
     				pygame.draw.circle(screen, random.choice(bg_anim_clr), (int(x[i]), int(y[i])), bg_radius[i], 0)

#*Game Functions******************!
def resetBall():
	ball.centerx = 500
	ball.centery = 400
	pygame.draw.ellipse(screen, VIOLET, ball, 20)
	pygame.time.delay(500)
					 				
def draw_outlines(x, y):
	x = player.x
	y = player.y
	pygame.draw.rect(screen, CYAN, (x, y, player.width, player.height), 5, border_radius=4)
	return 
	
def make_bricks():
	for row in range(rows):
		for col in range(cols):
			x = ((padding_left * col) + padding_left) + (brick_w * col)
			y = ((padding_top * row) + padding_top) + (brick_h * row)
			brick = pygame.Rect(x, y, brick_w, brick_h)
			brick_list.append(brick)
			
def draw_bricks():
	for brick in brick_list:
		pygame.draw.rect(screen, GREEN, brick, 25, border_radius=4)

#*Bricks******************************!
rows = 5
cols = 7

padding_left, padding_top = 10, 10
brick_w = 143
brick_h =60
brick_list = []
make_bricks()

particles = []
brick_particles = []

#**Load Sounds***********************
bgm = pygame.mixer.music.load('tgfcoder-FrozenJam-SeamlessLoop.ogg')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.4)
ball_hit_player = pygame.mixer.Sound('forceField_000.ogg')
ball_hit_wall = pygame.mixer.Sound('impactMetal_004.ogg')
ball_hit_brick = [pygame.mixer.Sound('laserLarge_002.ogg'), pygame.mixer.Sound('laserLarge_003.ogg')]
#*Other Game Variables************!

#*Game loop**************************!
running = True
while running:
    
#keep loop running at right  speed
    clock.tick(FPS)
    # Process events (input)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
        	posx = event.pos[0]
        	move = True
        elif event.type == pygame.MOUSEBUTTONUP:
        	move = False

#*****Update*************************! 
       		
    #Ball
    ball.x += dx 
    ball.y -= dy
    if ball.y < 0:
    	dy*= -1
    if ball.y > HEIGHT - b_radius:
    		lives = lives - 1
    		resetBall()
  		
    if ball.x < 0 or ball.x > WIDTH - b_radius:
    	ball_hit_wall.play()
    	dx *= -1
    #if ball.colliderect()
       	       	
    #Player
    if player.left <= 6:
    	    player.left = 6
    if player.right >= 1074:
    	    player.right = 1074
    	
    if move:
    	if posx < WIDTH // 2 and player.x > 0:
    		player.x -= 12
    	elif posx > WIDTH // 2 and player.x < WIDTH - 250:
    		player.x += 12
    		
    #Player collision	
    if player.colliderect(ball):
    		ball_hit_player.play()
    		dy =- dy
    		dx =- dx
    else:
    		dx =+ dx
    		
    #Brick collision
    for brick in brick_list:
    		if ball.colliderect(brick):
    			random.choice(ball_hit_brick).play()
    			score += 15
    			for i in range(30):
    				brick_particles.append([[brick.centerx, brick.centery], [random.randint(0, 45) / 10 - 1, -10], random.randint(0, 18)])
    			brick_list.remove(brick)
    			dy =- dy
    			dx = dx
    			
    #Bg(background)	
    for i in range(len(x)):
    	y[i] += bg_yspd[i]
    	if y[i] > HEIGHT + bg_radius[i]:
    		y[i] = -bg_radius[i]
    		x[i] = random.randrange(0, WIDTH)
    		
    def showTitle():
    	pass
    			
    def showEnd():
    	running = True
    	while running:
    		screen.fill(BLACK)
    		pygame.mixer.music.load('HipHopNoir_1.wav')
    		pygame.mixer.music.play(-1)
    		bg_anim()
    		screen.blit(font.render('!GAME_OVER!', True, WHITE), (400, 409))
    		os.system('clear')
    		pygame.display.flip()
    		pygame.time.delay(2000)
    		pygame.mixer.music.stop()
    		pygame.quit()
    		return
    				
    #Particles
   		
#***Draw/ Render********************!
    screen.fill(BLACK)
    bg_anim()    		
    pygame.draw.rect(screen, BLUE, player, border_radius=4)
    draw_outlines(player.x, player.y)
    draw_bricks()
    pygame.draw.ellipse(screen, VIOLET, ball, 20)
    particles.append([[ball.centerx, ball.centery], [random.randint(0, 5) / 10 - 1, -2], random.randint(3, 20)])
    
    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.8
        particle[1][1] += 0.2
        pygame.draw.circle(screen, random.choice(Expl_colors), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
        if particle[2] <= 0:
            particles.remove(particle)
            
    for bparticle in brick_particles:
        bparticle[0][0] += bparticle[1][0]
        bparticle[0][1] += bparticle[1][1]
        bparticle[2] -= 0.11
        bparticle[1][1] += 0.5
        pygame.draw.circle(screen, random.choice(Expl_colors), [int(bparticle[0][0]), int(bparticle[0][1])], int(bparticle[2]))
        if bparticle[2] <= 0:
            brick_particles.remove(bparticle)
             
    screen.blit(font.render('SCORE : ' + str(score), True, WHITE), (10, 1150))
    screen.blit(font.render('LIVES : ' + str(lives), True, WHITE), (860, 1150))
    if lives <= 0:
    	pygame.mixer.music.stop()
    	showEnd()
    	#screen.blit(font.render('!GAME_OVER!', True, WHITE), (400, 409))
    pygame.draw.rect(screen, YELLOW, (0, 0, WIDTH, HEIGHT), 5, border_radius=4)    
#**after drawing everything else, flip the display***************************!
    pygame.display.flip()

pygame.quit()
