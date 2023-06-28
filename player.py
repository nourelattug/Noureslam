from player import Player
from key import Key
from healingpad import HealingPad
from enemy import Enemy
from treasure import Treasure
from weapon import Weapon



class Player:
    def __init__(self, name, money, health, points):
        self.name = name
        self.money = money
        self.health = health
        self.points = points
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)
