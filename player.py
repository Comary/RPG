# Comary
# 2019-05-24
# This is a player object class that allows the user to heal, fight and view inventory

# Imports
import random

# The Object class
class player(object):
    
    # initialize the attributes
    def __init__(self):
        self.hp = 100
        self.hp_max = 100
        self.mp = 100
        self.stam = 100
        self.dam = 0
    
    def heal(self, obj): # Heal the player using an healing item TBAL
        if self.hp + obj.heals < self.hp_max:
            print('You Have healed for ' + obj.heals + '.')
            self.hp += obj.heals
        elif self.hp + obj.heals > self.hp_max:
            while True:
                print('\n')
                print('You will be wasting a bit of this potion, Are you sure you want to use this?')
                print('Enter [y] or [n] To Continue.')
                var = input('>>>  ')
                if var == 'y' or var == 'Y':
                    pass
                elif var == 'n' or var == 'N':
                    pass
                else:
                    print('Please enter [y] or [n]')
                    continue
            
