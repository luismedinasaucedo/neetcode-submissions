class SuperHero:
    def __init__(self, name: str, power: str, health: int):
        self.name=name
        self.power=power
        self.health=health


Batman=SuperHero("Batman", "Intelligence", 100)
Superman = SuperHero("Superman", "Strength", 150)

# TODO: Print out the attributes of each superhero
print(Batman.name)
print(Batman.power)
print(Batman.health)
print(Superman.name)
print(Superman.power)
print(Superman.health)
