from player import Player
from key import Key
from healingpad import HealingPad
from enemy import Enemy
from treasure import Treasure
from weapon import Weapon


class Key:
    def __init__(self, code, price):
        self.code = code
        self.price = price
