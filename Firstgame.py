__author__ ='Circler'
import pygame
WHITE = (255,255,255)
pad_width=1024
pad_height = 512


def Face_load(temp_x,temp_y):
	global gamepad, clock
	gamepad.blit(face_img,(temp_x,temp_y))
def runGame():
	global gamepad, clock
	face_x = pad_width*0.05
	face_y = pad_height*0.8
	face_x_change = 0
	face_y_change = 0
	
	crashed = False
	while not crashed:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				crashed=True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					crashed=True
				elif event.key == pygame.K_UP:
					face_y_change += -5
				elif event.key == pygame.K_DOWN:
					face_y_change += 5
				elif event.key == pygame.K_LEFT:
					face_x_change += -5
				elif event.key == pygame.K_RIGHT:
					face_x_change += 5
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					face_x_change=0
					face_y_change=0
		
		gamepad.fill(WHITE)
		face_x+=face_x_change
		face_y+=face_y_change
		Face_load(face_x,face_y)
		pygame.display.update()
		clock.tick(60)
		
	pygame.quit()
	quit()
def initGame():
	global gamepad, clock, face_img
	pygame.init()
	gamepad=pygame.display.set_mode((pad_width,pad_height))
	pygame.display.set_caption("Circler");
	face_img=pygame.image.load("image/face.jpg")
	pygame.mixer.music.load("music/Fuck.mp3")
	pygame.mixer.music.play(0,0.0)
	
	clock=pygame.time.Clock()
	runGame()
	
	

initGame()