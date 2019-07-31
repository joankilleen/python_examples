class Restaurant:
	"""Restaurant class"""
	def __init__(self, name, cuisine_type):
		self.name= name
		self.cuisine_type = cuisine_type
	def describe(self):
		print(f"{self.name} serves {self.cuisine_type}")
	def open(self):
		print(f"{self.name} is now open")