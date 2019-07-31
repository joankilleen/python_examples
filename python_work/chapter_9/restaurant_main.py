from restaurant import Restaurant
from icecream_stand import IceCreamStand

restaurant_nice = Restaurant("Fabulous Food", "Mediteranean")
restaurant_nice.describe()
restaurant_nice.open()

flavours = ["chocolate", "strawberry"]
icecream_rest = IceCreamStand("Best Icecream", flavours)

print(f"{icecream_rest.getFlavours()}")