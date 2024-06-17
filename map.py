from furni_list import *
symbols_to_remove = "[]',"

class simple_map():
    def __init__(self, x_max:int, y_max:int):
        self.x_maximum = x_max
        self.y_maximum = y_max
        self.map = self.classes_create_map(self.x_maximum, self.y_maximum)
        self.room_furni_list = []
        self.private_cord_list = []
    def classes_create_map(self, x_maximum, y_maximum):
        return [[0]* self.x_maximum for i in range(self.y_maximum)]

    def print_map(self):
        for item in self.map:
            result = str(item)
            for symbol in symbols_to_remove:
                result = result.replace(symbol, "")
            print(result)
        return None
    def updater_furni(self, x, y, furni_id):
        self.map[y-1][x-1] = furni_id
        return None
    def update_map(self):
        if len(self.room_furni_list) != 0:
            for item in self.room_furni_list:
                self.updater_furni(int(item["x"]), int(item["y"]), (item["id"]))
                
    #FURNI
    def use_furni(self, x, y):
        for item in self.room_furni_list:
            if item["x"] == x and item["y"] == y:
                if item["state"] + 1 <= item["possible_states"]:
                    item["state"] += 1
                else:
                    item["state"] = item["min_state"]
                return None
        print("Ошибка")
    
    def rotate_furni(self, x, y):
        for item in self.room_furni_list:
            if item["x"] == x and item["y"] == y:
                if item["direction"] + 1 <= item["possible_directions"]:
                    item["direction"] += 1
                else:
                    item["direction"] = item["min_direction"]
                return None
        print("Ошибка")
    
    def add_furni_in_coordinates(self, x, y, furni_id):
        temp = []
        temp.append(x)
        temp.append(y)
        if furni_id in FURNI_ID_LIST:
            if not temp in self.private_cord_list:
                self.room_furni_list.append(BASIC_FURNI[furni_id])
                last_furni = len(self.room_furni_list)
                self.room_furni_list[last_furni-1]["x"] = x
                self.room_furni_list[last_furni-1]["y"] = y
                self.private_cord_list.append(temp)
                return None
            else:
                print("Вы не можете добавить этот предмет!")
                return None
        else:
            self.map[y-1][x-1] = furni_id
    def get_info_by_coordinates(self, x, y):
        for item in self.room_furni_list:
            if item["x"] == x and item["y"] == y:
                return f'{item["furni_name"]} [{item["id"]}]\nКоординаты:{item["x"]} {item["y"]}\nИнфо:\nКол-во Состояний({item["possible_states"]})\nТекущее состояние ({item["state"]})\nКол-во направлений ({item["possible_directions"]})\nТекущее направление ({item["direction"]})'
        return "По этим координатам нет предмета с информацией"
    
if __name__ == "__main__":
    mapp = simple_map(3, 3)