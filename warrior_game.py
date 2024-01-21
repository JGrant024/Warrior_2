import random

class Character:
    def __init__(self, health, power, name, coins=20):
        self.health = health
        self.power = power
        self.name = name
        self.coins = coins


    def alive(self): 
        return self.health > 0
    
    def attack(self, enemy):   
        damage = random.randint(1, self.power)
        enemy.health -= damage 
        # created to double damage points 
        if random.random() < 0.2:
            damage *= 2
            print("Double Damage!") 
        enemy.health -= damage
    
    def print_status(self, enemy):
        print(f"{self.name}: {self.health} | {enemy.name}: {enemy.health} | Coins: {self.coins}")

    def buy(self, item): 
        if self.coins >= item.cost: 
            self.coins -= item.cost
            item.apply(self)
            print(f"{self.name} has purchased {item.name} for {item.cost} coins!")
        else: 
            print(f"Oops! {self.name} does not have enough for {self.Item}")
         
        


class Hero(Character): 
    def buy(self, item):
        #The super() function is used to give access to methods and properties of a parent or sibling class.
        return super().buy(item)

class Enemy(): 
    def __init__(self, health, power, name, bounty):
        super().__init__(self, health, power, name)
        self.bounty = bounty 

#created a class for the charater with default value for health, power, and bounty. 
class Shadow(): 
    def __init__(self): 
        super().__init__(health =1, power = 1, name ="Shadow", bounty = 6)

    # This allow the hero to take damage once out of every ten times hit. 
    def attack(self, hero): 
        if random.randint(1, 10) == 1:
            print(f"{self.name} is quicker than that! You almost had it!")
        else: 
            super().attack(hero)

#Make a Zombie character that doesn't die even if their health is below zero.
class Zombie(): 
    def __init__(self): 
        super().__init__(health =5, power =2, name="Zombie", bounty=8  )

    def alive(): 
        return True 
    

        





    
