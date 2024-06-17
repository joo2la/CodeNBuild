from functions import *

version = "0.2 ALPHA"
op_list = ["1", "2", "3", "4", "5", "6"]
operations = {
    1 : create_map,
    2 : map_printer,
    3 : create_furni,
    4 : start_player_mode,
    5 : print_furni_id_with_list,
    6 : settings
    }

print(f"CodeNBuild GAME v{version}")

while True:
    print("[1] - Создать карту")
    print("[2] - Вывести карту")
    print("[3] - Создать мебель на карту")
    print("[4] - Режим Игрока")
    print("[5] - Список Мебели")
    print("[6] - Настройки")
    op_id = input("")
    if op_id in op_list:
        operations[int(op_id)]()
    else:
        print("Операция не найдена :(")
