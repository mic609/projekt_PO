from PACKAGE.field import Field
from PACKAGE.moveable_object import MoveableObject
from PACKAGE.vaccine import Vaccine
from PACKAGE.medicine import Medicine
import random

class Chemist(MoveableObject):

    __amount = 0
    __indeks = 0

    def __init__(self, fields, ID, x, y):
        super().__init__(x, y, ID)
        self.__amount += 1
        fields[self._x_cord][self._y_cord].change_obj_amount(1, "Chemist", self._ID)

    def move(self, fields, xsize, ysize):

        super().where_to_move(xsize, ysize)
        lastcell = fields[self._x_cord][self._y_cord]
        cell = fields[self._x_move_to][self._y_move_to]

        while cell.answer() == False:
            super().where_to_move(xsize, ysize)  # Obiekt zmienia swoj ruch
            cell = fields[self._x_move_to][self._y_move_to]

        self._x_cord = self._x_move_to
        self._y_cord = self._y_move_to
        cell.change_obj_amount(1, "Chemist", self._ID)
        lastcell.change_obj_amount(-1, "Chemist", -1)
        return cell

    def interaction(self, cell, humans, viruses, doctors, respirators, vaccines, medicines):

        list = cell.check_status()

        if list[0] < 2:

            chosen = random.choice([0, 1])

            if int(chosen) == 0:
                self.generate_vaccine(cell, vaccines)
            elif int(chosen) == 1:
                self.generate_medicine(cell, medicines)

        return cell

    def generate_vaccine(self, cell, cure_obj):
        cure_obj.append(Vaccine(self._x_cord, self._y_cord, self.__indeks, cell))
        self.__indeks += 1

    def generate_medicine(self, cell, cure_obj):
        cure_obj.append(Medicine(self._x_cord, self._y_cord, self.__indeks, cell))
        self.__indeks += 1
