class Location:
    def __init__(self, desc, north, south, east, west, items):
        self.desc = desc
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.items = []
    
    # def add_pickup(self, item):
    #     self.pickups.append(item)
        
    # def remove_pickup(self, item):
    #     self.pickups.remove(item)
    #     return item

bedroom = Location("a small, comfortable bedroom containing a single bed. An alarm clock glows softly on the bedside table.\nOn the end of the bed is a Towel, and by the mirror, draped over a chair are some work clothes.", None, "hall", None, None,["Alarm Clock", "Towel", "Work Clothes", "Dressing Gown"])



print(bedroom.desc)
print(bedroom.north)
print(bedroom.south)
print(bedroom.east)
print(bedroom.west)
print(bedroom.items)

# kitchen = Location=("a messy kitchen with flour on the counter and dishes in the sink.")
# kitchen.add_pickup("flour")
# kitchen.add_pickup("dishes")
# bedroom = Location=("a bedroom with a watch on the bedside table")
# bedroom.add_pickup("watch")
# bath = Location=("a small bathroom with a towel on the floor.")
# bath.add_pickup("towel")
# porch = Location=("a wooden porch with a rocking chair.")

# dining_room.north = kitchen
# dining_room.south = bedroom
# dining_room.east = bath
# dining_room.west = porch

# location = dining_room
# response = ""

# while True:
#     pass

# print("the end")
# print(total_score)
