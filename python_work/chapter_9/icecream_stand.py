from restaurant import Restaurant

class IceCreamStand(Restaurant): 
	def __init__(self, name, flavours=["strawberry"]):
		super().__init__(name, "icecream")
		self.icecream_flavours = flavours

	def getFlavours(self):
		return self.icecream_flavours