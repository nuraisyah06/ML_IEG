import random
'''class Weapons(Pokemon):
    
    def __init__(self, name, power, weapons):
        super().__init__(name, power)
        self.weapons = weapons'''


class Pokemon:
    
    def __init__(self, name, power, element):
        self.name = name
        self.power = power
        self.element = element

    def doMove(self):
        print("Pokemon Move")
        
    def Herbivor(self):
        print("Pokemon eat green only")

class Jigglypuff(Pokemon):
    
    def __init__(self, name, power, element, lungcapacity):
        super().__init__(name, power, element)
        self.lungcapacity = lungcapacity
        
    def doMove(self):
        super().doMove()
        print("Jigglypuff can float")
        
    def __str__(self):
        return f"Name: {self.name}\nPower: {self.power}\nElement: {self.element}\nLung Capacity: {self.lungcapacity}"
        
class Pikachu(Pokemon):
    
    def __init__(self, name, power, element, electricity):
        super().__init__(name, power, element)
        self.electricity = electricity
        
'''pokemon = Jigglypuff("J1", 75, "fairy", 92)
pokemon.doMove'''

class Game:
    
    def __init__(self):
        self.power = ["Thunder", "Fire", "Water", "Ghost", "Ice"]
        self.pokemons = {
            "Jigglypuff": [Jigglypuff(f"J{i}", random.randint(50, 100), self.power[random.randint(0, len(self.power) - 1)], random.randint(50, 100)) for i in range(0, random.randint(3, 15))],
            "Pikachu": [Pikachu(f"P{i}", random.randint(50, 100), self.power[random.randint(0, len(self.power) - 1)], random.randint(50, 100)) for i in range(0, random.randint(5, 20))]
        }
        
    def __str__(self):
        message = " "
        for pokemonname, pokemonlist in self.pokemons.items():
            for pokemon in self.pokemons:
                message = message + pokemon.__str__() +"\n" + ("-" * 20) + "\n"
        return message
        
game = Game()
print(game)