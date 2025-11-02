import pygame
from random import * 

pygame.init()

scrn_hght = 1000
scrn_wdth = 1000

screen = pygame.display.set_mode((scrn_wdth, scrn_hght))

snoww = (230, 230, 230)
blackish = (30, 30, 30)

drivin = pygame.Rect(200, 200, 75, 75)
inside = pygame.Rect(75, 75, 850, 850)

sliderole = pygame.Rect(300, 19, 400, 37) 
slider = pygame.Rect(300, 17, 35, 41)

hintrect = pygame.Rect(295, 943, 400, 37)
font1 = pygame.font.SysFont(None, 36)
hint = font1.render("Press 'enter' to start / pause...", True, (50, 50, 50))

slider_min = sliderole.x - 1
slider_max = sliderole.x + sliderole.width + 1

drivin_value = False
drivin_speed = 2

movement = pygame.USEREVENT + 1
move_interval = 10
pygame.time.set_timer(movement, move_interval) 

def randomin():
	pass

hint_show = True
clock = pygame.time.Clock()
runnin = True

while runnin:

	screen.fill(blackish)

	mouse_held = pygame.mouse.get_pressed()
	mouse_x, mouse_y = pygame.mouse.get_pos() 

	if mouse_held[0]:
		if mouse_x in range(slider.x - 15, slider.x + slider.width + 15) and \
		 mouse_y in range(slider.y - 15, slider.y + slider.height + 15):
			slider.x = mouse_x - slider.width / 2


	if slider.x < slider_min:
		slider.x = slider_min + 1
	if slider.x + slider.width > slider_max:
		slider.x = slider_max - slider.width - 1

	if slider.x < sliderole.x + sliderole.width / 6:
		drivin_speed = 2
	elif slider.x < sliderole.x + sliderole.width / 2.25:
		drivin_speed = 4
	elif slider.x < sliderole.x + sliderole.width / 1.5:
		drivin_speed = 8
	elif slider.x < sliderole.x + sliderole.width / 0.9:
		drivin_speed = 11

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			runnin = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:
				if drivin_value == False:
					drivin_value = True
				else:
					drivin_value = False
				hint_show = False
		if event.type == movement:
			randomin()

	if drivin_value == True:
		def randomin():
			def mtop():
				drivin.y -= drivin_speed
			def mbottom():
				drivin.y += drivin_speed
			def mright():
				drivin.x += drivin_speed
			def mleft():
				drivin.x -= drivin_speed
			def mbottomright():
				drivin.x += drivin_speed
				drivin.y += drivin_speed
			def mtopright():
				drivin.x += drivin_speed
				drivin.y -= drivin_speed
			def mbottomleft():
				drivin.x -= drivin_speed
				drivin.y += drivin_speed
			def mtopleft():
				drivin.x -= drivin_speed
				drivin.y -= drivin_speed
			moves = mtop, mbottom, mright, mleft, mbottomright, mtopright, mbottomleft, mtopleft
			move = choice(moves)
			move()
	else:
		def randomin():
			pass

	if mouse_held[0]:
		if mouse_x in range(drivin.x - 15, drivin.x + drivin.width + 15) and \
		mouse_y in range(drivin.y - 15, drivin.y + drivin.height + 15):
			drivin.x = mouse_x - drivin.width / 2
			drivin.y = mouse_y - drivin.height / 2

	if drivin.top < inside.top:
		drivin.top = inside.top
	if drivin.bottom > inside.bottom:
		drivin.bottom = inside.bottom
	if drivin.right > inside.right:
		drivin.right = inside.right
	if drivin.left < inside.left:
		drivin.left = inside.left

	pygame.draw.rect(screen, snoww, inside)
	pygame.draw.rect(screen, blackish, drivin)

	pygame.draw.rect(screen, (75, 75, 75), sliderole)
	pygame.draw.rect(screen, snoww, slider)

	if hint_show == True:
		hint_text = hint.get_rect(center=hintrect.center)
		screen.blit(hint, hint_text)

	pygame.display.flip()

	clock.tick(90)