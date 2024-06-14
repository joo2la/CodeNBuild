from player_action_list import *
from furni_list import *
from player import *
from map import *

version = "0.1 ALPHA"
op_list = ["1", "2", "3", "4"]
map_created = False
player_created = False

player_mode = False
chat = []
print(f"Simple Retro Hotel Emulator v{version}")

while True:
    print("[1] - Create Map")
    print("[2] - Print Map")
    print("[3] - Add Furni in Map")
    print("[4] - Player Mode")
    op_id = input("")
    if op_id in op_list:
        op = int(op_id)
        
        if op == 1:
            x = input("Enter Max X Coordinate>")
            y = input("Enter Max Y Coordinate>")
            
            try:
                map_created = True
                my_map = simple_map(int(x), int(y))
            except:
                map_created = True
                my_map = simple_map(3, 3)
        
        if op == 2:
            if map_created:
                my_map.print_map()
            else:
                print("Map is not created :(")
        if op == 3:
            if map_created:
                furni_special_id = input("Enter Special Furni Id>")
                x = input("Enter X Coordinate>")
                y = input("Enter Y Coordinate>")
                my_map.add_furni_in_coordinates(int(x), int(y), int(furni_special_id))
                try:
                    my_map.add_furni_in_coordinates(int(x), int(y), int(furni_special_id))
                except:
                    print("Invalid Values")
            else:
                print("Map is not created :(")
        if op == 4:
            player_mode = True
            while player_mode:
                if player_created:
                    my_map.print_map()
                    if len(chat) == 8:
                        chat.pop(0)
                    for item in chat:
                        print(f'{my_player.username}: {item}')
                    message = input("Chat>")
                    chat.append(message)
                else:
                    if map_created:
                        username = input("Enter you Username>")
                        x = input("Enter X Coordinate>")
                        y = input("Enter Y Coordinate>")
                        my_player = simple_player(username, x, y)
                        player_created = True
                        my_map.add_furni_in_coordinates(int(x), int(y), "@")
                    else:
                        print("Map is not created :(")
                        player_mode = False
