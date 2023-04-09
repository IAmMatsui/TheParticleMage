import pygame

from player import Player

# For now the Scene manager will work as a scene itself, but it will change soon
class SceneManager:
	def __init__(self):
		self.setup()


	# Will be removed soon
	def setup(self):
		self.display = pygame.display.get_surface()
		self.sprites = pygame.sprite.Group()
		self.player = Player((100,200),self.sprites)

	def run(self,dt):
		self.update(dt)
		self.draw()

	def update(self,dt):
		self.sprites.update(dt)

	def draw(self):
		self.display.fill("black")
		self.sprites.draw(self.display)

