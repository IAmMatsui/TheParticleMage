class Scene:
	def __init__(self,scene_mngr,reloaded=False):
		self.sm = scene_mngr

		#if true, it will reload every time enter the scene
		self.reloaded = reloaded

	def update(self,dt):
		pass

	def draw(self):
		pass

	def enter(self):
		pass

	def exit(self):
		pass