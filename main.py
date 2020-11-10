from room import Room
from item import Item
from character import Enemy, Friend
from info import Info

spooky_house = Info("The Spooky House", "A Text-based Horror Game")
spooky_house.welcome()
Info.info()
Info.author = "Pedro Castilho"

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty place, buzzing with flies")

ballroom = Room("Ballroom")
ballroom.set_description(
    "A large room with ornate golden decorations on each wall")

dining_hall = Room("Dining Hall")
dining_hall.set_description(
    "A vast room with a shiny wooden floor; huge candlesticks guard the entrance")

print("There are " + str(Room.number_of_rooms) + " rooms to explore")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

dave = Enemy("Dave", "A smelly zombie!")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

catrina = Friend("Catrina", "A friendly skeleton")
catrina.set_conversation("Hello, there!")
ballroom.set_character(catrina)

cheese = Item("cheese")
cheese.set_description("A large and smelly block of cheese")
ballroom.set_item(cheese)

book = Item("book")
book.set_description("A really good book entitled 'Knitting for dummies'")
dining_hall.set_item(book)

current_room = kitchen
backpack = []
dead = False

while dead == False:
    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print('What will you fight with?')
            fight_with = input('> ')
            if fight_with in backpack:
                if inhabitant.fight(fight_with) == True:
                    print("Hooray, you won the fight!")
                    current_room.set_character(None)
                    if Enemy.enemies_to_defeat == 0:
                        print("Congratulations, you have vanquished the enemy horde!")
                        dead = True
                else:
                    print("Oh dear, you lost the fight")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")
    elif command == "hug":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that if I were you...")
            else:
                inhabitant.hug()
        else:
            print("There is no one here to hug :(")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)

Info.credits()
