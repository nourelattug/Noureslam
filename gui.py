import tkinter as tk
from player import Player
from key import Key
from healingpad import HealingPad
from enemy import Enemy
from Treasure import Treasure
from weapon import Weapon

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
