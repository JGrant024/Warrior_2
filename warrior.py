# Choose your own adventure
# Warrior Part 2
# Continuing from the work done in part 1 , update your code to reflect the changes to each class as noted below.

# NOTE: Doing this work on a new branch and/or new file is recommended!

# Update Characters
# Hero
# Make the hero generate double damage points during an attack with a probabilty of 20%
# Add a coins attribute to the Character class. Have it default to a value of 20.
# Add a buy method to the Hero class so that hero objects can purchase items from a virtual store (see below).
# Give the method an item parameter. The item being purchased will be passed as an argument into the method.
# It should subtract an items cost from the hero object's available coins
# Enemies
# Make a character called Shadow who has only 1 starting health but will only take damage about once out of every ten times he is attacked.
# Make a Zombie character that doesn't die even if their health is below zero.
# Give each enemy a bounty. For example, the prize for defeating the Goblin is 5 coins, for the Shadow it is 6 coins.
# Misc
# Come up with at least two other characters with their individual characteristics, and implement them (i.e. Wizard, Archer, Scribe)
# Go Shopping
# The Store
# Make a Store class to make a virtual "shop" within the game where characters can purchase items.
# Add an list called Items, this will be a class variable. Have it store two items: Tonic and Sword (see below)
# Add a do_shopping method to the Store class.
# Have it display a welcome message and the player's current coin balance.
# List all available items with their names and costs.
# The Hero class has a buy method that will allow a hero object to purchse an item. The cost of the item will be subtracted from the hero object's available coins.
# Store Items
# All items have a cost attribute that represents the number of coins the hero will spend.
# All items have a method called apply that allows them to be used.
# Make a Tonic class that is available via the the Items class variable on the store object.
# The tonic's apply method adds 2 to the hero's health
# Add a Sword class that is available via the the Items class variable on the store object.
# The sword's apply mehtod will add 2 to the hero's power.
# Level 9000
# Create a Battle class with a do_battle method. Move the game logic into that class. (i.e. asking the user what they want to do, and acting accordingly)
# Allow items to be used on the battle field. The hero can carry the items with them, and you have the option of choosing to use a tonic at any turn in a battle.
# Make a swap_power method and add it to a character (or the Character class). This method can be used on the battle field to swap the power values of the two characters for one turn.
# There is a bug in the store that allows the hero to buy items even if he has no coins. Fix this bug.
# To quote Fleetwood Mac: You can go your own way!
# Using the Warrior RPG as a guide, create a brand new RPG game.

# Here are some possible ideas based on previous students' work:

# Murder mystery (ala the game/movie "Clue", or tv show "How to Get Away with Murder")
# Race across the country (ala "Twisted Metal," "Death Race 2000," "Cannonball Run")
# Sports! (literally, football, basketball, baseball, golf)
# Level 10K - PyGame
# In the past I've had students use the PyGame framework to generate their own "platformer" games (think old school video games).

# Here are a couple links to tutorials that students have found helpful:

# Kids Can Code: PyGame
# PyGame Tutorials (Official Docs)
# YouTube: PyGame in 10 minutes
# Examples
# The Keating Four: RPG Murder Mystery
# MoonSet: PyGame