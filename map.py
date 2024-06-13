from furni_list import *

class simple_map():
    def __init__(self, x_max:int, y_max:int):
        self.x_maximum = x_max
        self.y_maximum = y_max
        self.map = self.classes_create_map(self.x_maximum, self.y_maximum)
        self.room_furni_universal_id_list = []
    def classes_create_map(self, x_maximum, y_maximum):
        return [[0]* self.x_maximum for i in range(self.y_maximum)]

    #OUTPUT FUNCTION
    def print_map(self):
        for item in self.map:
            print(item)
        return None

    #FURNI FUNCTION
    def add_furni_in_coordinates(self, x, y, furni_id):
        self.map[y-1][x-1] = furni_id
        self.room_furni_universal_id_list.append(BASIC_FURNI[furni_id])
        last_furni = len(self.room_furni_universal_id_list)
        self.room_furni_universal_id_list[last_furni-1]["x"] = x
        self.room_furni_universal_id_list[last_furni-1]["y"] = y
