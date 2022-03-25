import pygame as pg
import math
import random
import os
import sys

'''Game Setup'''
pg.init()
pg.mixer.init()
clock = pg.time.Clock()

'''Constant'''
#----------------------------Screen
SCREEN_WIDTH = 843
SCREEN_HEIGHT = 703
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
NULL = 0

#----------------------------In game default value
DEFAULT_SPEED = 2
DEFAULT_BULLET_TIME = 20
DEFAULT_BULLET_SPEED = 20
PLAYER_RUN = False
WALKCOUNT = 0
time_passed_rooms = 0
time_passed_aisle_x = 0
time_passed_aisle_y = 0
START_ROOMS = False
START_X = False
START_Y = False
FLIP = True
FLIP_X = True
FLIP_Y = True
OBJ_COLLECTED = 0
OBJ_DESTROYED = 0
OBJ_COUNT = 5
rand_bit = random.getrandbits(1)
RAND_MISSION = bool(rand_bit)

'''Setup screen'''
#----------------------------Create screen
SCREEN = pg.display.set_mode(SCREEN_SIZE)

#----------------------------Screen caption and icon
SCREEN_CAPTION = 'Operation Shadowfall'
pg.display.set_caption(SCREEN_CAPTION)
ICON = pg.image.load('icon.png')
pg.display.set_icon(ICON)

#----------------------------Load images
'''player'''
player_image = pg.image.load("character.png")
player_image = pg.transform.scale(player_image, (35,35))
'''enemy'''
enemy_image = pg.image.load('enemy.png')
enemy_image = pg.transform.scale(enemy_image, (40,40))
'''bullet'''
bullet_image = pg.image.load("bullet_player.png")
bullet_image = pg.transform.scale(bullet_image, (8,8))
'''player animation'''
player_idle = pg.image.load('survivor-idle_0.png')
player_idle = pg.transform.scale(player_idle, (25,25))
player_run1 = pg.image.load('survivor-run_0.png')
player_run1 = pg.transform.scale(player_run1, (25,25))
player_run2 = pg.image.load('survivor-run_1.png')
player_run2 = pg.transform.scale(player_run2, (25,25))
player_run3 = pg.image.load('survivor-run_2.png')
player_run3 = pg.transform.scale(player_run3, (25,25))
player_run4 = pg.image.load('survivor-run_3.png')
player_run4 = pg.transform.scale(player_run4, (25,25))
player_run5 = pg.image.load('survivor-run_4.png')
player_run5 = pg.transform.scale(player_run5, (25,25))
player_run6 = pg.image.load('survivor-run_5.png')
player_run6 = pg.transform.scale(player_run6, (25,25))
player_run7 = pg.image.load('survivor-run_6.png')
player_run7 = pg.transform.scale(player_run7, (25,25))
player_run8 = pg.image.load('survivor-run_7.png')
player_run8 = pg.transform.scale(player_run8, (25,25))
player_run9 = pg.image.load('survivor-run_8.png')
player_run9 = pg.transform.scale(player_run9, (25,25))
player_run10 = pg.image.load('survivor-run_9.png')
player_run10 = pg.transform.scale(player_run10, (25,25))
player_run11 = pg.image.load('survivor-run_10.png')
player_run11 = pg.transform.scale(player_run11, (25,25))
player_run12 = pg.image.load('survivor-run_11.png')
player_run12 = pg.transform.scale(player_run12, (25,25))
player_run13 = pg.image.load('survivor-run_12.png')
player_run13 = pg.transform.scale(player_run13, (25,25))
player_run14 = pg.image.load('survivor-run_13.png')
player_run14 = pg.transform.scale(player_run14, (25,25))
player_run15 = pg.image.load('survivor-run_14.png')
player_run15 = pg.transform.scale(player_run15, (25,25))
player_run16 = pg.image.load('survivor-run_15.png')
player_run16 = pg.transform.scale(player_run16, (25,25))
player_run17 = pg.image.load('survivor-run_16.png')
player_run17 = pg.transform.scale(player_run17, (25,25))
player_run18 = pg.image.load('survivor-run_17.png')
player_run18 = pg.transform.scale(player_run18, (25,25))
player_run19 = pg.image.load('survivor-run_18.png')
player_run19 = pg.transform.scale(player_run19, (25,25))
player_run25 = pg.image.load('survivor-run_19.png')
player_run25 = pg.transform.scale(player_run25, (25,25))
movement_image = [player_run1, player_run2, player_run3, player_run4, player_run5, player_run6, player_run7, player_run8, player_run9, player_run10, player_run11, player_run12, player_run13, player_run14, player_run15, player_run16, player_run17, player_run18, player_run19, player_run25]
'''map'''
bg_image = pg.image.load('map.png')
bg_image = pg.transform.scale(bg_image, (843,703))
'''main menu'''
menu_img = pg.image.load('menu.png')
menu_img_2 = pg.image.load('menu.jpg')
'''aisle x'''
los_img = pg.image.load('los.png')
los_img = pg.transform.scale(los_img, (100,35))
los_img_left = pg.image.load('los_left.png')
los_img_left = pg.transform.scale(los_img_left, (100,35))
'''aisle y'''
los_img_down = pg.image.load('los_down.png')
los_img_down = pg.transform.scale(los_img_down, (35,100))
los_img_top = pg.image.load('los_top.png')
los_img_top = pg.transform.scale(los_img_top, (35,100))
'''rooms'''
los_img_rooms = pg.image.load('los.png')
los_img_rooms = pg.transform.scale(los_img_rooms, (33,33))
los_img_rooms_left = pg.image.load('los_left.png')
los_img_rooms_left = pg.transform.scale(los_img_rooms_left, (33,33))
los_img_rooms_down = pg.image.load('los_down.png')
los_img_rooms_down = pg.transform.scale(los_img_rooms_down, (33,33))
los_img_rooms_top = pg.image.load('los_top.png')
los_img_rooms_top = pg.transform.scale(los_img_rooms_top, (33,33))
'''objectives'''
objective_img_destroy = pg.image.load('objective_destroy.png')
objective_img_destroy = pg.transform.scale(objective_img_destroy, (20,20))
objective_img_collect = pg.image.load('objective_collect.png')
objective_img_collect = pg.transform.scale(objective_img_collect, (20,20))
'''tutorial image'''
collect_demo = pg.image.load('objective_collect.png')
collect_demo = pg.transform.scale(collect_demo, (80,80))
destroy_demo = pg.image.load('objective_destroy.png')
destroy_demo = pg.transform.scale(destroy_demo, (80,80))

#------------------------Sound
SHOOT_SOUND = pg.mixer.Sound('gunshot.ogg')
SHOOT_SOUND.set_volume(0.1)
BGM = pg.mixer.Sound('bgm.ogg')
BGM.set_volume(0.1)
INGAME = pg.mixer.Sound('ingame_bgm.ogg')
INGAME.set_volume(0.1)
COMPLETE = pg.mixer.Sound('victory.ogg')
COMPLETE.set_volume(0.1)
MISSION_FAIL = pg.mixer.Sound('mission_fail.ogg')
MISSION_FAIL.set_volume(0.1)
FAIL = pg.mixer.Sound('fail.ogg')
FAIL.set_volume(0.1)
COLLECT = pg.mixer.Sound('pick_up.ogg')
DESTROY = pg.mixer.Sound('destroy.ogg')
DESTROY.set_volume(0.1)
HIT = pg.mixer.Sound('hit.ogg')
HIT.set_volume(0.1)


'''Game components'''
#wall class
class Wall(pg.sprite.Sprite):
	def __init__(self, x, y, w, h, angle):
		super().__init__()
		self.image = pg.Surface((w, h), pg.SRCALPHA)
		self.image.fill(pg.Color('sienna2'))
		self.rotate_image = pg.transform.rotate(self.image, angle)
		self.rect = self.rotate_image.get_rect(topleft=(x,y))

	def draw(self, SCREEN):
		SCREEN.blit(self.rotate_image, self.rect)

#player class
class create_player(pg.sprite.Sprite):
	def __init__(self, x_pos, y_pos):
		super().__init__()
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.image = player_image
		self.rect = self.image.get_rect(center=(x_pos,y_pos))

#movement class
class create_movement(pg.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.image = movement_image[0]
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.rect = self.image.get_rect(center=(pos_x,pos_y))

#enemy class
class Enemy(pg.sprite.Sprite):
	def __init__(self,x_pos,y_pos,end_x,end_y):
		super().__init__()
		self.health = 100
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.end_x = end_x
		self.end_y = end_y
		self.path_x = [self.x_pos, self.end_x]
		self.path_y = [self.y_pos, self.end_y]
		self.image = enemy_image
		self.rect = self.image.get_rect(center=(self.x_pos,self.y_pos))
		self.enemy_walkcount = 0
		self.vel = 1

	def movement_square(self,SCREEN):
		if self.vel > 0:
			if self.x_pos + self.vel < self.path_x[1]:
				self.x_pos += self.vel
				self.rect.move_ip(self.vel, 0)
				if self.x_pos + self.vel == self.path_x[1]:
					self.image = pg.transform.rotate(self.image, -90)
			elif self.y_pos + self.vel < self.path_y[1]:
				self.y_pos += self.vel
				self.rect.move_ip(0,self.vel)
			else:
				self.image = pg.transform.rotate(self.image, -90)
				self.vel = self.vel * -1
				self.enemy_walkcount = 0
		else:
			if self.x_pos - self.vel > self.path_x[0]:
				self.x_pos += self.vel
				self.rect.move_ip(self.vel,0)
				if self.x_pos - self.vel == self.path_x[0]:
					self.image = pg.transform.rotate(self.image, -90)
			elif self.y_pos - self.vel > self.path_y[0]:
				self.y_pos += self.vel
				self.rect.move_ip(0,self.vel)
			else:
				self.image = pg.transform.rotate(self.image, -90)
				self.vel = self.vel * -1
				self.enemy_walkcount = 0

		SCREEN.blit(self.image, self.rect)

	def movement_x(self,SCREEN):
		if self.vel > 0:
			if self.x_pos + self.vel < self.path_x[1]:
				self.x_pos += self.vel
				self.rect.move_ip(self.vel, 0)
			else:
				self.image = pg.transform.rotate(self.image, -180)
				self.vel = self.vel * -1
				self.enemy_walkcount = 0
		else:
			if self.x_pos - self.vel > self.path_x[0]:
				self.x_pos += self.vel
				self.rect.move_ip(self.vel, 0)
			else:
				self.image = pg.transform.rotate(self.image, 180)
				self.vel = self.vel * -1
				self.enemy_walkcount = 0

		SCREEN.blit(self.image, self.rect)

	def movement_y(self,SCREEN):
		if self.vel > 0:
			if self.y_pos + self.vel < self.path_y[1]:
				self.y_pos += self.vel
				self.rect.move_ip(0,self.vel)
			else:
				self.image = pg.transform.rotate(self.image, -180)
				self.vel = self.vel * -1
				self.enemy_walkcount = 0
		else:
			if self.y_pos - self.vel > self.path_y[0]:
				self.y_pos += self.vel
				self.rect.move_ip(0,self.vel)
			else:
				self.image = pg.transform.rotate(self.image, 180)
				self.vel = self.vel * -1
				self.enemy_walkcount = 0
		rotate_img = pg.transform.rotate(self.image, -90)
		SCREEN.blit(rotate_img, self.rect)

#LOS class
class Lineofsight(pg.sprite.Sprite):
	def __init__(self,x_pos,y_pos,end_x,end_y):
		super().__init__()
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.end_x = end_x
		self.end_y = end_y
		self.path_x = [self.x_pos, self.end_x]
		self.path_y = [self.y_pos, self.end_y]
		'''aisle x'''
		self.image = los_img
		self.image_left = los_img_left
		'''aisle y'''
		self.image_down = los_img_down
		self.image_top = los_img_top
		'''rooms'''
		self.image_rooms = los_img_rooms
		self.image_rooms_left = los_img_rooms_left
		self.image_rooms_down = los_img_rooms_down
		self.image_rooms_top = los_img_rooms_top
		'''aisle x'''
		self.rect = self.image.get_rect(midleft=(self.x_pos,self.y_pos))
		self.rect_left = self.image_left.get_rect(midright=(self.x_pos+100, self.y_pos))
		'''aisle y'''
		self.rect_down = self.image_down.get_rect(midtop=(self.x_pos, self.y_pos))
		self.rect_top = self.image_top.get_rect(midbottom=(self.x_pos, self.y_pos+100))
		'''rooms'''
		self.rect_room = self.image_rooms.get_rect(midleft=(self.x_pos, self.y_pos))
		self.rect_room_left = self.image_rooms_left.get_rect(midright=(self.x_pos+30, self.y_pos))
		self.rect_room_top = self.image_rooms_top.get_rect(midbottom=(self.x_pos+15, self.y_pos+15))
		self.rect_room_down = self.image_rooms_down.get_rect(midtop=(self.x_pos+15, self.y_pos-15))
		self.enemy_walkcount = 0
		self.vel = 1

	def movement_square(self,SCREEN):
		if self.vel > 0:
			if self.x_pos + self.vel < self.path_x[1]:
				self.x_pos += self.vel
				self.rect_room.move_ip(self.vel, 0)
				self.rect_room_down.move_ip(self.vel, 0)
				self.rect_room_left.move_ip(self.vel, 0)
				self.rect_room_top.move_ip(self.vel, 0)
				SCREEN.blit(self.image_rooms, self.rect_room)
				if self.x_pos + self.vel >= self.path_x[1]:
					self.rect_room.move_ip(-15,15)
					self.rect_room_down.move_ip(-15,15)
					self.rect_room_left.move_ip(-15,15)
					self.rect_room_top.move_ip(-15,15)
			elif self.y_pos + self.vel < self.path_y[1]:
				self.y_pos += self.vel
				self.rect_room.move_ip(0,self.vel)
				self.rect_room_down.move_ip(0,self.vel)
				self.rect_room_left.move_ip(0,self.vel)
				self.rect_room_top.move_ip(0,self.vel)
				SCREEN.blit(self.image_rooms_down, self.rect_room_down)
				if self.y_pos + self.vel >= self.path_y[1]:
					self.rect_room.move_ip(-15,-15)
					self.rect_room_down.move_ip(-15,-15)
					self.rect_room_left.move_ip(-15,-15)
					self.rect_room_top.move_ip(-15,-15)
			else:
				self.vel = self.vel * -1
				self.enemy_walkcount = 0
		else:
			if self.x_pos - self.vel > self.path_x[0]:
				self.x_pos += self.vel
				self.rect_room.move_ip(self.vel,0)
				self.rect_room_down.move_ip(self.vel, 0)
				self.rect_room_left.move_ip(self.vel, 0)
				self.rect_room_top.move_ip(self.vel, 0)
				SCREEN.blit(self.image_rooms_left, self.rect_room_left)
				if self.x_pos - self.vel <= self.path_x[0]:
					self.rect_room.move_ip(15,-15)
					self.rect_room_down.move_ip(15,-15)
					self.rect_room_left.move_ip(15,-15)
					self.rect_room_top.move_ip(15,-15)
			elif self.y_pos - self.vel > self.path_y[0]:
				self.y_pos += self.vel
				self.rect_room.move_ip(0,self.vel)
				self.rect_room_down.move_ip(0,self.vel)
				self.rect_room_left.move_ip(0,self.vel)
				self.rect_room_top.move_ip(0,self.vel)
				SCREEN.blit(self.image_rooms_top, self.rect_room_top)
				if self.y_pos - self.vel <= self.path_y[0]:
					self.rect_room.move_ip(15,15)
					self.rect_room_down.move_ip(15,15)
					self.rect_room_left.move_ip(15,15)
					self.rect_room_top.move_ip(15,15)
			else:
				self.vel = self.vel * -1
				self.enemy_walkcount = 0

	def movement_x(self,SCREEN):
		if self.vel > 0:
			if self.x_pos + self.vel < self.path_x[1]:
				self.x_pos += self.vel
				self.rect.move_ip(self.vel, 0)
				self.rect_left.move_ip(self.vel, 0)
				SCREEN.blit(self.image, self.rect)
			else:
				self.vel = self.vel * -1
				self.enemy_walkcount = 0
				self.rect.move_ip(-100, 0)
				self.rect_left.move_ip(-100, 0)
		else:
			if self.x_pos - self.vel > self.path_x[0]:
				self.x_pos += self.vel
				self.rect.move_ip(self.vel, 0)
				self.rect_left.move_ip(self.vel, 0)
				SCREEN.blit(self.image_left, self.rect_left)
			else:
				self.vel = self.vel * -1
				self.enemy_walkcount = 0
				self.rect.move_ip(100, 0)
				self.rect_left.move_ip(100, 0)

	def movement_y(self,SCREEN):
		if self.vel > 0:
			if self.y_pos + self.vel < self.path_y[1]:
				self.y_pos += self.vel
				self.rect_down.move_ip(0,self.vel)
				self.rect_top.move_ip(0,self.vel)
				SCREEN.blit(self.image_down, self.rect_down)
			else:
				self.vel = self.vel * -1
				self.enemy_walkcount = 0
				self.rect_down.move_ip(0,-100)
				self.rect_top.move_ip(0,-100)
		else:
			if self.y_pos - self.vel > self.path_y[0]:
				self.y_pos += self.vel
				self.rect_down.move_ip(0,self.vel)
				self.rect_top.move_ip(0,self.vel)
				SCREEN.blit(self.image_top, self.rect_top)
			else:
				self.vel = self.vel * -1
				self.enemy_walkcount = 0
				self.rect_down.move_ip(0,100)
				self.rect_top.move_ip(0,100)

#player's objectives
class Objective(pg.sprite.Sprite):
	def __init__(self, x_pos, y_pos):
		super().__init__()
		self.x_pos = x_pos
		self.y_pos = y_pos
		if RAND_MISSION:
			self.image = objective_img_collect
		else:
			self.image = objective_img_destroy
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

	def draw(self, screen):
		SCREEN.blit(self.image, self.rect)

#bullet class
class create_bullet(object):
	def __init__(self, x_pos, y_pos, mouse_x, mouse_y):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.mouse_x = mouse_x
		self.mouse_y = mouse_y
		self.bullet_time = DEFAULT_BULLET_TIME
		self.bullet_speed = DEFAULT_BULLET_SPEED
		#calculate bullet position
		self.angle = math.atan2(mouse_y-self.y_pos, mouse_x-self.x_pos)
		self.vel_x = math.cos(self.angle) * self.bullet_speed
		self.vel_y = math.sin(self.angle) * self.bullet_speed

	def draw(self, draw):
		self.x_pos += int(self.vel_x)
		self.y_pos += int(self.vel_y)
		self.image = bullet_image
		self.rect = self.image.get_rect(center=(self.x_pos,self.y_pos))
		SCREEN.blit(bullet_image, self.rect)
		self.bullet_time -= 1

#crosshair class
class create_crosshair(pg.sprite.Sprite):
	def __init__(self, image):
		super().__init__()
		self.image = pg.image.load(image)
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.center = pg.mouse.get_pos()

#--------Non class function-----------
#Rotate player function
def rotate(x, y, mouse_pos, img):
		mouse_x, mouse_y = (mouse_pos[0] - x, mouse_pos[1] - y)
		#calculations
		angle = math.degrees(math.atan2(mouse_y, mouse_x))
		rotate_img = pg.transform.rotate(img, -angle)
		rect = rotate_img.get_rect(center=(x,y))
		return rotate_img, rect

#Rotate animation function
def rotate_animation(x, y, mouse_pos, img):
	mouse_x, mouse_y = (mouse_pos[0] - x, mouse_pos[1] - y)
	#calculations
	angle = math.degrees(math.atan2(mouse_y, mouse_x))
	rotate_img = movement_image
	for ani in rotate_img:
		rotate_img = pg.transform.rotate(img, -angle)
	rect = rotate_img.get_rect(center=(x,y))
	return rotate_img, rect

'''Create components'''
#create wall
wall_group = pg.sprite.Group()
'''for i in ((0, 0, 264, 79, 0), (263, 0, 50, 174, 0), (313, 0, 68, 194, 0), (381, 0, 57, 135, 0), (438, 0, 153, 81, 0), 
	(591, 0, 287, 66, 0), (878, 0, 53, 145, 0), (931, 0, 38, 92, 0), (969, 0, 31, 39, 0), (56, 138, 165, 55, 252), 
	(135, 474, 35, 35, 44), (105, 362, 80, 294, 44.5), (138, 278, 80, 294, 44.5)):
	wall_class = Wall(*i)
	wall_group.add(wall_class)'''
'''wall_1 = Wall(0,0,264,79,0)
wall_2 = Wall(263,0,50,174,0)
wall_3 = Wall(313,0,68,194,0)
wall_4 = Wall(381,0,57,135,0)
wall_5 = Wall(438,0,153,81,0)
wall_6 = Wall(591,0,287,66,0)
wall_7 = Wall(878,0,53,145,0)
wall_8 = Wall(931,0,38,92,0)
wall_9 = Wall(969,0,31,39,0)
wall_10 = Wall(56, 138, 165, 55, 252)
wall_11 = Wall(135,474,35,35,44)
wall_12 = Wall(105,362,80,294,44.5)
wall_13 = Wall(138,278,80,294,44.5)
wall_14 = Wall(192, 239, 42, 40, 52)
wall_15 = Wall(223, 267, 44, 38, 37)
wall_16 = Wall(303,265,60,60,-11)
wall_17 = Wall(400,136,80,294,-27)
wall_18 = Wall(492,304,80,294,-21.5)
wall_19 = Wall(668,185,80,294,40)
wall_20 = Wall(720,117,80,294,40)
wall_21 = Wall(886,211,39,53,40)
wall_22 = Wall(870,205,28,23,40)
wall_23 = Wall(765,418,31,56,40)
wall_24 = Wall(797,414,23,57,40)
wall_25 = Wall(801,451,24,34,40)
wall_26 = Wall(886,530,34,44,-11)
wall_27 = Wall(890,575,13,25,-11)
wall_28 = Wall(104,569,47,92,-13)
wall_29 = Wall(0,667,682,44,0)
wall_30 = Wall(682,653,302,80,4)
wall_31 = Wall(144,649,32,18,0)
wall_32 = Wall(230,642,50,25,0)
wall_33 = Wall(411,647,46,20,0)
wall_34 = Wall(459,644,34,23,0)
wall_35 = Wall(423,622,59,45,0)
wall_36 = Wall(626,626,67,41,0)
wall_37 = Wall(695,552,48,88,-8.5)
wall_38 = Wall(723,565,48,88,23)
wall_39 = Wall(766,572,48,88,8)'''
wall_1 = Wall(365,209,128,108,0)
wall_2 = Wall(495,311,47,100,0)
wall_3 = Wall(235,201,35,311,0)
wall_4 = Wall(255,201,130,35,0)
wall_5 = Wall(255,477,113,35,0)
wall_6 = Wall(387,479,102,35,0)
wall_7 = Wall(458,200,55,48,0)
wall_8 = Wall(533,200,83,48,0)
wall_9 = Wall(565,233,51,259,0)
wall_10 = Wall(514,478,102,35,0)
wall_11 = Wall(456,0,45,215,0)
wall_12 = Wall(471,0,253,55,0)
wall_13 = Wall(677,41,47,175,0)
wall_14 = Wall(626,200,190,45,0)
wall_15 = Wall(626,215,55,146,0)
wall_16 = Wall(626,373,55,140,0)
wall_17 = Wall(786,232,30,249,0)
wall_18 = Wall(666,466,150,47,0)
wall_19 = Wall(701,484,65,190,0)
wall_20 = Wall(119,644,612,65,0)
wall_21 = Wall(85,484,64,188,0)
wall_22 = Wall(268,484,39,95,0)
wall_23 = Wall(268,590,39,83,0)
wall_24 = Wall(405,526,38,148,0)
wall_25 = Wall(405,526,84,38,0)
wall_26 = Wall(497,526,50,38,0)
wall_27 = Wall(509,526,38,148,0)
wall_28 = Wall(31,462,164,52,0)
wall_29 = Wall(166,370,58,144,0)
wall_30 = Wall(4,226,57,267,0)
wall_31 = Wall(41,191,112,64,0)
wall_32 = Wall(107,26,62,208,0)
wall_33 = Wall(139,205,86,50,0)
wall_34 = Wall(154,0,220,56,0)
wall_35 = Wall(360,0,40,215,0)
wall_36 = Wall(166,240,16,60,0)
wall_37 = Wall(182,240,1,60,0)
wall_38 = Wall(183,240,1,60,0)
wall_39 = Wall(184,240,1,60,0)
wall_40 = Wall(185,240,16,60,0)
wall_41 = Wall(186,240,1,59,0)
wall_42 = Wall(187,240,1,59,0)
wall_43 = Wall(188,240,16,59,0)
wall_44 = Wall(189,240,16,57,0)
wall_45 = Wall(190,240,16,56,0)
wall_46 = Wall(191,240,16,55,0)
wall_47 = Wall(192,240,16,53,0)
wall_48 = Wall(193,240,16,50,0)
wall_49 = Wall(194,240,16,47,0)
wall_50 = Wall(195,240,16,45,0)
wall_51 = Wall(196,240,16,43,0)
wall_52 = Wall(197,240,16,42,0)
wall_53 = Wall(198,240,16,40,0)
wall_54 = Wall(199,240,16,38,0)
wall_55 = Wall(200,240,16,36,0)
wall_56 = Wall(201,240,16,35,0)
wall_57 = Wall(202,240,16,34,0)
wall_58 = Wall(203,240,16,32,0)
wall_59 = Wall(203,240,16,31,0)
'''wall_list = [wall_1, wall_2, wall_3, wall_4, wall_5, wall_6, wall_7, wall_8, wall_9, wall_10,
				wall_11, wall_12, wall_13, wall_14, wall_15, wall_16, wall_17, wall_18, wall_19, wall_20,
				wall_21, wall_22, wall_23, wall_24, wall_25, wall_26, wall_27, wall_28, wall_29, wall_30,
				wall_31, wall_32, wall_33, wall_34, wall_35, wall_36, wall_37, wall_38, wall_39]'''
wall_list = [wall_1, wall_2, wall_3, wall_4, wall_5, wall_6, wall_7, wall_8, wall_9, wall_10,
			 wall_11, wall_12, wall_13, wall_14, wall_15, wall_16, wall_17, wall_18, wall_19, wall_20,
			 wall_21, wall_22, wall_23, wall_24, wall_25, wall_26, wall_27, wall_28, wall_29, wall_30,
			 wall_31, wall_32, wall_33, wall_34, wall_35, wall_36, wall_37, wall_38, wall_39, wall_40,
			 wall_41, wall_42, wall_43, wall_44, wall_45, wall_46, wall_47, wall_48, wall_49, wall_50,
			 wall_51, wall_52, wall_53, wall_54, wall_55, wall_56, wall_57, wall_58, wall_59]
wall_group.add(wall_list)

#create player
player = create_player(542, 360)
player_group = pg.sprite.Group()
player_group.add(player)

#create movement
moving_animation = create_movement(542, 360)
moving_ani_group = pg.sprite.Group()
moving_ani_group.add(moving_animation)

#create default enemy position in each rooms and aisles
enemy_group = pg.sprite.Group()
enemy_aisle_1 = Enemy(395,520,592,NULL)
enemy_aisle_2 = Enemy(230,222,NULL,545)
enemy_aisle_3 = Enemy(621,220,NULL,475)
enemy_room_1 = Enemy(185,72,345,185)
enemy_room_2 = Enemy(75,273,152,448)
enemy_room_3 = Enemy(455,580,495,632)
enemy_room_4 = Enemy(695,264,775,455)
enemy_room_5 = Enemy(518,73,665,180)

aisle_x = [enemy_aisle_1]
aisle_y = [enemy_aisle_2, enemy_aisle_3]
rooms = [enemy_room_1, enemy_room_2, enemy_room_3, enemy_room_4, enemy_room_5]
temp_aisle_x = []
temp_aisle_y = []
temp_room = []
enemy_list = [enemy_aisle_1, enemy_aisle_2, enemy_aisle_3, enemy_room_1, enemy_room_2, enemy_room_3, enemy_room_4, 
			   enemy_room_5]
enemy_group.add(enemy_list)

#los group
los_group = pg.sprite.Group()
los_enemy_aisle_1 = Lineofsight(395,520,592,NULL)
los_enemy_aisle_2 = Lineofsight(230,222,NULL,545)
los_enemy_aisle_3 = Lineofsight(621,220,NULL,475)
los_enemy_room_1 = Lineofsight(185,72,345,185)
los_enemy_room_2 = Lineofsight(75,273,152,448)
los_enemy_room_3 = Lineofsight(455,580,495,632)
los_enemy_room_4 = Lineofsight(695,264,775,455)
los_enemy_room_5 = Lineofsight(518,73,665,180)
los_enemy_aisle_x = [los_enemy_aisle_1]
los_enemy_aisle_y = [los_enemy_aisle_2,los_enemy_aisle_3]
los_enemy_rooms = [los_enemy_room_1,los_enemy_room_2,los_enemy_room_3,los_enemy_room_4,los_enemy_room_5]
temp_los_aisle_x = []
temp_los_aisle_y = []
temp_los_room = []
los_list = [los_enemy_aisle_1,los_enemy_aisle_2,los_enemy_aisle_3,los_enemy_room_1,los_enemy_room_2,los_enemy_room_3,los_enemy_room_4,los_enemy_room_5]
los_group.add(los_list)

#create objectives group
objective_1 = Objective(320,63)
objective_2 = Objective(67,442)
objective_3 = Objective(454,628)
objective_4 = Objective(763,445)
objective_5 = Objective(585,61)
objective_list = [objective_1, objective_2, objective_3, objective_4, objective_5]
objective_group = pg.sprite.Group()
objective_group.add(objective_list)

#create bullet
bullet = []

#create crosshair
crosshair = create_crosshair("crosshair.png")
crosshair_group = pg.sprite.Group()
crosshair_group.add(crosshair)

'''Draw game elements'''
def remove_cursor():
	#disable cursor
	pg.mouse.set_visible(0)

#draw background
def draw_bg():
	SCREEN.blit(bg_image, (0,0))

#draw crosshair
def draw_crosshair():
	#show crosshair on screen
	crosshair_group.draw(SCREEN)
	crosshair_group.update()

#draw player
def draw_player():
	mouse_x, mouse_y = pg.mouse.get_pos()

	#Set walking animation
	global WALKCOUNT
	if WALKCOUNT + 1 >= 60:
		WALKCOUNT = 0

	if PLAYER_RUN:
		rotate_img, rect = rotate_animation(moving_animation.pos_x, moving_animation.pos_y, (mouse_x, mouse_y), movement_image[WALKCOUNT//3])
		SCREEN.blit(rotate_img, rect)
		WALKCOUNT += 1
	else:
		rotate_img, rect = rotate(moving_animation.pos_x, moving_animation.pos_y, (mouse_x, mouse_y), player_idle)
		SCREEN.blit(rotate_img, rect)

	#image rotate with mouse position
	rotate_img, rect = rotate(player.x_pos, player.y_pos, (mouse_x, mouse_y), player_image)
	SCREEN.blit(rotate_img, rect)
	pg.display.update()

#draw all enemies
def draw_enemy():
	for enemies in aisle_x:
		enemies.movement_x(SCREEN)

	for enemies in aisle_y:
		enemies.movement_y(SCREEN)

	for enemies in rooms:
		enemies.movement_square(SCREEN)

#draw los
def draw_los():
	for los in los_enemy_aisle_x:
		los.movement_x(SCREEN)

	for los in los_enemy_aisle_y:
		los.movement_y(SCREEN)

	for los in los_enemy_rooms:
		los.movement_square(SCREEN)

#draw objectives
def draw_obj():
	for obj in objective_list:
		obj.draw(SCREEN)

#------------------Components for main menu
class Title(object):
	def __init__(self, x_pos, y_pos, text_input):
		self.x_pos = x_pos
		self.y_pos = y_pos
		font = pg.font.Font('EASPORTS15.ttf',60)
		self.text = font.render(text_input, True, (169,169,169))
		self.rect = self.text.get_rect(center=(self.x_pos,self.y_pos))

	def draw(self,screen):
		SCREEN.blit(self.text,self.rect)

class Buttons(object):
	def __init__(self, x_pos, y_pos, text_input):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.width = 200
		self.height = 50
		self.button = pg.Surface((self.width,self.height))
		self.button.fill(pg.Color(169,169,169))
		self.rect = self.button.get_rect(center=(self.x_pos, self.y_pos))
		font = pg.font.Font('EASPORTS15.ttf',30)
		self.text = font.render(text_input, True, (255,255,255))
		self.text_rect = self.text.get_rect(center=(self.x_pos,self.y_pos))

	def draw(self,screen):
		SCREEN.blit(self.button, self.rect)
		SCREEN.blit(self.text, self.text_rect)

class Text(object):
	def __init__(self,x_pos,y_pos,text_input):
		self.x_pos = x_pos
		self.y_pos = y_pos
		font = pg.font.Font('EASPORTS15.ttf',15)
		self.text = font.render(text_input, True, (255,255,255))
		self.rect = self.text.get_rect(midleft=(self.x_pos,self.y_pos))

	def draw(self,screen):
		SCREEN.blit(self.text, self.rect)

class SmallTitle(object):
	def __init__(self,x_pos,y_pos,text_input):
		self.x_pos = x_pos
		self.y_pos = y_pos
		font = pg.font.Font('EASPORTS15.ttf',30)
		self.text = font.render(text_input, True, (255,255,255))
		self.rect = self.text.get_rect(midleft=(self.x_pos,self.y_pos))

	def draw(self,screen):
		SCREEN.blit(self.text, self.rect)

click = False

#--------------------------Functions for UI
'''main menu'''
def main_menu():
	BGM.play(-1)
	global click
	while True:
		pg.mouse.set_visible(1)
		SCREEN.fill((0,0,0))
		SCREEN.blit(menu_img, (0,0))
		main_title = Title(422,150, 'Operation Shadowfall')
		main_title.draw(SCREEN)
		start_game = Buttons(422,300, 'Start')
		how_to_play = Buttons(422,400, 'How to play')
		quit_game = Buttons(422,500, 'Quit')

		start_game.draw(SCREEN)
		how_to_play.draw(SCREEN)
		quit_game.draw(SCREEN)

		x,y = pg.mouse.get_pos()
		if start_game.rect.collidepoint(x,y):
			if click:
				BGM.stop()
				game()
		if how_to_play.rect.collidepoint(x,y):
			if click:
				tutorial()
		if quit_game.rect.collidepoint(x,y):
			if click:
				break

		click = False
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				quit()

			if event.type == pg.MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True

		pg.display.update()
		clock.tick(60)

'''tutorial screen'''
def tutorial():
	pg.mouse.set_visible(1)
	global click
	click = False
	run = True
	while run:
		SCREEN.fill((0,0,0))
		SCREEN.blit(menu_img_2, (0,0))
		tutorial_title = Title(422,100,'How to play')
		tutorial_title.draw(SCREEN)
		introduction = Text(70,170, 'Your name is Agent Spectre. You will be given one of two missions, if you choose to accept it.')
		introduction.draw(SCREEN)
		sub_title_1 = SmallTitle(50,250, 'Mission 1')
		sub_title_1.draw(SCREEN)
		mission_1 = Text(50,300, 'Recover 5 classified information files from')
		mission_1.draw(SCREEN)
		mission_1_1 = Text(50,320, 'the enemy compound without alerting the guards.')
		mission_1_1.draw(SCREEN)
		SCREEN.blit(collect_demo, (450,270))
		sub_title_2 = SmallTitle(50,370, 'Mission 2')
		sub_title_2.draw(SCREEN)
		mission_2 = Text(50,420, 'Destroy 5 computers in the enemy compound to cripple')
		mission_2.draw(SCREEN)
		mission_2_1 = Text(50,440, 'the enemy’s intelligence network without alerting the guards.')
		mission_2_1.draw(SCREEN)
		SCREEN.blit(destroy_demo, (560,380))
		controls = Text(50,540, 'Use WASD to move around the compound.')
		controls_1 = Text(50,560, 'Use the mouse to aim your weapon and press the left mouse button to fire.')
		controls_2 = Text(50,580, 'If you are detected by the guards, the mission will be aborted. ')
		controls_3 = Text(50,600, 'Good luck, agent.')
		controls.draw(SCREEN)
		controls_1.draw(SCREEN)
		controls_2.draw(SCREEN)
		controls_3.draw(SCREEN)
		start_game = Buttons(700,650, 'Start game')
		start_game.draw(SCREEN)
		
		x,y = pg.mouse.get_pos()
		if start_game.rect.collidepoint(x,y):
			if click:
				BGM.stop()
				game()

		for event in pg.event.get():
			if event.type == pg.QUIT:
				run = False
				pg.quit()
				quit()

			if event.type == pg.MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True
					
		keys = pg.key.get_pressed()
		if keys[pg.K_ESCAPE]:
			run = False

		pg.display.update()
		clock.tick(60)

'''end game screen'''
def end_game():
	COMPLETE.play(-1)
	global click
	click = False
	pg.mouse.set_visible(1)
	run = True
	while run:
		SCREEN.fill((0,0,0))
		SCREEN.blit(menu_img_2, (0,0))
		completed = Title(422,300,'Mission complete')
		completed.draw(SCREEN)

		quit_game = Buttons(422,400, 'Main menu')
		quit_game.draw(SCREEN)

		x,y = pg.mouse.get_pos()
		if quit_game.rect.collidepoint(x,y):
			if click:
				#rerun the code, please make sure that there is no whitespace in your directory. 
				#Eg. My PC, this will not work
				os.execv(sys.executable, ['python'] + sys.argv)

		for event in pg.event.get():
			if event.type == pg.QUIT:
				run = False
				pg.quit()
				quit()

			if event.type == pg.MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True

		pg.display.update()
		clock.tick(60)

'''mission fail screen'''
def failed():
	MISSION_FAIL.play()
	FAIL.play(-1)
	global click
	click = False
	pg.mouse.set_visible(1)
	run = True
	while run:
		SCREEN.fill((0,0,0))
		SCREEN.blit(menu_img_2, (0,0))
		completed = Title(422,300,'Mission fail')
		completed.draw(SCREEN)

		quit_game = Buttons(422,400, 'Main menu')
		quit_game.draw(SCREEN)

		x,y = pg.mouse.get_pos()
		if quit_game.rect.collidepoint(x,y):
			if click:
				#rerun the code, please make sure that there is no whitespace in your directory. 
				#Eg. My PC, this will not work
				os.execv(sys.executable, ['python'] + sys.argv)

		for event in pg.event.get():
			if event.type == pg.QUIT:
				run = False
				pg.quit()
				quit()

			if event.type == pg.MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True

		pg.display.update()
		clock.tick(60)

'''Main game'''
def game():
	global DEFAULT_SPEED,PLAYER_RUN,WALKCOUNT,SCREEN_WIDTH,SCREEN_HEIGHT,time_passed_rooms,time_passed_aisle_x,time_passed_aisle_y,START_ROOMS,START_X,START_Y,FLIP,FLIP_X,FLIP_Y,OBJ_COLLECTED,OBJ_DESTROYED,OBJ_COUNT,RAND_MISSION
	INGAME.play(-1)
	run = True
	while run:
		remove_cursor()
		#draw wall from wall_list
		for wall_class in wall_list:
			wall_class.draw(SCREEN)
		draw_bg()

		#Retrieve mouse x and y position
		x, y = pg.mouse.get_pos()

		for event in pg.event.get():
			if event.type == pg.QUIT:
				run = False
				pg.quit()
				quit()

			#add bullet to list when left click is pressed
			if event.type == pg.MOUSEBUTTONDOWN:
				if event.button == 1:
					bullet.append(create_bullet(player.x_pos, player.y_pos, x, y))
					SHOOT_SOUND.play()

		#movement keys
		keys = pg.key.get_pressed()
		'''if keys[pg.K_ESCAPE]:
			run = False'''
		if keys[pg.K_w]:
			player.y_pos -= DEFAULT_SPEED
			player.rect.move_ip(0,-DEFAULT_SPEED)
			moving_animation.pos_y -= DEFAULT_SPEED
			moving_animation.rect.move_ip(0,-DEFAULT_SPEED)
			PLAYER_RUN = True

			#add boundary
			for wall_class in wall_list:
				if wall_class.rect.collidepoint(player.x_pos, player.y_pos):
					player.y_pos += DEFAULT_SPEED
					player.rect.move_ip(0,DEFAULT_SPEED)
					moving_animation.pos_y += DEFAULT_SPEED
					moving_animation.rect.move_ip(0,DEFAULT_SPEED)

		elif keys[pg.K_a]:
			player.x_pos -= DEFAULT_SPEED
			player.rect.move_ip(-DEFAULT_SPEED,0)
			moving_animation.pos_x -= DEFAULT_SPEED 
			moving_animation.rect.move_ip(-DEFAULT_SPEED,0)           
			PLAYER_RUN = True

			#add boundary
			for wall_class in wall_list:
				if wall_class.rect.collidepoint(player.x_pos, player.y_pos):
					player.x_pos += DEFAULT_SPEED
					player.rect.move_ip(DEFAULT_SPEED,0)
					moving_animation.pos_x += DEFAULT_SPEED
					moving_animation.rect.move_ip(DEFAULT_SPEED,0)

		elif keys[pg.K_s]:
			player.y_pos += DEFAULT_SPEED
			player.rect.move_ip(0,DEFAULT_SPEED)
			moving_animation.pos_y += DEFAULT_SPEED
			moving_animation.rect.move_ip(0,DEFAULT_SPEED)
			PLAYER_RUN = True

			#add boundary
			for wall_class in wall_list:
				if wall_class.rect.collidepoint(player.x_pos, player.y_pos):
					player.y_pos -= DEFAULT_SPEED
					player.rect.move_ip(0,-DEFAULT_SPEED)
					moving_animation.pos_y -= DEFAULT_SPEED
					moving_animation.rect.move_ip(0,-DEFAULT_SPEED)

		elif keys[pg.K_d]:
			player.x_pos += DEFAULT_SPEED
			player.rect.move_ip(DEFAULT_SPEED,0)
			moving_animation.pos_x += DEFAULT_SPEED
			moving_animation.rect.move_ip(DEFAULT_SPEED,0)
			PLAYER_RUN = True

			#add boundary
			for wall_class in wall_list:
				if wall_class.rect.collidepoint(player.x_pos, player.y_pos):
					player.x_pos -= DEFAULT_SPEED
					player.rect.move_ip(-DEFAULT_SPEED,0)
					moving_animation.pos_x -= DEFAULT_SPEED
					moving_animation.rect.move_ip(-DEFAULT_SPEED,0)

		else:
			PLAYER_RUN = False
			WALKCOUNT = 0

		'''add map boundary'''
		if player.x_pos <= 15:
			player.x_pos = 15
			player.rect.x = 15
			moving_animation.pos_x = 15
			moving_animation.rect.x = 15
		elif player.x_pos >= SCREEN_WIDTH - 15:
			player.x_pos = SCREEN_WIDTH - 15
			player.rect.x = SCREEN_WIDTH - 15
			moving_animation.pos_x = SCREEN_WIDTH - 15
			moving_animation.rect.x = SCREEN_WIDTH - 15

		if player.y_pos <= 15:
			player.y_pos = 15
			player.rect.y = 15
			moving_animation.pos_y = 15
			moving_animation.rect.y = 15
		elif player.y_pos >= SCREEN_HEIGHT - 15:
			player.y_pos = SCREEN_HEIGHT - 15
			player.rect.y = SCREEN_HEIGHT - 15
			moving_animation.pos_y = SCREEN_HEIGHT - 15
			moving_animation.rect.y = SCREEN_HEIGHT - 15
			
		#player shoots bullet
		for bullets in bullet: 
			if bullets.bullet_time <= 0:
				bullet.pop(bullet.index(bullets))
			bullets.draw(SCREEN)

		#remove bullet if collided with wall
		for wall_class in wall_list:
			for bullets in bullet:
				if wall_class.rect.collidepoint(bullets.x_pos, bullets.y_pos):
					bullet.remove(bullets)

		'''remove enemy if hit'''
		#respawn enemies if enemy count is <= 0
		if len(aisle_x) <= 0 and len(los_enemy_aisle_x) <= 0:
			START_X = True
			if START_X and FLIP_X:
				start_timer_x = pg.time.get_ticks()
				#print('start time: ', start_timer_x)
				FLIP_X = False
			#respawn timer = 10s
			if time_passed_aisle_x >= 10000:
				for enemy, los in zip(temp_aisle_x, temp_los_aisle_x):
					enemy.health = 100
					aisle_x.append(enemy)
					los_enemy_aisle_x.append(los)

					if len(aisle_x) == 1 and len(los_enemy_aisle_x) == 1:
						temp_aisle_x.clear()
						temp_los_aisle_x.clear()

				START_X = False
				FLIP_X = True
				time_passed_aisle_x = 0

		#spawn enemies on x axis aisles
		for enemies, los in zip(aisle_x, los_enemy_aisle_x):
			#print("enemy aisle x: ", aisle_x.index(enemies))
			#print("enemy x and y: ", enemies.x_pos, enemies.y_pos)
			#print("enemy rect x and rect y: ", enemies.rect.x, enemies.rect.y)
			#print("enemy health: ", enemies.health)
			for bullets in bullet:
				if enemies.rect.collidepoint(bullets.x_pos, bullets.y_pos):
					HIT.play()
					bullet.remove(bullets)
					enemies.health -= 50

					if enemies.health <= 0:
						temp_aisle_x.append(enemies)
						temp_los_aisle_x.append(los)
						aisle_x.remove(enemies)
						los_enemy_aisle_x.remove(los)

		#countdown timer on x axis aisle
		if START_X:
			time_passed_aisle_x = pg.time.get_ticks() - start_timer_x

		#respawn enemy if enemy in aisle y is less than or = 0
		if len(aisle_y) <= 0 and len(los_enemy_aisle_y) <= 0:
			START_Y = True
			if START_Y and FLIP_Y:
				start_timer_y = pg.time.get_ticks()
				#print('start time: ', start_timer_y)
				FLIP_Y = False
			#respawn timer = 5s
			if time_passed_aisle_y >= 5000:
				for enemy, los in zip(temp_aisle_y, temp_los_aisle_y):
					enemy.health = 100
					aisle_y.append(enemy)
					los_enemy_aisle_y.append(los)

					if len(aisle_y) == 2 and len(los_enemy_aisle_y) == 2:
						temp_aisle_y.clear()
						temp_los_aisle_y.clear()

				START_Y = False
				FLIP_Y = True
				time_passed_aisle_y = 0

		#print all enemies in y axis aisle
		for enemies, los in zip(aisle_y, los_enemy_aisle_y):
			#print("enemy aisle y: ", aisle_y.index(enemies))
			#print("enemy x and y: ", enemies.x_pos, enemies.y_pos)
			#print("enemy rect x and rect y: ", enemies.rect.x, enemies.rect.y)
			#print("enemy health: ", enemies.health)
			for bullets in bullet:
				if enemies.rect.collidepoint(bullets.x_pos, bullets.y_pos):
					HIT.play()
					bullet.remove(bullets)
					enemies.health -= 50

					if enemies.health <= 0:
						temp_aisle_y.append(enemies)
						temp_los_aisle_y.append(los)
						aisle_y.remove(enemies)
						los_enemy_aisle_y.remove(los)

		#countdown timer for aisle y
		if START_Y:
			time_passed_aisle_y = pg.time.get_ticks() - start_timer_y

		#if enemy less than or = 1, enemy starts respawn
		if len(rooms) <= 1 and len(los_enemy_rooms) <= 1:
			START_ROOMS = True
			if START_ROOMS and FLIP:
				start_timer_rooms = pg.time.get_ticks()
				#print('start time: ', start_timer_rooms)
				FLIP = False
			#respawn timer = 5s
			if time_passed_rooms >= 5000:
				for enemy, los in zip(temp_room, temp_los_room):
					enemy.health = 100
					rooms.append(enemy)
					los_enemy_rooms.append(los)
					#print('enemy added: ', rooms.index(enemy))
					if len(rooms) == 5 and len(los_enemy_rooms) == 5:
						temp_room.clear()
						temp_los_room.clear()

				START_ROOMS = False
				FLIP = True
				time_passed_rooms = 0

		#print all enemies in room
		for enemies, los in zip(rooms, los_enemy_rooms):
			#print("enemy room: ", rooms.index(enemies))
			#print("enemy x and y: ", enemies.x_pos, enemies.y_pos)
			#print("enemy rect x and rect y: ", enemies.rect.x, enemies.rect.y)
			#print("enemy health: ", enemies.health)
			#print('enemy in temp room: ', len(temp_room))
			for bullets in bullet:
				if enemies.rect.collidepoint(bullets.x_pos, bullets.y_pos):
					HIT.play()
					bullet.remove(bullets)
					enemies.health -= 50
					#print("enemy shot")
					#print("enemy health: ", enemies.health)

					if enemies.health <= 0:
						temp_room.append(enemies)
						temp_los_room.append(los)
						#print('enemies in temp room: ', len(temp_room))
						#print('enemy removed: ', rooms.index(enemies))
						rooms.remove(enemies)
						los_enemy_rooms.remove(los)
						#print('enemy left: ', len(rooms))
		#start countdown
		if START_ROOMS:
			time_passed_rooms = pg.time.get_ticks() - start_timer_rooms

		#check if player is in enemy los
		for los in los_enemy_aisle_x:
			if los.rect.collidepoint(player.x_pos, player.y_pos):
				INGAME.stop()
				failed()
				break
			if los.rect_left.collidepoint(player.x_pos, player.y_pos):
				INGAME.stop()
				failed()
				break

		for los in los_enemy_aisle_y:
			if los.rect_down.collidepoint(player.x_pos, player.y_pos):
				INGAME.stop()
				failed()
				break
			if los.rect_top.collidepoint(player.x_pos, player.y_pos):
				INGAME.stop()
				failed()
				break

		for los in los_enemy_rooms:
			if los.rect_room.collidepoint(player.x_pos, player.y_pos):
				INGAME.stop()
				failed()
				break
			if los.rect_room_down.collidepoint(player.x_pos, player.y_pos):
				INGAME.stop()
				failed()
				break
			if los.rect_room_left.collidepoint(player.x_pos, player.y_pos):
				INGAME.stop()
				failed()
				break
			if los.rect_room_top.collidepoint(player.x_pos, player.y_pos):
				INGAME.stop()
				failed()
				break

		#player captures objective
		if RAND_MISSION:
			#print('collect the objectives')
			for obj in objective_list:
				if player.rect.colliderect(obj.rect):
					COLLECT.play()
					objective_list.remove(obj)
					OBJ_COLLECTED += 1
					#print('objective collected %d/5' % OBJ_COLLECTED)
		else:
			#print('destroy the objectives')
			for obj in objective_list:
				for bullets in bullet:
					if obj.rect.collidepoint(bullets.x_pos, bullets.y_pos):
						DESTROY.play()
						objective_list.remove(obj)
						OBJ_DESTROYED += 1
						#print('objective destroyed %d/5' % OBJ_DESTROYED)

		if OBJ_DESTROYED == 5 or OBJ_COLLECTED == 5:
			INGAME.stop()
			end_game()
			break

		#print("room: ", time_passed_rooms/1000)
		#print("x: ", time_passed_aisle_x/1000)
		#print("y: ", time_passed_aisle_y/1000)

		'''draw objective counter'''
		font = pg.font.Font('DS-DIGI.ttf',50)
		if RAND_MISSION:
			objective_counts = f'{OBJ_COLLECTED}/{OBJ_COUNT}'
		else:
			objective_counts = f'{OBJ_DESTROYED}/{OBJ_COUNT}'
		text = font.render(objective_counts, True, (255,255,255))
		SCREEN.blit(text, (760,640))

		#draw_count()
		draw_obj()
		draw_los()
		draw_enemy()
		draw_crosshair()
		draw_player()
		#print('enemies left on map: ', len(aisle_x) + len(aisle_y) + len(rooms))

		#print("mouse x: ", x)
		#print("mouse y: ", y)

		#print("player x and y: ", player.x_pos, player.y_pos)
		#print("player rect x and y: ", player.rect.x, player.rect.y)
		#print("leg x and y: ", moving_animation.pos_x, moving_animation.pos_y)
		#print("leg rect x and y: ", moving_animation.rect.x, moving_animation.rect.y)

		pg.display.update()
		clock.tick(60)

main_menu()
#game()
#end_game()