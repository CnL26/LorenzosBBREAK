# Pygame template skeleton for new Project
import pygame
import random
import os

WIDTH = 1080
HEIGHT = 1300
FPS = 60

# Define colors
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

colors = (BLUE, INDIGO, CYAN)

# setup assests folders(optional for graphics)
game_folder = os.path.dirname(__file__)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Lorenzo's BrickBreaker")
clock = pygame.time.Clock()
#ball variables
dx = 6
dy = 8

#paddle variables
move = False

#Game Rects
player = pygame.Rect(390, 1230 , 250, 60)
b_radius = 50
ball = pygame.Rect(WIDTH / 2 - 15, HEIGHT / 2 - 15, b_radius, b_radius)

#Background Animation
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
     				pygame.draw.circle(screen, WHITE, (int(x[i]), int(y[i])), bg_radius[i], 0)
				 				
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
		pygame.draw.rect(screen, ORANGE, brick, 25, border_radius=4)

#Bricks
rows = 5
cols = 7
padding_left, padding_top = 10, 10
brick_w = 143
brick_h =60
brick_list = []
make_bricks()

particles = []
	
# Game loop
running = True
while running:
    
 
    # keep loop running at right  speed
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

    # Update 
       		
    #Ball
    ball.x += dx
    ball.y -= dy
    
    if ball.y < 0 or ball.y > HEIGHT - b_radius:
    	dy *= -1
    if ball.x < 0 or ball.x > WIDTH - b_radius:
    	dx *= -1
    if ball.left >= player.right:
       	       	
    #Player
     if player.left <= 6:
    	    player.left = 6
     if player.right >= 1074:
    	    player.right = 1074
    	
    if move:
    	if posx < WIDTH // 2 and player.x > 0:
    		player.x -= 9
    	elif posx > WIDTH // 2 and player.x < WIDTH - 250:
    		player.x += 9
    		
    #Player collision	
    if player.colliderect(ball):
    		dy =- dy
    		dx =+ dx
    		
    #Brick collision
    for brick in brick_list:
    		if ball.colliderect(brick):
    			brick_list.remove(brick)
    			dy =- dy
    			
    #Bg(background)	
    for i in range(len(x)):
    	y[i] += bg_yspd[i]
    	if y[i] > HEIGHT + bg_radius[i]:
    		y[i] = -bg_radius[i]
    		x[i] = random.randrange(0, WIDTH)
    		
    #Particles
 
    		
    # Draw/ Render
    screen.fill(BLACK)
    bg_anim()    		
    pygame.draw.rect(screen, BLUE, player, border_radius=4)
    draw_outlines(player.x, player.y)
    draw_bricks()
    pygame.draw.ellipse(screen, VIOLET, ball, 20)
    particles.append([[ball.centerx, ball.centery], [random.randint(0, 5) / 10 - 1, -2], random.randint(0, 20)])
    
    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.8
        particle[1][1] += 0.2
        pygame.draw.circle(screen, random.choice(colors), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
        if particle[2] <= 0:
            particles.remove(particle)
    #pygame.Surface.fill(ball, GREEN)
    pygame.draw.rect(screen, YELLOW, (0, 0, WIDTH, HEIGHT), 5, border_radius=4)
     
    # after drawing everything else, flip the display
    pygame.display.flip()

pygame.quit()
