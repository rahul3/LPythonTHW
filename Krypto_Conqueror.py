from sys import exit
from random import randint

class Character(object):

    def __init__(self):
        name = "Krypto"
        type = "Warrior"
        health = 100
        taunt = "I'm a gangsta {type} named {name}"
        kills = 0

    def attack(self):
        nonlocal kills
        print("BLAST! BLAST! BLAST! You be dead alien sucker!")
        kills += 1
        print(kills)

new = Character()
new.attack()
