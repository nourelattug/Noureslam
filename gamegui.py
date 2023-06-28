# import tkinter as tk

# class GameGUI:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("Game Title")
        
#         # Player Information Labels
#         self.player_name_label = tk.Label(self.root, text="Player Name:")
#         self.player_name_label.pack()
        
#         self.money_label = tk.Label(self.root, text="Money:")
#         self.money_label.pack()
        
#         self.health_label = tk.Label(self.root, text="Health:")
#         self.health_label.pack()
        
#         self.points_label = tk.Label(self.root, text="Points:")
#         self.points_label.pack()
        
#         # Room Description Label
#         self.room_description_label = tk.Label(self.root, text="Room Description:")
#         self.room_description_label.pack()
        
#         # Enemy Information Labels
#         self.enemy_name_label = tk.Label(self.root, text="Enemy Name:")
#         self.enemy_name_label.pack()
        
#         self.enemy_damage_label = tk.Label(self.root, text="Enemy Damage:")
#         self.enemy_damage_label.pack()
        
#         self.enemy_health_label = tk.Label(self.root, text="Enemy Health:")
#         self.enemy_health_label.pack()
        
#         # Inventory Button
#         self.inventory_button = tk.Button(self.root, text="View Inventory", command=self.open_inventory)
#         self.inventory_button.pack()
        
#         # Room Buttons
#         self.room1_button = tk.Button(self.root, text="Enter Room 1", command=self.enter_room1)
#         self.room1_button.pack()
        
#         self.room2_button = tk.Button(self.root, text="Enter Room 2", command=self.enter_room2)
#         self.room2_button.pack()
        
#         self.room3_button = tk.Button(self.root, text="Enter Room 3", command=self.enter_room3)
#         self.room3_button.pack()
        
#         self.room4_button = tk.Button(self.root, text="Enter Room 4", command=self.enter_room4)
#         self.room4_button.pack()
        
#         # Shop Button
#         self.shop_button = tk.Button(self.root, text="Visit Shop", command=self.visit_shop)
#         self.shop_button.pack()
        
#     def open_inventory(self):
#         # Implement the logic to open the inventory window
#         pass
    
#     def enter_room1(self):
#         # Implement the logic for entering Room 1
#         pass
    
#     def enter_room2(self):
#         # Implement the logic for entering Room 2
#         pass
    
#     def enter_room3(self):
#         # Implement the logic for entering Room 3
#         pass
    
#     def enter_room4(self):
#         # Implement the logic for entering Room 4
#         pass
    
#     def visit_shop(self):
#         # Implement the logic for visiting the shop
#         pass
    
#     def run(self):
#         self.root.mainloop()

# # Create an instance of the GameGUI class and run the GUI
# game_gui = GameGUI()
# game_gui.run()

import tkinter as tk
from player import Player
from key import Key
from healingpad import HealingPad
from enemy import Enemy
from Treasure import Treasure
from weapon import Weapon
from armor import Armor


class GameGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Game Title")
        
        self.player = None
        self.enemy = None
        self.weapon = None
        self.key = None
        self.healing_pad = None
        
        # ... Rest of the GUI code ...
        
    def open_inventory(self):
        # Check if player instance exists
        if self.player is not None:
            # Implement the logic to open the inventory window
            # Access player's inventory through self.player.inventory
            pass
    
    def enter_room1(self):
        # Check if player and enemy instances exist
        if self.player is not None and self.enemy is not None:
            # Create instances of weapon, key, healing pad
            self.weapon = Weapon("Sword", 10, 20)
            self.key = Key(1, 50)
            self.healing_pad = HealingPad(30, 50)
            
            # Implement the logic for entering Room 1
            # Access player instance through self.player
            # Access enemy instance through self.enemy
            pass
    
    def enter_room2(self):
        # Check if player and enemy instances exist
        if self.player is not None and self.enemy is not None:
            # Create instances of weapon, key, healing pad
            self.weapon = Weapon("Axe", 15, 30)
            self.key = Key(0, 40)
            self.healing_pad = HealingPad(25, 50)
            
            # Implement the logic for entering Room 2
            # Access player instance through self.player
            # Access enemy instance through self.enemy
            pass
    
    def enter_room3(self):
        # Check if player and enemy instances exist
        if self.player is not None and self.enemy is not None:
            # Create instances of weapon, key, healing pad
            self.weapon = Weapon("Bow", 12, 25)
            self.key = Key(1, 60)
            self.healing_pad = HealingPad(20, 50)
            
            # Implement the logic for entering Room 3
            # Access player instance through self.player
            # Access enemy instance through self.enemy
            pass
    
    def enter_room4(self):
        # Check if player and enemy instances exist
        if self.player is not None and self.enemy is not None:
            # Create instances of weapon, key, healing pad
            self.weapon = Weapon("Dagger", 8, 15)
            self.key = Key(0, 30)
            self.healing_pad = HealingPad(15, 50)
            
            # Implement the logic for entering Room 4
            # Access player instance through self.player
            # Access enemy instance through self.enemy
            pass
    
    # ... Implement visit_shop method and other GUI elements ...
    
    def run(self):
        self.root.mainloop()

# Create an instance of the GameGUI class and run the GUI
game_gui = GameGUI()
game_gui.run()

