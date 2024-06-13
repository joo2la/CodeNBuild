from furni_list import *
from map import *

class simple_player():
    def __init__(self, username, x, y):
        self.username = username
        self.x = x
        self.y = y
        self.action = 1

    def set_action(self, action_id):
        self.action = action_id
        
    def walk(self, x = True, y = True):
        if x:
            x = self.x
        elif y:
            y = self.y
        self.x = x
        self.y = y
