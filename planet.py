
class Planet:
    def __init__(self,name: str, radius: float, mass: float, temp: float,age:int,moons: int):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.temp = temp
        self.age = age
        self.moons = moons
    
MARS = Planet("Mars",3389500,6.417 * (10 ** 23),-153,4_000_000_000,2)

