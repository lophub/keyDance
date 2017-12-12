import pygame, sys
import time
from pygame.locals import *
import random

pygame.init()

FPS = 160
fpsClock = pygame.time.Clock()

level = None

score = 0

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
GRAY = (211, 211, 211)

#Sound and Music
ButtonClick = pygame.mixer.Sound('buttonclick.wav')
FailSound = pygame.mixer.Sound('fail.wav')
pygame.mixer.music.load('backgroundmusic.mp3')


DISPLAYSURF = pygame.display.set_mode((800, 800))
pygame.display.set_caption('KeyDance')



KEYUP = pygame.image.load('testuparrow.png')
KEYDOWN = pygame.image.load('testdownarrow.png')
KEYLEFT = pygame.image.load('testleftarrow.png')
KEYRIGHT = pygame.image.load('testrightarrow.png')



UPBUTTON = pygame.K_UP
DOWNBUTTON = pygame.K_DOWN
LEFTBUTTON = pygame.K_LEFT
RIGHTBUTTON = pygame.K_RIGHT 

def MusicOn():
		pygame.mixer.music.play(-1, 0.0)
		pygame.mixer.music.set_volume(.3)
		
		
def MusicOff():
	pygame.mixer.music.stop()

def text_objects(text, font):
	textSURF = font.render(text, True, BLACK)
	return textSURF, textSURF.get_rect()

def game_intro():
	intro = True
	
	while intro:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		DISPLAYSURF.fill(WHITE)
		largeText = pygame.font.Font('freesansbold.ttf', 115)
		TextSURF, TextRECT = text_objects("Key Dance", largeText)
		TextRECT.center = ((400), (200))
		DISPLAYSURF.blit(TextSURF, TextRECT)
		
		button("Play", 350, 450, 100, 50, WHITE, GRAY, main_menu)
		
		button_no_line ("Music", 55, 715, 65, 25, WHITE, WHITE, )
		button ("On", 50, 750, 35, 20, WHITE, GRAY, MusicOn)
		button ("Off", 100, 750, 35, 20, WHITE, GRAY, MusicOff)
		
		pygame.display.update()
		fpsClock.tick(15)
		
def button(msg, x, y, w, h, ic, ac, action = None):
		MOUSE = pygame.mouse.get_pos()
		CLICK = pygame.mouse.get_pressed()
		
		#So Algebra was useful 
		
		#bottom line
		pygame.draw.line(DISPLAYSURF, BLACK, (x, y + h), (x + w, y + h), 3)
		
		#left line
		pygame.draw.line(DISPLAYSURF, BLACK, (x, y), (x, y + h), 3)
		
		#top line
		pygame.draw.line(DISPLAYSURF, BLACK, (x, y), (x + w, y), 3)
		
		#right line
		pygame.draw.line(DISPLAYSURF, BLACK, (x + w, y), (x + w, y + h), 2)
		
		
		if x+w > MOUSE[0] > x and  y+h > MOUSE[1] > y:
			pygame.draw.rect(DISPLAYSURF, ac, (x, y, w, h))
			
			if CLICK[0] == 1 and action != None:
				ButtonClick.play()
				time.sleep(.15)
				action()
		else:
			pygame.draw.rect(DISPLAYSURF, ic, (x, y, w, h))
			
		smallText = pygame.font.Font('freesansbold.ttf', 20)
		TextSURF, TextRECT = text_objects(msg, smallText)
		TextRECT.center = ( (x+(w/2)), (y+(h/2)) )
		DISPLAYSURF.blit(TextSURF, TextRECT)


def button_no_line(msg, x, y, w, h, ic, ac, action = None):
		MOUSE = pygame.mouse.get_pos()
		CLICK = pygame.mouse.get_pressed()
		
		#So Algebra was useful 
		
		#bottom line
		#pygame.draw.line(DISPLAYSURF, BLACK, (x, y + h), (x + w, y + h), 3)
		
		#left line
		#pygame.draw.line(DISPLAYSURF, BLACK, (x, y), (x, y + h), 3)
		
		#top line
		#pygame.draw.line(DISPLAYSURF, BLACK, (x, y), (x + w, y), 3)
		
		#right line
		#pygame.draw.line(DISPLAYSURF, BLACK, (x + w, y), (x + w, y + h), 2)
		
		
		if x+w > MOUSE[0] > x and  y+h > MOUSE[1] > y:
			pygame.draw.rect(DISPLAYSURF, ac, (x, y, w, h))
			
			if CLICK[0] == 1 and action != None:
				ButtonClick.play()
				time.sleep(.15)
				action()
		else:
			pygame.draw.rect(DISPLAYSURF, ic, (x, y, w, h))
			
		smallText = pygame.font.Font('freesansbold.ttf', 20)
		TextSURF, TextRECT = text_objects(msg, smallText)
		TextRECT.center = ( (x+(w/2)), (y+(h/2)) )
		DISPLAYSURF.blit(TextSURF, TextRECT)
		
def level_select():

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
					pygame.quit()
					sys.exit()
		DISPLAYSURF.fill(WHITE)
		largeText = pygame.font.Font('freesansbold.ttf', 115)
		TextSURF, TextRECT = text_objects("Select Level", largeText)
		TextRECT.center = ((400), (200))
		DISPLAYSURF.blit(TextSURF, TextRECT)
			
		button("Level 1", 100, 450, 100, 50, WHITE, GRAY, level1)
		button("Level 2", 350, 450, 100, 50, WHITE, GRAY, level2)
		button("Level 3", 600, 450, 100, 50, WHITE, GRAY, level3)
		button("Main Menu", 650, 725, 125, 50, WHITE, GRAY, main_menu)

		
		button_no_line ("Music", 55, 715, 65, 25, WHITE, WHITE, )
		button ("On", 50, 750, 35, 20, WHITE, GRAY, MusicOn)
		button ("Off", 100, 750, 35, 20, WHITE, GRAY, MusicOff)
		
		pygame.display.update()
		fpsClock.tick(15)
				
		
def terminate():
	pygame.quit()
	sys.exit()
	
def level_win1():
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		DISPLAYSURF.fill(WHITE)
		largeText = pygame.font.Font('freesansbold.ttf', 115)
		TextSURF, TextRECT = text_objects("You Win !", largeText)
		TextRECT.center = ((400), (200))
		DISPLAYSURF.blit(TextSURF, TextRECT)
		
		button("Level Select", 225, 450, 150, 50, WHITE, GRAY, level_select)
		
		button("Next Level", 425, 450, 150, 50, WHITE, GRAY, level2)
		
		button_no_line ("Music", 55, 715, 65, 25, WHITE, WHITE, )
		button ("On", 50, 750, 35, 20, WHITE, GRAY, MusicOn)
		button ("Off", 100, 750, 35, 20, WHITE, GRAY, MusicOff)
		
		pygame.display.update()
		fpsClock.tick(15)
		
def level_win2():
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		DISPLAYSURF.fill(WHITE)
		largeText = pygame.font.Font('freesansbold.ttf', 115)
		TextSURF, TextRECT = text_objects("You Win !", largeText)
		TextRECT.center = ((400), (200))
		DISPLAYSURF.blit(TextSURF, TextRECT)
		
		button("Level Select", 225, 450, 150, 50, WHITE, GRAY, level_select)
		
		button("Next Level", 425, 450, 150, 50, WHITE, GRAY, level3)
		
		button_no_line ("Music", 55, 715, 65, 25, WHITE, WHITE, )
		button ("On", 50, 750, 35, 20, WHITE, GRAY, MusicOn)
		button ("Off", 100, 750, 35, 20, WHITE, GRAY, MusicOff)
		
		pygame.display.update()
		fpsClock.tick(15)
		
def level_win3():
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		DISPLAYSURF.fill(WHITE)
		largeText = pygame.font.Font('freesansbold.ttf', 115)
		TextSURF, TextRECT = text_objects("You Win !", largeText)
		TextRECT.center = ((400), (200))
		DISPLAYSURF.blit(TextSURF, TextRECT)
		
		button("Level Select", 325, 450, 150, 50, WHITE, GRAY, level_select)
		
		
		button_no_line ("Music", 55, 715, 65, 25, WHITE, WHITE, )
		button ("On", 50, 750, 35, 20, WHITE, GRAY, MusicOn)
		button ("Off", 100, 750, 35, 20, WHITE, GRAY, MusicOff)
		
		pygame.display.update()
		fpsClock.tick(15)

		

def level_lose_level1():
	 
	FailSound.play()

	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		DISPLAYSURF.fill(WHITE)
		largeText = pygame.font.Font('freesansbold.ttf', 115)
		TextSURF, TextRECT = text_objects("You Lose :( ", largeText)
		TextRECT.center = ((400), (200))
		DISPLAYSURF.blit(TextSURF, TextRECT)
		
		button("Level Select", 225, 450, 150, 50, WHITE, GRAY, level_select)
		
		button("Retry", 425, 450, 150, 50, WHITE, GRAY, level1)
		
		button_no_line ("Music", 55, 715, 65, 25, WHITE, WHITE, )
		button ("On", 50, 750, 35, 20, WHITE, GRAY, MusicOn)
		button ("Off", 100, 750, 35, 20, WHITE, GRAY, MusicOff)
		
		pygame.display.update()
		fpsClock.tick(15)
		
def level_lose_level2():
	 
	FailSound.play()

	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		DISPLAYSURF.fill(WHITE)
		largeText = pygame.font.Font('freesansbold.ttf', 115)
		TextSURF, TextRECT = text_objects("You Lose :( ", largeText)
		TextRECT.center = ((400), (200))
		DISPLAYSURF.blit(TextSURF, TextRECT)
		
		button("Level Select", 225, 450, 150, 50, WHITE, GRAY, level_select)
		
		button("Retry", 425, 450, 150, 50, WHITE, GRAY, level2)
		
		button_no_line ("Music", 55, 715, 65, 25, WHITE, WHITE, )
		button ("On", 50, 750, 35, 20, WHITE, GRAY, MusicOn)
		button ("Off", 100, 750, 35, 20, WHITE, GRAY, MusicOff)
		
		pygame.display.update()
		fpsClock.tick(15)
		
def level_lose_level3():
	 
	FailSound.play()

	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		DISPLAYSURF.fill(WHITE)
		largeText = pygame.font.Font('freesansbold.ttf', 115)
		TextSURF, TextRECT = text_objects("You Lose :( ", largeText)
		TextRECT.center = ((400), (200))
		DISPLAYSURF.blit(TextSURF, TextRECT)
		
		button("Level Select", 225, 450, 150, 50, WHITE, GRAY, level_select)

		button("Retry", 425, 450, 150, 50, WHITE, GRAY, level3)
		
		button_no_line ("Music", 55, 715, 65, 25, WHITE, WHITE, )
		button ("On", 50, 750, 35, 20, WHITE, GRAY, MusicOn)
		button ("Off", 100, 750, 35, 20, WHITE, GRAY, MusicOff)
		
		pygame.display.update()
		fpsClock.tick(15)
		
		
def level_lose_easy():

	FailSound.play()

	while True:
		for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
		DISPLAYSURF.fill(WHITE)
		largeText = pygame.font.Font('freesansbold.ttf', 115)
		TextSURF, TextRECT = text_objects("You Lose :( ", largeText)
		TextRECT.center = ((400), (200))
		DISPLAYSURF.blit(TextSURF, TextRECT)
		
		button("Select Difficulty", 225, 450, 170, 50, WHITE, GRAY, FreeStyleSelect)

		button("Retry", 425, 450, 150, 50, WHITE, GRAY, FreeStyleEasy)
			
		button_no_line ("Music", 55, 715, 65, 25, WHITE, WHITE, )
		button ("On", 50, 750, 35, 20, WHITE, GRAY, MusicOn)
		button ("Off", 100, 750, 35, 20, WHITE, GRAY, MusicOff)
		
		pygame.display.update()
		fpsClock.tick(15)

def level_lose_medium():

	FailSound.play()

	while True:
		for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
		DISPLAYSURF.fill(WHITE)
		largeText = pygame.font.Font('freesansbold.ttf', 115)
		TextSURF, TextRECT = text_objects("You Lose :( ", largeText)
		TextRECT.center = ((400), (200))
		DISPLAYSURF.blit(TextSURF, TextRECT)
		
		button("Select Difficulty", 225, 450, 170, 50, WHITE, GRAY, FreeStyleSelect)

		button("Retry", 425, 450, 150, 50, WHITE, GRAY, FreeStyleMedium)
			
		button_no_line ("Music", 55, 715, 65, 25, WHITE, WHITE, )
		button ("On", 50, 750, 35, 20, WHITE, GRAY, MusicOn)
		button ("Off", 100, 750, 35, 20, WHITE, GRAY, MusicOff)
		
		pygame.display.update()
		fpsClock.tick(15)
		
def level_lose_hard():

	FailSound.play()

	while True:
		for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
		DISPLAYSURF.fill(WHITE)
		largeText = pygame.font.Font('freesansbold.ttf', 115)
		TextSURF, TextRECT = text_objects("You Lose :( ", largeText)
		TextRECT.center = ((400), (200))
		DISPLAYSURF.blit(TextSURF, TextRECT)
		
		button("Select Difficulty", 225, 450, 170, 50, WHITE, GRAY, FreeStyleSelect)

		button("Retry", 425, 450, 150, 50, WHITE, GRAY, FreeStyleHard)
			
		button_no_line ("Music", 55, 715, 65, 25, WHITE, WHITE, )
		button ("On", 50, 750, 35, 20, WHITE, GRAY, MusicOn)
		button ("Off", 100, 750, 35, 20, WHITE, GRAY, MusicOff)
		
		pygame.display.update()
		fpsClock.tick(15)		
		

def main_menu():
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		DISPLAYSURF.fill(WHITE)
		largeText = pygame.font.Font('freesansbold.ttf', 115)
		TextSURF, TextRECT = text_objects("Main Menu", largeText)
		TextRECT.center = ((400), (200))
		DISPLAYSURF.blit(TextSURF, TextRECT)
		
		button("Level's", 250, 450, 100, 50, WHITE, GRAY, level_select)
		
		button("Free Style", 400, 450, 125, 50, WHITE, GRAY, FreeStyleSelect)
		
		
		button_no_line ("Music", 55, 715, 65, 25, WHITE, WHITE, )
		button ("On", 50, 750, 35, 20, WHITE, GRAY, MusicOn)
		button ("Off", 100, 750, 35, 20, WHITE, GRAY, MusicOff)
		
		pygame.display.update()
		fpsClock.tick(15)
		
		


		
def level1():
	
	level = level1
	FPS = 180
	
	UPPOSX = 350
	UPPOSY = 5
	
	DOWNPOSX = 450
	DOWNPOSY = -100

	DOWNPOSX1 = 450
	DOWNPOSY1 = -195
	
	RIGHTPOSX = 500
	RIGHTPOSY = -290
	
	UPPOSX1 = 350
	UPPOSY1 = -385
	
	LEFTPOSX = 400
	LEFTPOSY = -480
	
	RIGHTPOSX1 = 500
	RIGHTPOSY1 = -575
	
	LEFTPOSX1 = 400
	LEFTPOSY1 = -670
	
	UPPOSX2 = 350
	UPPOSY2 = -765
	
	while True:
	
		if UPPOSY == 562:
			level_lose_level1()
			
		if DOWNPOSY == 562:
			level_lose_level1()
			
		if DOWNPOSY1 == 562:
			level_lose_level1()
	
		if RIGHTPOSY == 562:
			level_lose_level1()
	
		if UPPOSY1 == 562:
			level_lose_level1()
			
		if LEFTPOSY == 562:
			level_lose_level1()
			
		if LEFTPOSY1 == 562:
			level_lose_level1()
			
		if RIGHTPOSY1 == 562:
			level_lose_level1()
			
		if UPPOSY2 == 562:
			level_lose_level1()
			
		#Background
		DISPLAYSURF.fill(WHITE)
		
		#Red Bar
		pygame.draw.line(DISPLAYSURF, BLACK, (0, 500), (799, 500), 4)
		pygame.draw.line(DISPLAYSURF, BLACK, (0, 563), (799, 563), 4)
		REDSURFACE = pygame.draw.rect(DISPLAYSURF, RED, (0, 502, 800, 60))
		
		#Animation
		UPPOSY += 1
		DOWNPOSY += 1
		DOWNPOSY1 += 1	
		RIGHTPOSY += 1
		UPPOSY1 += 1
		LEFTPOSY += 1
		RIGHTPOSY1 += 1
		LEFTPOSY1 += 1
		UPPOSY2 += 1
		
		
		DISPLAYSURF.blit(KEYUP, (UPPOSX, UPPOSY))
		DISPLAYSURF.blit(KEYDOWN, (DOWNPOSX, DOWNPOSY))
		DISPLAYSURF.blit(KEYDOWN, (DOWNPOSX1, DOWNPOSY1))
		DISPLAYSURF.blit(KEYRIGHT, (RIGHTPOSX, RIGHTPOSY))
		DISPLAYSURF.blit(KEYUP, (UPPOSX1, UPPOSY1))
		DISPLAYSURF.blit(KEYLEFT, (LEFTPOSX, LEFTPOSY))
		
		DISPLAYSURF.blit(KEYRIGHT, (RIGHTPOSX1, RIGHTPOSY1))
		DISPLAYSURF.blit(KEYLEFT, (LEFTPOSX1, LEFTPOSY1))
		DISPLAYSURF.blit(KEYUP, (UPPOSX2, UPPOSY2))
	
		#level 1
		for event in pygame.event.get():
		

			if event.type == pygame.KEYDOWN:
			
				#Up Arrow 1
				if event.key == pygame.K_UP and REDSURFACE.collidepoint(UPPOSX, UPPOSY):
					UPPOSY = -10000


				#Down Arrow 2
				elif event.key == pygame.K_DOWN and REDSURFACE.collidepoint(DOWNPOSX, DOWNPOSY):
					DOWNPOSY = -10000

					
				#Down Arrow 3 
				elif event.key == pygame.K_DOWN and REDSURFACE.collidepoint(DOWNPOSX1, DOWNPOSY1):
					DOWNPOSY1 = -10000
					
				#Right Arrow 4
				elif event.key == pygame.K_RIGHT and REDSURFACE.collidepoint(RIGHTPOSX, RIGHTPOSY):
					RIGHTPOSY = -10000

				#Up Arrow 5
				elif event.key == pygame.K_UP and REDSURFACE.collidepoint(UPPOSX1, UPPOSY1):
					UPPOSY1 = -10000
	
				#Left Arrow 6
				elif event.key == pygame.K_LEFT and REDSURFACE.collidepoint(LEFTPOSX, LEFTPOSY):
					LEFTPOSY = -10000
					
				#Right Arrow 7
				elif event.key == pygame.K_RIGHT and REDSURFACE.collidepoint(RIGHTPOSX1, RIGHTPOSY1):
					RIGHTPOSY1 = -10000	
					
				#Left Arrow 8
				elif event.key == pygame.K_LEFT and REDSURFACE.collidepoint(LEFTPOSX1, LEFTPOSY1):
					LEFTPOSY1 = -10000
				
				#Up Arrow 9
				elif event.key == pygame.K_UP and REDSURFACE.collidepoint(UPPOSX2, UPPOSY2):
					UPPOSY2 = -10000
					level_win1()
			
			if event.type == QUIT:
				pygame.quit()
				sys.exit()	
			
		button_no_line ("Music", 55, 715, 65, 25, WHITE, WHITE, )
		button ("On", 50, 750, 35, 20, WHITE, GRAY, MusicOn)
		button ("Off", 100, 750, 35, 20, WHITE, GRAY, MusicOff)
			

		pygame.display.update()
		fpsClock.tick(FPS)
	
	
def level2():
	level = level2
	FPS = 250
	
	DOWNPOSX = 450
	DOWNPOSY = 5
	
	UPPOSX = 350
	UPPOSY = -100

	DOWNPOSX1 = 450
	DOWNPOSY1 = -195
	
	RIGHTPOSX = 500
	RIGHTPOSY = -290
	
	RIGHTPOSX1 = 500
	RIGHTPOSY1 = -385
	
	LEFTPOSX1 = 400
	LEFTPOSY1 = -480
	
	UPPOSX2 = 350
	UPPOSY2 = -575
		
	UPPOSX1 = 350
	UPPOSY1 = -670
	
	LEFTPOSX = 400
	LEFTPOSY = -765
	
	
	
	while True:
	
		if UPPOSY == 562:
			level_lose_level2()
			
		if DOWNPOSY == 562:
			level_lose_level2()
			
		if DOWNPOSY1 == 562:
			level_lose_level2()
	
		if RIGHTPOSY == 562:
			level_lose_level2()
	
		if UPPOSY1 == 562:
			level_lose_level2()
			
		if LEFTPOSY == 562:
			level_lose_level2()
			
		if LEFTPOSY1 == 562:
			level_lose_level2()
			
		if RIGHTPOSY1 == 562:
			level_lose_level2()
			
		if UPPOSY2 == 562:
			level_lose_level2()
			
		#Background
		DISPLAYSURF.fill(WHITE)
		
		#Red Bar
		pygame.draw.line(DISPLAYSURF, BLACK, (0, 500), (799, 500), 4)
		pygame.draw.line(DISPLAYSURF, BLACK, (0, 563), (799, 563), 4)
		REDSURFACE = pygame.draw.rect(DISPLAYSURF, RED, (0, 502, 800, 60))
		
		#Animation
		UPPOSY += 1
		DOWNPOSY += 1
		DOWNPOSY1 += 1	
		RIGHTPOSY += 1
		UPPOSY1 += 1
		LEFTPOSY += 1
		RIGHTPOSY1 += 1
		LEFTPOSY1 += 1
		UPPOSY2 += 1
		
		DISPLAYSURF.blit(KEYDOWN, (DOWNPOSX, DOWNPOSY))
		DISPLAYSURF.blit(KEYUP, (UPPOSX, UPPOSY))
		DISPLAYSURF.blit(KEYDOWN, (DOWNPOSX1, DOWNPOSY1))
		DISPLAYSURF.blit(KEYRIGHT, (RIGHTPOSX, RIGHTPOSY))
		DISPLAYSURF.blit(KEYRIGHT, (RIGHTPOSX1, RIGHTPOSY1))
		DISPLAYSURF.blit(KEYLEFT, (LEFTPOSX1, LEFTPOSY1))
		DISPLAYSURF.blit(KEYUP, (UPPOSX2, UPPOSY2))
		DISPLAYSURF.blit(KEYUP, (UPPOSX1, UPPOSY1))
		DISPLAYSURF.blit(KEYLEFT, (LEFTPOSX, LEFTPOSY))
		
	
		#level 2
		for event in pygame.event.get():
		

			if event.type == pygame.KEYDOWN:
			
				#Down Arrow 1
				if event.key == pygame.K_DOWN and REDSURFACE.collidepoint(DOWNPOSX, DOWNPOSY):
					DOWNPOSY = -10000

				#Up Arrow 2
				elif event.key == pygame.K_UP and REDSURFACE.collidepoint(UPPOSX, UPPOSY):
					UPPOSY = -10000
					
				#Down Arrow 3 
				elif event.key == pygame.K_DOWN and REDSURFACE.collidepoint(DOWNPOSX1, DOWNPOSY1):
					DOWNPOSY1 = -10000

					
				#Right Arrow 4
				elif event.key == pygame.K_RIGHT and REDSURFACE.collidepoint(RIGHTPOSX, RIGHTPOSY):
					RIGHTPOSY = -10000

				#Right Arrow 5
				elif event.key == pygame.K_RIGHT and REDSURFACE.collidepoint(RIGHTPOSX1, RIGHTPOSY1):
					RIGHTPOSY1 = -10000	
	
				#Left Arrow 6
				elif event.key == pygame.K_LEFT and REDSURFACE.collidepoint(LEFTPOSX1, LEFTPOSY1):
					LEFTPOSY1 = -10000
					
				#Up Arrow 7
				elif event.key == pygame.K_UP and REDSURFACE.collidepoint(UPPOSX1, UPPOSY1):
					UPPOSY1 = -10000
					
				#Up Arrow 8
				elif event.key == pygame.K_UP and REDSURFACE.collidepoint(UPPOSX2, UPPOSY2):
					UPPOSY2 = -10000
				
				#Left Arrow 9
				elif event.key == pygame.K_LEFT and REDSURFACE.collidepoint(LEFTPOSX, LEFTPOSY):
					LEFTPOSY = -10000
					level_win2()
			
			if event.type == QUIT:
				pygame.quit()
				sys.exit()	
			
		button_no_line ("Music", 55, 715, 65, 25, WHITE, WHITE, )
		button ("On", 50, 750, 35, 20, WHITE, GRAY, MusicOn)
		button ("Off", 100, 750, 35, 20, WHITE, GRAY, MusicOff)
			

		pygame.display.update()
		fpsClock.tick(FPS)
		
		
def level3():
	level = level3
	FPS = 450
	
	DOWNPOSX = 450
	DOWNPOSY = -765
	
	UPPOSX  = 350
	UPPOSY = -670

	DOWNPOSX1 = 450
	DOWNPOSY1 = -195
	
	RIGHTPOSX = 500
	RIGHTPOSY = -575
	
	RIGHTPOSX1 =500
	RIGHTPOSY1 = -480
	
	LEFTPOSX1 = 400
	LEFTPOSY1 = -385
	
	UPPOSX2 = 350
	UPPOSY2 = -100
		
	UPPOSX1 = 350
	UPPOSY1 = -290
	
	LEFTPOSX = 400
	LEFTPOSY = 5
	
	
	
	while True:
	
		if UPPOSY == 562:
			level_lose_level3()
			
		if DOWNPOSY == 562:
			level_lose_level3()
			
		if DOWNPOSY1 == 562:
			level_lose_level3()
	
		if RIGHTPOSY == 562:
			level_lose_level3()
	
		if UPPOSY1 == 562:
			level_lose_level3()
			
		if LEFTPOSY == 562:
			level_lose_level3()
			
		if LEFTPOSY1 == 562:
			level_lose_level3()
			
		if RIGHTPOSY1 == 562:
			level_lose_level3()
			
		if UPPOSY2 == 562:
			level_lose_level3()
			
		#Background
		DISPLAYSURF.fill(WHITE)
		
		#Red Bar
		pygame.draw.line(DISPLAYSURF, BLACK, (0, 500), (799, 500), 4)
		pygame.draw.line(DISPLAYSURF, BLACK, (0, 563), (799, 563), 4)
		REDSURFACE = pygame.draw.rect(DISPLAYSURF, RED, (0, 502, 800, 60))
		
		#Animation
		UPPOSY += 1
		DOWNPOSY += 1
		DOWNPOSY1 += 1	
		RIGHTPOSY += 1
		UPPOSY1 += 1
		LEFTPOSY += 1
		RIGHTPOSY1 += 1
		LEFTPOSY1 += 1
		UPPOSY2 += 1
		
		DISPLAYSURF.blit(KEYLEFT, (LEFTPOSX, LEFTPOSY))
		DISPLAYSURF.blit(KEYUP, (UPPOSX2, UPPOSY2))
		DISPLAYSURF.blit(KEYDOWN, (DOWNPOSX1, DOWNPOSY1))
		DISPLAYSURF.blit(KEYUP, (UPPOSX1, UPPOSY1))
		DISPLAYSURF.blit(KEYLEFT, (LEFTPOSX1, LEFTPOSY1))
		DISPLAYSURF.blit(KEYRIGHT, (RIGHTPOSX1, RIGHTPOSY1))
		DISPLAYSURF.blit(KEYRIGHT, (RIGHTPOSX, RIGHTPOSY))
		DISPLAYSURF.blit(KEYUP, (UPPOSX, UPPOSY))
		DISPLAYSURF.blit(KEYDOWN, (DOWNPOSX, DOWNPOSY))
		
		#level 3
		for event in pygame.event.get():
		

			if event.type == pygame.KEYDOWN:
			
				#Left Arrow 1
				if event.key == pygame.K_LEFT and REDSURFACE.collidepoint(LEFTPOSX, LEFTPOSY):
					LEFTPOSY = -10000
					
				#Up Arrow 2
				elif event.key == pygame.K_UP and REDSURFACE.collidepoint(UPPOSX2, UPPOSY2):
					UPPOSY2 = -10000
					
				#Down Arrow 3 
				elif event.key == pygame.K_DOWN and REDSURFACE.collidepoint(DOWNPOSX1, DOWNPOSY1):
					DOWNPOSY1 = -10000

				#Up Arrow 4			
				elif event.key == pygame.K_UP and REDSURFACE.collidepoint(UPPOSX1, UPPOSY1):
					UPPOSY1 = -10000

				#Left Arrow 5	
				elif event.key == pygame.K_LEFT and REDSURFACE.collidepoint(LEFTPOSX1, LEFTPOSY1):
					LEFTPOSY1 = -10000
	
				#Right Arrow 6
				elif event.key == pygame.K_RIGHT and REDSURFACE.collidepoint(RIGHTPOSX1, RIGHTPOSY1):
					RIGHTPOSY1 = -10000	
					
				#Right Arrow 7
				elif event.key == pygame.K_RIGHT and REDSURFACE.collidepoint(RIGHTPOSX, RIGHTPOSY):
					RIGHTPOSY = -10000
					
				#Up Arrow 8
				elif event.key == pygame.K_UP and REDSURFACE.collidepoint(UPPOSX, UPPOSY):
					UPPOSY = -10000
				
				#Down Arrow 9
				elif event.key == pygame.K_DOWN and REDSURFACE.collidepoint(DOWNPOSX, DOWNPOSY):
					DOWNPOSY = -10000
					level_win3()
			
			if event.type == QUIT:
				pygame.quit()
				sys.exit()	
		
		button_no_line ("Music", 55, 715, 65, 25, WHITE, WHITE, )
		button ("On", 50, 750, 35, 20, WHITE, GRAY, MusicOn)
		button ("Off", 100, 750, 35, 20, WHITE, GRAY, MusicOff)
			

		pygame.display.update()
		fpsClock.tick(FPS)
	

def FreeStyleSelect():
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		DISPLAYSURF.fill(WHITE)
		largeText = pygame.font.Font('freesansbold.ttf', 115)
		TextSURF, TextRECT = text_objects("Difficulty", largeText)
		TextRECT.center = ((400), (200))
		DISPLAYSURF.blit(TextSURF, TextRECT)
		
		button("Easy", 150, 450, 100, 50, WHITE, GRAY, FreeStyleEasy)
		
		button("Medium",330, 450, 125, 50, WHITE, GRAY, FreeStyleMedium)
		
		button("Hard", 525, 450, 125, 50, WHITE, GRAY, FreeStyleHard)
		
		button("Main Menu", 650, 725, 125, 50, WHITE, GRAY, main_menu)
		
		button_no_line ("Music", 55, 715, 65, 25, WHITE, WHITE, )
		button ("On", 50, 750, 35, 20, WHITE, GRAY, MusicOn)
		button ("Off", 100, 750, 35, 20, WHITE, GRAY, MusicOff)
		
		pygame.display.update()
		fpsClock.tick(15)


def FreeStyleEasy():

	FPS = 500
	score = 0
	
	
	while True:
	
	
		KeyList = ('KeyUp', 'KeyRight', 'KeyLeft', 'KeyDown')
		RandomKeyGen = (random.choice(KeyList))
		#print (RandomKeyGen)
	
		#Background
		DISPLAYSURF.fill(WHITE)
		
		#Red Bar
		pygame.draw.line(DISPLAYSURF, BLACK, (0, 500), (799, 500), 4)
		pygame.draw.line(DISPLAYSURF, BLACK, (0, 563), (799, 563), 4)
		REDSURFACE = pygame.draw.rect(DISPLAYSURF, RED, (0, 502, 800, 60))


		
		if RandomKeyGen == 'KeyRight':
		
			RightKeyX = 500
			RightKeyY = -10
			
			UpKeyX = 350
			UpKeyY =  -300
			
			
			while True:
			
				if UpKeyY == 562:
					level_lose_easy()
				
				
				if RightKeyY == 562:
					level_lose_easy()
					
				
				DISPLAYSURF.fill(WHITE)
				
				pygame.draw.line(DISPLAYSURF, BLACK, (0, 500), (799, 500), 4)
				pygame.draw.line(DISPLAYSURF, BLACK, (0, 563), (799, 563), 4)
				REDSURFACE = pygame.draw.rect(DISPLAYSURF, RED, (0, 502, 800, 60))
			
				RightKeyY += 1
				UpKeyY += 1
				
				DISPLAYSURF.blit(KEYRIGHT, (RightKeyX, RightKeyY))
				DISPLAYSURF.blit(KEYUP, (UpKeyX, UpKeyY))
			
				for event in pygame.event.get():
					
					if event.type == pygame.KEYDOWN:						
						if event.key == pygame.K_RIGHT and REDSURFACE.collidepoint(RightKeyX, RightKeyY):
							RightKeyY = -1000000

							
					if event.type == pygame.KEYDOWN:		
						if event.key == pygame.K_UP and REDSURFACE.collidepoint(UpKeyX, UpKeyY):
							UpKeyY = -1000
							FreeStyleEasy()
							
							
					
							
					if event.type == QUIT:
							pygame.quit()
							sys.exit()
						
				button_no_line ("Music", 55, 715, 65, 25, WHITE, WHITE, )
				button ("On", 50, 750, 35, 20, WHITE, GRAY, MusicOn)
				button ("Off", 100, 750, 35, 20, WHITE, GRAY, MusicOff)
						
				pygame.display.update()
				fpsClock.tick(FPS)
				
				

				
				
				
		if RandomKeyGen == 'KeyUp':	
		
			UpKeyX = 350
			UpKeyY =  -10
			
			DownKeyX = 450
			DownKeyY =  -300
			
			while True:
			
			
				if DownKeyY == 562:
					level_lose_easy()
				if UpKeyY == 562:
					level_lose_easy()
				
				DISPLAYSURF.fill(WHITE)
				
				pygame.draw.line(DISPLAYSURF, BLACK, (0, 500), (799, 500), 4)
				pygame.draw.line(DISPLAYSURF, BLACK, (0, 563), (799, 563), 4)
				REDSURFACE = pygame.draw.rect(DISPLAYSURF, RED, (0, 502, 800, 60))
				
				DownKeyY += 1
				UpKeyY += 1
			
				DISPLAYSURF.blit(KEYUP, (UpKeyX, UpKeyY))
				DISPLAYSURF.blit(KEYDOWN, (DownKeyX, DownKeyY))
		
				for event in pygame.event.get():			
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_UP and REDSURFACE.collidepoint(UpKeyX, UpKeyY):
							UpKeyY = -10000
							
						elif event.key == pygame.K_DOWN and REDSURFACE.collidepoint(DownKeyX, DownKeyY):	
							DownKeyY = -1000
							FreeStyleEasy()	
							
							
							
							
					if event.type == QUIT:
							pygame.quit()
							sys.exit()
						
				button_no_line ("Music", 55, 715, 65, 25, WHITE, WHITE, )
				button ("On", 50, 750, 35, 20, WHITE, GRAY, MusicOn)
				button ("Off", 100, 750, 35, 20, WHITE, GRAY, MusicOff)
						
				pygame.display.update()
				fpsClock.tick(FPS)
				
				
		if RandomKeyGen == 'KeyDown':
		
			DownKeyX = 450
			DownKeyY =  -10
			
			LeftKeyX = 400
			LeftKeyY =  -300
			
			while True:
				
				if DownKeyY == 562:
					level_lose_easy()
				
				if LeftKeyY == 562:
					level_lose_easy()
				
				
				DISPLAYSURF.fill(WHITE)
				
				pygame.draw.line(DISPLAYSURF, BLACK, (0, 500), (799, 500), 4)
				pygame.draw.line(DISPLAYSURF, BLACK, (0, 563), (799, 563), 4)
				REDSURFACE = pygame.draw.rect(DISPLAYSURF, RED, (0, 502, 800, 60))
				

				LeftKeyY += 1
				DownKeyY += 1
				
				DISPLAYSURF.blit(KEYDOWN, (DownKeyX, DownKeyY))
				DISPLAYSURF.blit(KEYLEFT, (LeftKeyX, LeftKeyY))
			
			
				for event in pygame.event.get():		
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_DOWN and REDSURFACE.collidepoint(DownKeyX, DownKeyY):	
							DownKeyY = -1000
							
						elif event.key == pygame.K_LEFT and REDSURFACE.collidepoint(LeftKeyX, LeftKeyY):
							LeftKeyY = -1000
							FreeStyleEasy()
							
					if event.type == QUIT:
						pygame.quit()
						sys.exit()
							
				button_no_line ("Music", 55, 715, 65, 25, WHITE, WHITE, )
				button ("On", 50, 750, 35, 20, WHITE, GRAY, MusicOn)
				button ("Off", 100, 750, 35, 20, WHITE, GRAY, MusicOff)
							
				pygame.display.update()
				fpsClock.tick(FPS)
				
			
		if RandomKeyGen == 'KeyLeft':	
		
			LeftKeyX = 400
			LeftKeyY =  -10
			
			UpKeyX = 350
			UpKeyY =  -300
			
			while True:
			
				if LeftKeyY == 562:
					level_lose_easy()
					
				if UpKeyY == 562:
					level_lose_easy()
			
			
				DISPLAYSURF.fill(WHITE)
				
				pygame.draw.line(DISPLAYSURF, BLACK, (0, 500), (799, 500), 4)
				pygame.draw.line(DISPLAYSURF, BLACK, (0, 563), (799, 563), 4)
				REDSURFACE = pygame.draw.rect(DISPLAYSURF, RED, (0, 502, 800, 60))
				
				UpKeyY += 1
				LeftKeyY += 1
		
				DISPLAYSURF.blit(KEYLEFT, (LeftKeyX, LeftKeyY))
				DISPLAYSURF.blit(KEYUP, (UpKeyX, UpKeyY))
			
				for event in pygame.event.get():			
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_LEFT and REDSURFACE.collidepoint(LeftKeyX, LeftKeyY):
							LeftKeyY = -1000
							
						elif event.key == pygame.K_UP and REDSURFACE.collidepoint(UpKeyX, UpKeyY):
							UpKeyY = -10000
							FreeStyleEasy()
							
					if event.type == QUIT:
						pygame.quit()
						sys.exit()
					
				button_no_line ("Music", 55, 715, 65, 25, WHITE, WHITE, )
				button ("On", 50, 750, 35, 20, WHITE, GRAY, MusicOn)
				button ("Off", 100, 750, 35, 20, WHITE, GRAY, MusicOff)
					
				pygame.display.update()
				fpsClock.tick(FPS)
					
				
		button_no_line ("Music", 55, 715, 65, 25, WHITE, WHITE, )
		button ("On", 50, 750, 35, 20, WHITE, GRAY, MusicOn)
		button ("Off", 100, 750, 35, 20, WHITE, GRAY, MusicOff)
		
		pygame.display.update()
		fpsClock.tick(FPS)
		
		
		
		
		
		
		
		
def FreeStyleMedium():

	FPS = 450
	score = 0
	
	
	while True:
	
	
		KeyList = ('KeyUp', 'KeyRight', 'KeyLeft', 'KeyDown')
		RandomKeyGen = (random.choice(KeyList))
		#print (RandomKeyGen)
	
		#Background
		DISPLAYSURF.fill(WHITE)
		
		#Red Bar
		pygame.draw.line(DISPLAYSURF, BLACK, (0, 500), (799, 500), 4)
		pygame.draw.line(DISPLAYSURF, BLACK, (0, 563), (799, 563), 4)
		REDSURFACE = pygame.draw.rect(DISPLAYSURF, RED, (0, 502, 800, 60))


		
		if RandomKeyGen == 'KeyRight':
		
			RightKeyX = 500
			RightKeyY = 1
			
			
			
			while True:
				
				
				
				if RightKeyY == 562:
					level_lose_medium()
					
				
				DISPLAYSURF.fill(WHITE)
				
				pygame.draw.line(DISPLAYSURF, BLACK, (0, 500), (799, 500), 4)
				pygame.draw.line(DISPLAYSURF, BLACK, (0, 563), (799, 563), 4)
				REDSURFACE = pygame.draw.rect(DISPLAYSURF, RED, (0, 502, 800, 60))
			
				RightKeyY += 1
			
				DISPLAYSURF.blit(KEYRIGHT, (RightKeyX, RightKeyY))
			
				for event in pygame.event.get():
		
					if event.type == pygame.KEYDOWN:						
						if event.key == pygame.K_RIGHT and REDSURFACE.collidepoint(RightKeyX, RightKeyY):
							FreeStyleMedium()
							
							
							
							
					if event.type == QUIT:
							pygame.quit()
							sys.exit()
						
				button_no_line ("Music", 55, 715, 65, 25, WHITE, WHITE, )
				button ("On", 50, 750, 35, 20, WHITE, GRAY, MusicOn)
				button ("Off", 100, 750, 35, 20, WHITE, GRAY, MusicOff)
						
				pygame.display.update()
				fpsClock.tick(FPS)
				
				

				
				
				
		if RandomKeyGen == 'KeyUp':	
		
			UpKeyX = 350
			UpKeyY =  1
			
			while True:
			
				if UpKeyY == 562:
					level_lose_medium()
				
				DISPLAYSURF.fill(WHITE)
				
				pygame.draw.line(DISPLAYSURF, BLACK, (0, 500), (799, 500), 4)
				pygame.draw.line(DISPLAYSURF, BLACK, (0, 563), (799, 563), 4)
				REDSURFACE = pygame.draw.rect(DISPLAYSURF, RED, (0, 502, 800, 60))
				
				UpKeyY += 1
			
				DISPLAYSURF.blit(KEYUP, (UpKeyX, UpKeyY))
			
		
				for event in pygame.event.get():			
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_UP and REDSURFACE.collidepoint(UpKeyX, UpKeyY):
							UpKeyY = -1000
							FreeStyleMedium()
					if event.type == QUIT:
							pygame.quit()
							sys.exit()
						
				button_no_line ("Music", 55, 715, 65, 25, WHITE, WHITE, )
				button ("On", 50, 750, 35, 20, WHITE, GRAY, MusicOn)
				button ("Off", 100, 750, 35, 20, WHITE, GRAY, MusicOff)
						
				pygame.display.update()
				fpsClock.tick(FPS)
				
				
		if RandomKeyGen == 'KeyDown':
		
			DownKeyX = 450
			DownKeyY =  1
			
			while True:
				
				if DownKeyY == 562:
					level_lose_medium()
				
				
				DISPLAYSURF.fill(WHITE)
				
				pygame.draw.line(DISPLAYSURF, BLACK, (0, 500), (799, 500), 4)
				pygame.draw.line(DISPLAYSURF, BLACK, (0, 563), (799, 563), 4)
				REDSURFACE = pygame.draw.rect(DISPLAYSURF, RED, (0, 502, 800, 60))
				

				
				DownKeyY += 1
				
				DISPLAYSURF.blit(KEYDOWN, (DownKeyX, DownKeyY))
		
			
			
				for event in pygame.event.get():		
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_DOWN and REDSURFACE.collidepoint(DownKeyX, DownKeyY):	
							DownKeyY = -1000
							FreeStyleMedium()
							
					if event.type == QUIT:
						pygame.quit()
						sys.exit()
						
				button_no_line ("Music", 55, 715, 65, 25, WHITE, WHITE, )
				button ("On", 50, 750, 35, 20, WHITE, GRAY, MusicOn)
				button ("Off", 100, 750, 35, 20, WHITE, GRAY, MusicOff)
						
				pygame.display.update()
				fpsClock.tick(FPS)
				
			
		if RandomKeyGen == 'KeyLeft':	
		
			LeftKeyX = 400
			LeftKeyY =  1
			
			while True:
			
				if LeftKeyY == 562:
					level_lose_medium()
			
			
				DISPLAYSURF.fill(WHITE)
				
				pygame.draw.line(DISPLAYSURF, BLACK, (0, 500), (799, 500), 4)
				pygame.draw.line(DISPLAYSURF, BLACK, (0, 563), (799, 563), 4)
				REDSURFACE = pygame.draw.rect(DISPLAYSURF, RED, (0, 502, 800, 60))
			
				LeftKeyY += 1
		
				DISPLAYSURF.blit(KEYLEFT, (LeftKeyX, LeftKeyY))
		
			
				for event in pygame.event.get():			
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_LEFT and REDSURFACE.collidepoint(LeftKeyX, LeftKeyY):
							LeftKeyY = -1000
							FreeStyleMedium()
							
					if event.type == QUIT:
						pygame.quit()
						sys.exit()
					
				button_no_line ("Music", 55, 715, 65, 25, WHITE, WHITE, )
				button ("On", 50, 750, 35, 20, WHITE, GRAY, MusicOn)
				button ("Off", 100, 750, 35, 20, WHITE, GRAY, MusicOff)
					
				pygame.display.update()
				fpsClock.tick(FPS)
					
				
		button_no_line ("Music", 55, 715, 65, 25, WHITE, WHITE, )
		button ("On", 50, 750, 35, 20, WHITE, GRAY, MusicOn)
		button ("Off", 100, 750, 35, 20, WHITE, GRAY, MusicOff)
		
		pygame.display.update()
		fpsClock.tick(FPS)




		
def FreeStyleHard():

	FPS = 650
	score = 0
	
	
	while True:
	
	
		KeyList = ('KeyUp', 'KeyRight', 'KeyLeft', 'KeyDown')
		RandomKeyGen = (random.choice(KeyList))
		#print (RandomKeyGen)
	
		#Background
		DISPLAYSURF.fill(WHITE)
		
		#Red Bar
		pygame.draw.line(DISPLAYSURF, BLACK, (0, 500), (799, 500), 4)
		pygame.draw.line(DISPLAYSURF, BLACK, (0, 563), (799, 563), 4)
		REDSURFACE = pygame.draw.rect(DISPLAYSURF, RED, (0, 502, 800, 60))


		
		if RandomKeyGen == 'KeyRight':
		
			RightKeyX = 500
			RightKeyY = 1
			
			
			
			while True:
				
				
				
				if RightKeyY == 562:
					level_lose_hard()
					
				
				DISPLAYSURF.fill(WHITE)
				
				pygame.draw.line(DISPLAYSURF, BLACK, (0, 500), (799, 500), 4)
				pygame.draw.line(DISPLAYSURF, BLACK, (0, 563), (799, 563), 4)
				REDSURFACE = pygame.draw.rect(DISPLAYSURF, RED, (0, 502, 800, 60))
			
				RightKeyY += 1
			
				DISPLAYSURF.blit(KEYRIGHT, (RightKeyX, RightKeyY))
			
				for event in pygame.event.get():
		
					if event.type == pygame.KEYDOWN:						
						if event.key == pygame.K_RIGHT and REDSURFACE.collidepoint(RightKeyX, RightKeyY):
							FreeStyleHard()
							
							
							
							
					if event.type == QUIT:
							pygame.quit()
							sys.exit()
						
				button_no_line ("Music", 55, 715, 65, 25, WHITE, WHITE, )
				button ("On", 50, 750, 35, 20, WHITE, GRAY, MusicOn)
				button ("Off", 100, 750, 35, 20, WHITE, GRAY, MusicOff)
						
				pygame.display.update()
				fpsClock.tick(FPS)
				
				

				
				
				
		if RandomKeyGen == 'KeyUp':	
		
			UpKeyX = 350
			UpKeyY =  1
			
			while True:
			
				if UpKeyY == 562:
					level_lose_hard()
				
				DISPLAYSURF.fill(WHITE)
				
				pygame.draw.line(DISPLAYSURF, BLACK, (0, 500), (799, 500), 4)
				pygame.draw.line(DISPLAYSURF, BLACK, (0, 563), (799, 563), 4)
				REDSURFACE = pygame.draw.rect(DISPLAYSURF, RED, (0, 502, 800, 60))
				
				UpKeyY += 1
			
				DISPLAYSURF.blit(KEYUP, (UpKeyX, UpKeyY))
			
		
				for event in pygame.event.get():			
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_UP and REDSURFACE.collidepoint(UpKeyX, UpKeyY):
							UpKeyY = -1000
							FreeStyleHard()
					if event.type == QUIT:
							pygame.quit()
							sys.exit()
						
				button_no_line ("Music", 55, 715, 65, 25, WHITE, WHITE, )
				button ("On", 50, 750, 35, 20, WHITE, GRAY, MusicOn)
				button ("Off", 100, 750, 35, 20, WHITE, GRAY, MusicOff)
						
				pygame.display.update()
				fpsClock.tick(FPS)
				
				
		if RandomKeyGen == 'KeyDown':
		
			DownKeyX = 450
			DownKeyY =  1
			
			while True:
				
				if DownKeyY == 562:
					level_lose_hard()
				
				
				DISPLAYSURF.fill(WHITE)
				
				pygame.draw.line(DISPLAYSURF, BLACK, (0, 500), (799, 500), 4)
				pygame.draw.line(DISPLAYSURF, BLACK, (0, 563), (799, 563), 4)
				REDSURFACE = pygame.draw.rect(DISPLAYSURF, RED, (0, 502, 800, 60))
				

				
				DownKeyY += 1
				
				DISPLAYSURF.blit(KEYDOWN, (DownKeyX, DownKeyY))
		
			
			
				for event in pygame.event.get():		
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_DOWN and REDSURFACE.collidepoint(DownKeyX, DownKeyY):	
							DownKeyY = -1000
							FreeStyleHard()
							
					if event.type == QUIT:
						pygame.quit()
						sys.exit()
							
				button_no_line ("Music", 55, 715, 65, 25, WHITE, WHITE, )
				button ("On", 50, 750, 35, 20, WHITE, GRAY, MusicOn)
				button ("Off", 100, 750, 35, 20, WHITE, GRAY, MusicOff)
							
				pygame.display.update()
				fpsClock.tick(FPS)
				
			
		if RandomKeyGen == 'KeyLeft':	
		
			LeftKeyX = 400
			LeftKeyY =  1
			
			while True:
			
				if LeftKeyY == 562:
					level_lose_hard()
			
			
				DISPLAYSURF.fill(WHITE)
				
				pygame.draw.line(DISPLAYSURF, BLACK, (0, 500), (799, 500), 4)
				pygame.draw.line(DISPLAYSURF, BLACK, (0, 563), (799, 563), 4)
				REDSURFACE = pygame.draw.rect(DISPLAYSURF, RED, (0, 502, 800, 60))
			
				LeftKeyY += 1
		
				DISPLAYSURF.blit(KEYLEFT, (LeftKeyX, LeftKeyY))
		
			
				for event in pygame.event.get():			
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_LEFT and REDSURFACE.collidepoint(LeftKeyX, LeftKeyY):
							LeftKeyY = -1000
							FreeStyleHard()
							
					if event.type == QUIT:
						pygame.quit()
						sys.exit()
					
				button_no_line ("Music", 55, 715, 65, 25, WHITE, WHITE, )
				button ("On", 50, 750, 35, 20, WHITE, GRAY, MusicOn)
				button ("Off", 100, 750, 35, 20, WHITE, GRAY, MusicOff)
					
				pygame.display.update()
				fpsClock.tick(FPS)
					
				
		button_no_line ("Music", 55, 715, 65, 25, WHITE, WHITE, )
		button ("On", 50, 750, 35, 20, WHITE, GRAY, MusicOn)
		button ("Off", 100, 750, 35, 20, WHITE, GRAY, MusicOff)
		
		pygame.display.update()
		fpsClock.tick(FPS)


		
	
game_intro()