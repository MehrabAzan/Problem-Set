class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

    def set_catchphrase(self, new_catchphrase):
        if len(new_catchphrase) > 20:
            print("Invalid catchphrase")
        for c in new_catchphrase:
            if not (c.isalpha() or c.isspace()):
                print("Invalid catchphrase")
                return
        self.catchphrase = new_catchphrase
        print("Catchphrase Updated!")

    def add_item(self, item_name):
        if item_name == "acoustic guitar" or item_name == "ironwood kitchenette" or item_name == "rattan armchair" or item_name == "kotatsu" or item_name == "cacao tree":
            self.furniture.append(item_name)

    def print_inventory(self):
        if len(self.furniture) == 0:
            print("Inventory empty")
            return
        freq = {}
        for item in self.furniture:
            freq[item] = freq.get(item, 0) + 1
        print(freq)

# Instantiate your villager here
apollo = Villager("Apollo", "Eagle", "pah")
bones = Villager("Bones", "Dog", "yip yip")

print(apollo.name)  
print(apollo.species)  
print(apollo.catchphrase) 
print(apollo.furniture)

print("\n")
print(bones.greet_player("Tram"))

bones.catchphrase = "ruff it up"
print("\n")
print(bones.greet_player("Samia"))

alice = Villager("Alice", "Koala", "guvnor")

print("\n")
alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)
alice.set_catchphrase("#?!")
print(alice.catchphrase)

alice = Villager("Alice", "Koala", "guvnor")
print("\n")
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)

alice = Villager("Alice", "Koala", "guvnor")

print("\n")
alice.print_inventory()

alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
alice.print_inventory()