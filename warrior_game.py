import random

class Character:
    def __init__(self, health, power, name, coins=20):
        self.health = health
        self.power = power
        self.name = name
        self.coins = coins


    def alive(self): 
        return self.health > 1
    
    def attack(self, enemy):   
        damage = random.randint(1, self.power)
        enemy.health -= damage 
        # created to double damage points 
        if random.random() < 0.2:
            damage *= 2
            print("Double Damage!") 
        enemy.health = max(0, enemy.health - damage)
    
    def print_status(self, enemy):
        print(f"{self.name}: {self.health} | {enemy.name}: {enemy.health} | Coins: {self.coins}")

    def buy(self, item,): 
        if self.coins >= item.cost: 
            self.coins -= item.cost
            item.apply_item(self)
            print(f"{self.name} has purchased {item.name} for {item.cost} coins!")
        else: 
            print(f"Oops! {self.name} does not have enough for {self.Item}")
         
        


class Hero(Character): 
    def buy(self, item):
        #The super() function is used to give access to methods and properties of a parent or sibling class.
        return super().buy(item)

class Enemy(Character): 
    def __init__(self, health, power, name, bounty):
        super().__init__(self, health, power, name)
        self.bounty = bounty 

#created a class for the charater with default value for health, power, and bounty. 
class Shadow(Enemy):  
        def __init__(self): 
            super().__init__(health=1, power=1, name="Shadow", bounty=6)

    # This allows the hero to take damage once out of every ten times hit. 
        def attack(self, hero): 
            if random.randint(1, 10) == 1:
                print(f"{self.name} is quicker than that! You almost had it!")
            else: 
                super().attack(hero)

     

#Make a Zombie character that doesn't die even if their health is below zero.
class Zombie(Enemy): 
    def __init__(self): 
        super().__init__(health =5, power =2, name="Zombie", bounty=8  )
    # This method makes sure that the zombie stays alive 
    def alive(self): 
        return True 
    
class Wizard(Enemy): 
    def __init__(self): 
       super().__init__(health = 8, power= 4, name= "Wizard", bounty= 10) 


class Archer(Enemy): 
    def __init__(self): 
       super().__init__(health = 6, power= 3, name= "Archer", bounty= 7) 


# Make a Store class to make a virtual "shop" within the game where characters can purchase items.
# Add an list called Items, this will be a class variable. Have it store two items: Tonic and Sword         
class Store(): 
    Items =[
        {"name": "Tonic", "cost": 5, "class": "Tonic"},
        {"name": "Sword", "cost": 7, "class": "Sword"}
    ]

    def go_shopping(self, hero): 
        




        ascii_art = """


 ____      ____                        _                           ___             _   __         _    _   
|_  _|    |_  _|                      (_)                        .'   `.          / |_[  |       / |_ | |  
  \ \  /\  / / .--.   _ .--.  _ .--.  __   .--.   _ .--.        /  .-.  \ __   _ `| |-'| | .---.`| |-'| |  
   \ \/  \/ // .'`\ \[ `/'`\][ `/'`\][  |/ .'`\ \[ `/'`\]       | |   | |[  | | | | |  | |/ /__\\| |  | |  
    \  /\  / | \__. | | |     | |     | || \__. | | |           \  `-'  / | \_/ |,| |, | || \__.,| |, |_|  
     \/  \/   '.__.' [___]   [___]   [___]'.__.' [___]           `.___.'  '.__.'_/\__/[___]'.__.'\__/ (_)  
                                                                                                           

 """
        print(ascii_art)
        print(f"Welcome to Warrior Outlets! Bank Balance: {hero.coins}")
        print("Check out our avaliable items:!")
        #for loop for items taken from inventory
        for items in self.Items: 
            print(f"{items['name']} - {items['cost']} coins.")

        selection = input("Enter the name of your selected item, or type 'exit' to leave:  ")
        
        if selection.lower() == 'exit': 
            print("Thanks!! Come back soon!")
        else: 
            item = next((i for i in self.Items if i['name'].lower() == selection.lower()), None)
            if item: 
                hero.buy(globals()[item["class"]](name = item["name"], cost = item["cost"]))
                self.go_shopping(hero)
            else: 
                print("Oops! Pick something valid from the selection!")


#defining the name and cost of the item in its on class 
class Item: 
    def __init__(self, name, cost):
        self.name = name 
        self.cost = cost 
    
    def apply_item(self, character):
        pass

#defining the item Tonic with the default value of tonie and cost of 5 coins.
class Tonic(Item): 
    def __init__(self, name, cost):
        super().__init__(name="Tonic", cost=5)
    
    def apply_item(self, character):
        character.health += 2

class Sword(Item): 
    def __init__(self, name, cost):
        super().__init__(name="Sword", cost=8)
    
    def apply_item(self, character):
        character.power += 2



hero = Hero(name = "Hero", health = 10, power = 5)
shadow = Shadow() 
zombie = Zombie() 
wizard = Wizard()
archer = Archer() 
store = Store()     


ascii_art = """


 _______                        __             _            _______                          __       __         _____    
|_   __ \                      |  ]           / |_         |_   __ \                        [  |     [  |       / ___ `.  
  | |__) |  .---.  ,--.    .--.| |   _   __  `| |-' .--.     | |__) |  __   _   _ .--..--.   | |.--.  | | .---.|_/___) |  
  |  __ /  / /__\\`'_\ : / /'`\' |  [ \ [  ]  | | / .'`\ \   |  __ /  [  | | | [ `.-. .-. |  | '/'`\ \| |/ /__\\ /  __.'  
 _| |  \ \_| \__.,// | |,| \__/  |   \ '/ /   | |,| \__. |  _| |  \ \_ | \_/ |, | | | | | |  |  \__/ || || \__., |_|      
|____| |___|'.__.'\'-;__/ '.__.;__][\_:  /    \__/ '.__.'  |____| |___|'.__.'_/[___||__||__][__;.__.'[___]'.__.' (_)      
                                    \__.'                                                                                 

                                                                                                           

"""




while hero.alive():
    print(ascii_art)
    print("Choose one of the following options or get ready for a rumble!")
    print("1. Shadow")
    print("2. Zombie")
    print("3. Wizard")
    print("4. Archer")
    print("5. Go Shopping")
    print("6. Quit")

    user_input = input()

    if user_input == "1":
        enemy = shadow
    elif user_input == "2":
        enemy = zombie
    elif user_input == "3":
        enemy = wizard
    elif user_input == "4":
        enemy = archer
    elif user_input == "5":
        store.go_shopping(hero)
        continue
    elif user_input == "6":
        print("See ya L8r!")
        break
    else:
        print("Opps! Choose valid option!")
        continue

while hero.alive():
    print(ascii_art)
    print("Choose one of the following options or get ready for a rumble!")
    print("1. Shadow")
    print("2. Zombie")
    print("3. Wizard")
    print("4. Archer")
    print("5. Go Shopping")
    print("6. Quit")

    user_input = input()

    if user_input == "1":
        enemy = shadow
    elif user_input == "2":
        enemy = zombie
    elif user_input == "3":
        enemy = wizard
    elif user_input == "4":
        enemy = archer
    elif user_input == "5":
        Store.go_shopping(hero)
        continue
    elif user_input == "6":
        print("See ya L8r!")
        break
    else:
        print("Opps! Choose valid option!")
        continue

    while enemy.alive() and hero.alive():
        print("What do you want to do?")
        print("1. Rumble")
        print("2. Do nothing")
        print("3. Get out there!")
        user_input = input()

        if user_input == "1":
            hero.attack(enemy)
            enemy.attack(hero)
            hero.print_status(enemy)

            if not enemy.alive():
                print(f"You taught {enemy.name} a lesson, and earned {enemy.bounty} coins!")
                hero.coins += enemy.bounty
                break

        elif user_input == "2":
            enemy.attack(hero)
            hero.print_status(enemy)

        elif user_input == "3":
            print("The Battle was too much! You left!")
            break

        else:
            print("Opps! Choose a valid option!")

        if not hero.alive():
            print("You have been unalived. Try again? ")
            break
