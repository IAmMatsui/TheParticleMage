import pygame
from importlib import import_module, invalidate_caches
from os import listdir

class SceneManager:
	def __init__(self):
		self.SCENES_CLASSES = {}
		self.SCENES = {}
		self.import_scenes()

	def import_scenes(self):
		for file in listdir("./scenes"):
			if file.endswith(".py") and file != "scene.py":
				invalidate_caches()
				scene_name = file.replace(".py","")
				module = import_module(f"scenes.{scene_name}")
				self.SCENES_CLASSES[scene_name] = getattr(module,"Scene")

		for scene_name, scene_class in self.SCENES_CLASSES.items():
			self.SCENES[scene_name] = scene_class(self) 


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

sm = SceneManager()