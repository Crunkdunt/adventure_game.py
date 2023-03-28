class Player:
    def __init__(self):

        self.name = input("Please enter your name: ")
        self.home_town = input("Salutations {}, from where do you hail? ".format(self.name))
        print("Excelent! I hear the weather is.... interesting in " + self.home_town + "!")
        while True:
            data = input("So, {name}.... What animal would you chose as a pet from the following?:\nA:Dog\nB:Cat\nC:Eagle?\nPlease select A, B or C:  ".format(town=self.home_town, name=self.name))
            if data.lower() not in ('a', 'b', 'c'):
                print("Not an appropriate choice.")
            else:
                 break
        if data.lower() == "a":
                self.pet = "Dog"
        elif data.lower() == "b":
                self.pet = "Cat"
        elif data.lower() == "c":
                self.pet = "Eagle"
        print("Indeed, I too enjoy the company of a loyal, steadfast {pet}!\nFinally {name}... ".format(pet=self.pet, name=self.name))
        while True:
            self.battle_cry = input("Please shout your battle cry!")
            if not self.battle_cry.isupper():
                print("Simply not LOUD enough! SHOUT YOUR BATTLE CRY!!!")
            else:
                 break
        print(self.battle_cry + "!!!!!")
                

    def __repr__(self):
        rep = "{name} is a fine person hailing from {town}! Their favorite animal is {pet} and they charge into battle screaming {cry}!!!".format(name=self.name, town=self.home_town, pet=self.pet, cry=self.battle_cry)
        return rep
        
# Create some random areas to travel through.
# class Room:
#      def __init__(self, name, desc, items, exits, enemies, end):
#           self.room_name = name
#           self.room_desc = desc
#         #   self.room_items = items
#           self.exits = exits
#         #   self.enemies = enemies
#         #   self.is_game_end = end

# def starting_room():
#      exits = ["north","south","east","west"]
#      name = "Lounge"
#      desc = "Hey {name}! You're chillin in the lounge. You want to go for a walk. You can go "

player = Player()
print(player)
