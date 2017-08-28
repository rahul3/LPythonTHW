from sys import exit
from random import randint

class Character(object):

    def __init__(self):
        type = "Warrior"
        kills = 0
        health = 100
        taunt = "I'm a gangsta {type}"

    def attack(self,name):
        self.name = name;
        print("BLAST! BLAST! BLAST! You be dead alien sucker!")
        kill = kill + 1

class Spaceship(object):
    def __init__(self):
        next_room = "default"
        opening_room = "Red Room"


class Room(Spaceship):



    def __init__(self):
        death_type = "default"
        monster = "default"
        solution = "default"
        surprise = "default"
        escape_pod = "no"

    def Red_Room(self):
        death_type = "Drowned in photography water! AAAAAAAA!!!!"
        next_room = "Blue Room"
        monster = "Photography Monster"
        solution = "fire"
        surprise = "Flash light crashes in front of you! With alien models running away!!!"

    def Blue_Room(self):
        death_type = "Eaten by puppies!"
        next_room = "Green Room"
        monster = "Puppy Monster"
        solution = "fire"
        surprise = "Puppies scrambling away!!!!"

    def Green_Room(self):
        death_type = "Death by SLIME! SLIME! SLIME! SLIME!"
        next_room = "Green Room"
        monster = "Puppy Monster"
        solution = "fire"
        surprise = "Puppies scrambling away!!!!"

class Death(Room):
    pass


class Alien(Room):
    color = "green"
    horns = 5
    size = "small"
    attack = "default"
    mega_laser = "no"

class Boss_Alien(Alien):

    color = "blue"
    horns = "200"
    mega_laser = "yes"
    attack = "KABOOM! KABOOM! KABOOM!"

    def attack(self):
        print("{attack}\t{attack}\t{attack}\nYOU ARE DEAD!!!")
        exit(0)

class Underling_Alien(Alien):

    attack = "Zap zap zap! Zap zap zap!"
    def attack(self):
        print("{attack}\t{attack}\t{attack}\nYOU ARE DEAD!!!")



class Weapons(Spaceship):
    ammo = 3


class Stun_gun(Weapons):
    pass

class BFG(Weapons):
    pass

class Engine(object):
    pass


class Map(object):
    room_obj = Room()
    run_entry = {
                'Red Room': room_obj.Red_Room(),
                'Blue Room': room_obj.Blue_Room(),
                'Green Room': room_obj.Green_Room(),
                'Death': Death(),
                # 'Complete': Complete(),
            }

    def __init__(self, opening_scene):
        self.opening_scene = opening_scene

    def next_room(self,room_name):
        val = self.run_entry.get(room_name)
        return val

    def opening_scene(self):
        return self.next_room(self.opening_scene)
