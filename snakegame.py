# importing required modules
import pygame
import random
from random import randint

# initialising the pygame window
pygame.init()

# Colors Used
skyblue = (84,194,205)
orange = (255,165,0)
white = (93,216,228)
medblue = (17,24,47)
green = (0,255,0)

# setting up a window
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
GRID_SIZE = 20
GRID_WIDTH = (SCREEN_WIDTH)//GRID_SIZE
GRID_HEIGHT = (SCREEN_HEIGHT)//GRID_SIZE
win = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Defining Grid
def MakeGrid(win):
	for x in range(0,GRID_WIDTH):
		for y in range(0,GRID_HEIGHT):
			if (x+y)%2 == 0:
				pygame.draw.rect(win,skyblue,(x*GRID_SIZE,y*GRID_SIZE,GRID_SIZE,GRID_SIZE))
				pygame.display.update()
			else:
				pygame.draw.rect(win,white,(x*GRID_SIZE,y*GRID_SIZE,GRID_SIZE,GRID_SIZE))
				pygame.display.update()

# Snake Class
class Snake():
	direction = 'R'
	score = 0
	snake_positions = [(100,100),(80,100),(60,100)]
	x,y = snake_positions[0]
	deleted_x , deleted_y = snake_positions[len(snake_positions)-1]
	food_x , food_y = 300 , 300
	gameover = False
	def __init__(self,win):
		pass
	def initialize(self):
		self.direction = 'R'
		self.score = 0
		self.snake_positions = [(100,100),(80,100),(60,100)]
		self.x,self.y = self.snake_positions[0]
		self.deleted_x , self.deleted_y = self.snake_positions[len(self.snake_positions)-1]
		self.food_x , self.food_y = 300 , 300
		self.gameover = False
		MakeGrid(win)
		pygame.draw.rect(win,medblue,(100,100,GRID_SIZE,GRID_SIZE))
		pygame.draw.rect(win,medblue,(80,100,GRID_SIZE,GRID_SIZE))
		pygame.draw.rect(win,medblue,(60,100,GRID_SIZE,GRID_SIZE))
		pygame.draw.rect(win,green,(300,300,GRID_SIZE,GRID_SIZE))
		pygame.display.update()

	def Loop(self,win):
		global checking
		self.x , self.y = self.snake_positions[0]
		self.deleted_x , self.deleted_y = self.snake_positions[len(self.snake_positions)-1]
		for events in pygame.event.get():
			if events.type == pygame.QUIT:
				pygame.quit()
		self.move()
		if self.chck_collisions() == True:
			if ((self.food_x//GRID_SIZE)+(self.food_y//GRID_SIZE))%2 == 0:
				pygame.draw.rect(win,skyblue,(self.food_x,self.food_y,GRID_SIZE,GRID_SIZE))
				pygame.display.update()
			elif ((self.food_x//GRID_SIZE)+(self.food_y//GRID_SIZE))%2 == 1:
				pygame.draw.rect(win,white,(self.food_x,self.food_y,GRID_SIZE,GRID_SIZE))
				pygame.display.update()
			for P,Q in self.snake_positions:
				if ((P//GRID_SIZE)+(Q//GRID_SIZE))%2 == 0:
					pygame.draw.rect(win,skyblue,(P,Q,GRID_SIZE,GRID_SIZE))
					pygame.display.update()
				elif ((P//GRID_SIZE)+(Q//GRID_SIZE))%2 == 1:
					pygame.draw.rect(win,white,(P,Q,GRID_SIZE,GRID_SIZE))
					pygame.display.update()
			score_font = pygame.font.SysFont("comicsansms",50)
			value = score_font.render("Your Score : " + str(self.score), True , (255,255,255))
			win.blit(value , [SCREEN_WIDTH//5,SCREEN_HEIGHT//5])
			score_font1 = pygame.font.SysFont("comicsansms",20)
			value1 = score_font1.render("Click Enter to Restart or Esc to Exit", True , (255,255,255))
			win.blit(value1 , [SCREEN_WIDTH//6,SCREEN_HEIGHT//3])
			pygame.display.update()
			self.gameover = True
			return
		else:
			temp_set = []
			temp_set.append((self.x,self.y))
			self.deleted_x,self.deleted_y = self.snake_positions[len(self.snake_positions)-1]
			for i in range(len(self.snake_positions)):
				temp_set.append(self.snake_positions[i])
			self.snake_positions = temp_set
			if (self.food_x,self.food_y) != self.snake_positions[0]:
				self.snake_positions.remove((self.deleted_x,self.deleted_y))
			else:
				self.score += 1
				self.food_position()
		self.update_positions()

	def move(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			self.direction = 'L'
		elif keys[pygame.K_RIGHT]:
			self.direction = 'R'
		elif keys[pygame.K_UP]:
			self.direction = 'U'
		elif keys[pygame.K_DOWN]:
			self.direction = 'D'
		if self.direction == 'L':
			self.x -= GRID_SIZE
		elif self.direction == 'R':
			self.x += GRID_SIZE
		elif self.direction == 'U':
			self.y -= GRID_SIZE
		elif self.direction == 'D':
			self.y += GRID_SIZE

	def chck_collisions(self):
		for X,Y in self.snake_positions:
			if X == self.x and Y == self.y:
				return True
		if self.x == SCREEN_WIDTH or self.x < 0 or self.y == SCREEN_HEIGHT or self.y < 0:
			return True
		return False

	def update_positions(self):
		pygame.draw.rect(win,medblue,(self.x,self.y,GRID_SIZE,GRID_SIZE))
		pygame.display.update()
		if ((self.deleted_x//GRID_SIZE)+(self.deleted_y//GRID_SIZE))%2 == 0:
			pygame.draw.rect(win,skyblue,(self.deleted_x,self.deleted_y,GRID_SIZE,GRID_SIZE))
			pygame.display.update()
		elif ((self.deleted_x//GRID_SIZE)+(self.deleted_y//GRID_SIZE))%2 == 1:
			pygame.draw.rect(win,white,(self.deleted_x,self.deleted_y,GRID_SIZE,GRID_SIZE))
			pygame.display.update()

	def food_position(self):
		while True:
			is_food = 0
			self.food_x = randint(1,24)*20
			self.food_y = randint(1,24)*20
			for P,Q in self.snake_positions:
				if P == self.food_x and Q == self.food_y:
					is_food = 1
			if is_food == 0:
				break
		pygame.draw.rect(win,green,(self.food_x,self.food_y,GRID_SIZE,GRID_SIZE))
		pygame.display.update()

# Our MainLoop
s = Snake(win)
s.initialize()
while True:
	pygame.time.delay(60)
	if s.gameover == True:
		for events in pygame.event.get():
			if events.type == pygame.QUIT:
				pygame.quit()
			if events.type == pygame.KEYDOWN:
				if events.key == pygame.K_RETURN:
					s.initialize()
				elif events.key == pygame.K_ESCAPE:
					pygame.quit()
	else:
		s.Loop(win)
		pygame.display.update()
quit() 


