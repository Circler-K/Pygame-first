__author__ ='Circler'
import pygame
import random
WHITE = (255,255,255)
pad_width=1024
pad_height = 512
	
def drawObject(obj,temp_x,temp_y):
	global gamepad, clock, JollaMan_img, background_img,bat_img
	gamepad.blit(obj,(temp_x,temp_y))

def runGame():
	global gamepad, clock, JollaMan_img, background_img, bat_img
	JollaMan_x = pad_width*0.05
	JollaMan_y = pad_height*0.8
	JollaMan_x_change = 0
	JollaMan_y_change = 0
	
	bat_x =  pad_width
	bat_y = random.randrange(0,pad_height)
	
	
	crashed = False
	while not crashed:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				crashed=True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					crashed=True
				elif event.key == pygame.K_UP:
					JollaMan_y_change += -5
				elif event.key == pygame.K_DOWN:
					JollaMan_y_change += 5
				elif event.key == pygame.K_LEFT:
					JollaMan_x_change += -5
				elif event.key == pygame.K_RIGHT:
					JollaMan_x_change += 5
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					JollaMan_x_change=0
					JollaMan_y_change=0
		
		#게임패드 그리기
		gamepad.fill(WHITE)
		drawObject(background_img,0,0)
		
		#졸라맨 그리기
		JollaMan_x+=JollaMan_x_change
		JollaMan_y+=JollaMan_y_change
		drawObject(JollaMan_img,JollaMan_x,JollaMan_y)
		
		#박쥐 그리기
		bat_x -=7
		if bat_x <=0:
			bat_x = pad_width
			bat_y = random.randrange(0,pad_height)
		drawObject(bat_img,bat_x,bat_y)
		
		pygame.display.update()
		clock.tick(100)
		
	pygame.quit()
	quit()
	
def initGame():
	global gamepad, clock, JollaMan_img, background_img,bat_img
	pygame.init()
	gamepad=pygame.display.set_mode((pad_width,pad_height))
	pygame.display.set_caption("Jolla Game~");
	JollaMan_img=pygame.image.load("image/jolla.png")
	background_img=pygame.image.load("image/background.png")
	bat_img = pygame.image.load("image/bat.png")
	bullet_img = pygame.image.load("image/bullet.png")
	pygame.mixer.music.load("music/Fuck.mp3")
	pygame.mixer.music.play(0,0.0)
	clock=pygame.time.Clock()
	runGame()

if __name__ =="__main__":
	initGame()