class Location:
    def __init__(self, desc):
        self.desc = desc
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.pickups = []
    
    def add_pickup(self, item):
        self.pickups.append(item)
        
    def remove_pickup(self, item):
        self.pickups.remove(item)
        return item

dining_room = Location("a fancy dining room.")
kitchen = Location=("a messy kitchen with flour on the counter and dishes in the sink.")
kitchen.add_pickup("flour")
kitchen.add_pickup("dishes")
bedroom = Location=("a bedroom with a watch on the bedside table")
bedroom.add_pickup("watch")
bath = Location=("a small bathroom with a towel on the floor.")
bath.add_pickup("towel")
porch = Location=("a wooden porch with a rocking chair.")

dining_room.north = kitchen
dining_room.south = bedroom
dining_room.east = bath
dining_room.west = porch