import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self,pos,group):
		super().__init__(group)

		self.image = pygame.Surface((64,32))
		self.image.fill("red")
		self.rect = self.image.get_rect(center=pos)
		self.speed = 300
		self.direction = pygame.math.Vector2()

	def update(self,dt):
		keys = pygame.key.get_pressed()
		h_spd = keys[pygame.K_d] - keys[pygame.K_a]
		v_spd = keys[pygame.K_s] - keys[pygame.K_w]
		self.direction.update(h_spd,v_spd)

		if self.direction.magnitude()>0:
			self.direction = self.direction.normalize()

		self.rect.center += self.direction * self.speed * dt
