from room import Room
from item import Item
from character import Character, Enemy

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty place, buzzing with flies")

ballroom = Room("Ballroom")
ballroom.set_description(
    "A large room with ornate golden decorations on each wall")

dining_hall = Room("Dining hall")
dining_hall.set_description(
    "A vast room with a shiny wooden floor; huge candlesticks guard the entrance")

kitchen.link_room(dining_hall, 'south')
dining_hall.link_room(kitchen, 'north')
dining_hall.link_room(ballroom, 'west')
ballroom.link_room(dining_hall, 'east')

dave = Enemy("Dave", "A smelly zombie!")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

# print('What will you fight with?')
# fight_with = input('> ')
# dave.fight(fight_with)

current_room = kitchen

while True:
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    command = input("> ")
    current_room = current_room.move(command)
    print("\n")
