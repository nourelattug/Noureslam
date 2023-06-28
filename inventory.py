import tkinter as tk

class InventoryWindow:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("Inventory")
        
        # Weapons
        self.weapon_labels = []
        self.weapon_buttons = []
        
        self.weapon_frame = tk.Frame(self.root)
        self.weapon_frame.pack()
        
        # Add weapons to the inventory
        self.add_weapon("Weapon 1", 10, 50)
        self.add_weapon("Weapon 2", 20, 100)
        # Add more weapons...
        
        # Keys
        self.key_labels = []
        self.key_buttons = []
        
        self.key_frame = tk.Frame(self.root)
        self.key_frame.pack()
        
        # Add keys to the inventory
        self.add_key(0, 200)
        self.add_key(1, 300)
        # Add more keys...
        
        # Armors
        self.armor_labels = []
        self.armor_buttons = []
        
        self.armor_frame = tk.Frame(self.root)
        self.armor_frame.pack()
        
        # Add armors to the inventory
        self.add_armor(1, 200)
        self.add_armor(2, 400)
        # Add more armors...
        
        # Healing Pads
        self.healing_pad_labels = []
        self.healing_pad_buttons = []
        
        self.healing_pad_frame = tk.Frame(self.root)
        self.healing_pad_frame.pack()
        
        # Add healing pads to the inventory
        self.add_healing_pad(100)
        self.add_healing_pad(150)
        # Add more healing pads...
        
        # Close Button
        self.close_button = tk.Button(self.root, text="Close Inventory", command=self.close_inventory)
        self.close_button.pack()
    
    def add_weapon(self, name, damage, price):
        weapon_label = tk.Label(self.weapon_frame, text=name)
        weapon_label.pack(side=tk.LEFT)
        self.weapon_labels.append(weapon_label)
        
        damage_label = tk.Label(self.weapon_frame, text=f"Damage: {damage}")
        damage_label.pack(side=tk.LEFT)
        self.weapon_labels.append(damage_label)
        
        price_label = tk.Label(self.weapon_frame, text=f"Price: {price}")
        price_label.pack(side=tk.LEFT)
        self.weapon_labels.append(price_label)
        
        use_button = tk.Button(self.weapon_frame, text="Use", command=lambda: self.use_weapon(name))
        use_button.pack(side=tk.LEFT)
        self.weapon_buttons.append(use_button)
    
    def add_key(self, code, price):
        key_label = tk.Label(self.key_frame, text=f"Code: {code}")
        key_label.pack(side=tk.LEFT)
        self.key_labels.append(key_label)
        
        price_label = tk.Label(self.key_frame, text=f"Price: {price}")
        price_label.pack(side=tk.LEFT)
        self.key_labels.append(price_label)
        
        use_button = tk.Button(self.key_frame, text="Use", command=lambda: self.use_key(code))
        use_button.pack(side=tk.LEFT)
        self.key_buttons.append(use_button)
    
    def add_armor(self, durability, price):
        armor_label = tk.Label(self.armor_frame, text=f"Durability: {durability}")
        armor_label.pack(side=tk.LEFT)
        self.armor_labels.append(armor_label)
        
        price_label = tk.Label(self.armor_frame, text=f"Price: {price}")
        price_label.pack(side=tk.LEFT)
        self.armor_labels.append(price_label)
        
        use_button = tk.Button(self.armor_frame, text="Use", command=lambda: self.use_armor(durability))
        use_button.pack(side=tk.LEFT)
        self.armor_buttons.append(use_button)
    
    def add_healing_pad(self, price):
        healing_pad_label = tk.Label(self.healing_pad_frame, text=f"Price: {price}")
        healing_pad_label.pack(side=tk.LEFT)
        self.healing_pad_labels.append(healing_pad_label)
        
        use_button = tk.Button(self.healing_pad_frame, text="Use", command=self.use_healing_pad)
        use_button.pack(side=tk.LEFT)
        self.healing_pad_buttons.append(use_button)
    
    def use_weapon(self, name):
        # Implement the logic to use the selected weapon
        pass
    
    def use_key(self, code):
        # Implement the logic to use the selected key
        pass
    
    def use_armor(self, durability):
        # Implement the logic to use the selected armor
        pass
    
    def use_healing_pad(self):
        # Implement the logic to use the healing pad
        pass
    
    def close_inventory(self):
        self.root.destroy()

# Create an instance of the InventoryWindow class
inventory_window = InventoryWindow()
