import pygame
from sys import exit as sys_exit
from sceneMNGR import SceneManager

class Game:
	def __init__(self):
		pygame.init()
		pygame.display.set_caption("The Particle Mage")
		self.screen = pygame.display.set_mode((800,800))
		self.clock = pygame.time.Clock()
		self.FPS_limit = 120
		self.SM = SceneManager()

	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys_exit()


			dt = self.clock.tick(self.FPS_limit)/1000
			self.SM.run(dt)
			pygame.display.update()

if __name__ == "__main__":
	game = Game()
	game.run()

