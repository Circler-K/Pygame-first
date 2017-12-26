__author__ ='Circler'
import pygame
import random
from time import sleep
WHITE = (255,255,255)
pad_width=1024
pad_height = 512


def drawObject(obj,temp_x,temp_y):
	global gamepad
	gamepad.blit(obj,(temp_x,temp_y))

def runGame():
	global gamepad, clock, JollaMan_img, background_img, bat_img, bullet_img
	JollaMan_x = 0
	JollaMan_y = 0
	JollaMan_x_change = 0
	JollaMan_y_change = 0
	
	bat_x = pad_width
	bat_y = random.randrange(0,pad_height)
	
	bullet_xy = []
	
	isStriked = False
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
				elif event.key == pygame.K_LCTRL:
					bullet_x = JollaMan_x+60
					bullet_y = JollaMan_y +85
					bullet_xy.append([bullet_x,bullet_y])
				elif event.key == pygame.K_SPACE:
					sleep(1)
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					JollaMan_x_change=0
					JollaMan_y_change=0
		
		
		#게임패드 그리기
		gamepad.fill(WHITE)
		drawObject(background_img,0,0)
		
		
		#박쥐 그리기
		bat_x -=7
		if bat_x <=0:
			bat_x = pad_width
			bat_y = random.randrange(0,pad_height)
		
		#총알 계산
		if len(bullet_xy)!=0:
			for i,bxy in enumerate(bullet_xy):
				bxy[0]+=15
				bullet_xy[i][0] = bxy[0]
				if bxy[0] > bat_x:
					if bxy[1] > bat_y and bxy[1] <= bat_y+75:
						bullet_xy.remove(bxy)
						isStriked = True
				drawObject(bullet_img,bxy[0],bxy[1])
				if bxy[0]>= pad_width:
					bullet_xy.remove(bxy)
		
		
		#졸라맨 그리기
		JollaMan_x+=JollaMan_x_change
		JollaMan_y+=JollaMan_y_change
		drawObject(JollaMan_img,JollaMan_x,JollaMan_y)
		
		
		clock.tick(60)
		
		
		#총알 그리기
		if len(bullet_xy)!=0:
			for bx,by in bullet_xy:
				drawObject(bullet_img,bx,by)
		# 총알 충돌
		if not isStriked:
			drawObject(bat_img,bat_x,bat_y)
		else:
			bat_x = pad_width
			bat_y = random.randrange(0,pad_height)
			isStriked = False
				
		#디스플레이 업데이트!, 항상 마지막에		
		pygame.display.update()
		
		
	pygame.quit()
	quit()
	
def initGame():
	global gamepad, clock, JollaMan_img, background_img,bat_img, bullet_img
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