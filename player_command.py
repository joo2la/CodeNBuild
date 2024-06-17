from map import *
def goto(x, y, player_map, player):
    player_map.add_furni_in_coordinates(x, y, 0)
    player_map.add_furni_in_coordinates(x, y, "@")
    player.goto(x, y, 0)
    return None


def info(x, y, player_map, temp):
    temp = None
    print(player_map.get_info_by_coordinates(x, y))
    return None

def use(x, y, player_map, temp):
    temp = None
    player_map.use_furni(x, y)
    
def rotate(x, y, player_map, temp):
    temp = None
    player_map.rotate_furni(x, y)