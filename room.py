class Room:
    def __init__(self, description, enemy=None, points=0, weapon=None, money=0, treasure=None, healing_pad=None, key=None):
        self.description = description
        self.enemy = enemy
        self.points = points
        self.weapon = weapon
        self.money = money
        self.treasure = treasure
        self.healing_pad = healing_pad
        self.key = key
    
    def __str__(self):
        room_info = f"Description: {self.description}\n"
        
        if self.enemy is not None:
            room_info += f"Enemy: {self.enemy.name} (Damage: {self.enemy.damage}, Health: {self.enemy.health})\n"
        
        room_info += f"Points: {self.points}\n"
        
        if self.weapon is not None:
            room_info += f"Weapon: {self.weapon.name} (Damage: {self.weapon.damage}, Price: {self.weapon.price})\n"
        
        room_info += f"Money: {self.money}\n"
        
        if self.treasure is not None:
            room_info += f"Treasure: Code: {self.treasure.code}, Point: {self.treasure.point}\n"
        
        if self.healing_pad is not None:
            room_info += f"Healing Pad: {self.healing_pad}\n"
        
        if self.key is not None:
            room_info += f"Key: Code: {self.key.code}, Price {self.key.price}\n"
        
        return room_info

