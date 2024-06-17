import os
import pickle
from player_action_list import *
from furni_list import *
from map import *
from player import *

commands = [":info", ":goto", ":use", ":exit", ":rotate"]
map_created = False
player_created = False
player_mode = False
chat = []

#SETTINGS
chat_len = 8

set_op_list = ["1", "2", "3"]

def print_furni_id_with_list():
    for key in BASIC_FURNI:
        item = BASIC_FURNI[key]
        print(f'Название/Специальный ID {item["furni_name"]} [{item["id"]}]\nИнфо:\nКол-во Состояний({item["possible_states"]})\nТекущее состояние ({item["state"]})\nКол-во направлений ({item["possible_directions"]})\nТекущее направление ({item["direction"]})\nМожно ли ходить ({item["walkable"]})\n')
def settings():
    global chat_len
    print(f"[1] Длина чата({chat_len})")
    print("[2] Сохранить мир")
    print("[3] Загрузить мир")
    set_op = input("")
    if set_op in set_op_list:
        set_op = int(set_op)
        if set_op == 1:
            try:
                chat_len = int(input("Введите длину чата>"))
            except:
                chat_len = 8
                print("Ошибка(")
        elif set_op == 2:
            save_all()
        elif set_op == 3:
            load_all()
    else:
        print("Операция не найдена.. :(")

def load_all():
    filename = input("Название файла(ТОЛЬКО .pickle)>")
    global my_map
    global my_player
    global player_created
    global map_created
    global chat
    global chat_len
    with open(filename, "rb") as fh:
        save_data = pickle.load(fh)
        my_map = save_data["map"]
        my_player = save_data["player"]
        player_created = save_data["player_created"]
        map_created = save_data["map_created"]
        chat = save_data["chat"]
        chat_len = save_data["chat_len"]
        my_map.update_map()
def save_all():
    filename = input("Название файла(ТОЛЬКО .pickle)>")
    my_map.update_map()
    save_data = {
        "map" : my_map,
        "player" : my_player,
        "player_created" : player_created,
        "map_created" : map_created,
        "chat" : chat,
        "chat_len" : chat_len
        }
    with open(filename, 'wb') as fh:
        pickle.dump(save_data, fh)
    
def create_map():
    os.system("cls||clear")
    x = input("Введите максимальную X>")
    y = input("Введите максимальную Y>")
    global map_created
    global my_map
    map_created = True
    try:
        my_map = simple_map(int(x), int(y))
    except:
        my_map = simple_map(3, 3)

def map_printer():
    os.system("cls||clear")
    if map_created:
        my_map.update_map()
        my_map.print_map()
    else:
        print("У вас нет карты :(")

def create_furni():
    os.system("cls||clear")
    if map_created:
        my_map.update_map()
        my_map.print_map()
        furni_special_id = input("Введите специальный id мебели>")
        x = input("Координата X>")
        y = input("Координата Y>")
        try:
            my_map.add_furni_in_coordinates(int(x), int(y), int(furni_special_id))
        except:
            print("Ошибка значения")
    else:
        print("У вас нет карты :(")

def start_player_mode():
    os.system("cls||clear")
    global player_mode
    global player_created
    global my_player
    
    player_mode = True
    while player_mode:
        if player_created:
            my_map.update_map()
            my_map.print_map()
            if len(chat) == chat_len:
                chat.pop(0)
            for item in chat:
                print(f'{my_player.username}: {item}')
            message = input("Чат>")
            check = message.split()
            try:
                if check[0] not in commands:
                    chat.append(message)
            except:
                chat.append(message)
            else:
                command_line = message.split()
                try:
                    if command_line[0] == ":info":
                        os.system("cls||clear")
                        print(my_map.get_info_by_coordinates(int(command_line[1]), int(command_line[2])))
                    elif command_line[0] == ":goto":
                        os.system("cls||clear")
                        my_map.add_furni_in_coordinates(int(my_player.x), int(my_player.y), 0)
                        my_map.add_furni_in_coordinates(int(command_line[1]), int(command_line[2]), "@")
                        my_player.goto(int(command_line[1]), int(command_line[2]), 0)
                    elif command_line[0] == ":use":
                        os.system("cls||clear")
                        my_map.use_furni(int(command_line[1]), int(command_line[2]))
                    elif command_line[0] == ":rotate":
                        os.system("cls||clear")
                        my_map.rotate_furni(int(command_line[1]), int(command_line[2]))
                    elif command_line[0] == ":exit":
                        os.system("cls||clear")
                        return None
                    else:
                        os.system("cls||clear")
                except IndexError:
                    print("Вы неправильно ввели команду. Возможно, вы забыли добавить координаты.")
        else:
            if map_created:
                username = input("Никнейм>")
                x = input("Начальные координаты X>")
                y = input("Начальные координаты Y>")
                my_player = simple_player(username, x, y)
                player_created = True
                my_map.add_furni_in_coordinates(int(x), int(y), "@")
            else:
                print("У вас нет карты :(")
                player_mode = False