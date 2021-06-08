from PACKAGE.field import Field
from PACKAGE.moveable_object import MoveableObject
from PACKAGE.vaccine import Vaccine
from PACKAGE.medicine import Medicine
import random

class Chemist(MoveableObject):

    __amount = 0
    __med_indeks = 0
    __vac_indeks = 0

    def __init__(self, fields, ID, x, y, ):
        super().__init__(x, y, ID)
        Chemist.__amount += 1

        self.__moment = 0 # !!!

        fields[self._x_cord][self._y_cord].change_obj_amount(1, "Chemist", self._ID)

    def move(self, fields, xsize, ysize):

        super().where_to_move(xsize, ysize)
        lastcell = fields[self._x_cord][self._y_cord]


        if super().neighbour(fields, xsize, ysize, self._x_cord, self._y_cord) == False:

            if self.__moment == 1:

                cell = fields[self._x_move_to][self._y_move_to]

                while cell.answer() == False:
                    super().where_to_move(xsize, ysize)  # Obiekt zmienia swoj ruch
                    cell = fields[self._x_move_to][self._y_move_to]

                self._x_cord = self._x_move_to
                self._y_cord = self._y_move_to
                cell.change_obj_amount(1, "Chemist", self._ID)
                lastcell.change_obj_amount(-1, "Chemist", -1)
                self.__moment -= 1

                return cell

            else:

                self.__moment += 1
                return lastcell
        else:
            return lastcell

    def interaction(self, cell, humans, viruses, doctors, respirators, vaccines, medicines):

        list = cell.check_status()

        if list[0] == 1: # Tylko chemik stoi na kratce

            chosen = random.choice([0, 1])

            if int(chosen) == 0:
                if cell.check_status()[7] != 1:
                    self.generate_vaccine(cell, vaccines)
            elif int(chosen) == 1:
                if cell.check_status()[6] != 1:
                    self.generate_medicine(cell, medicines)

        # return cell

    def generate_vaccine(self, cell, cure_obj):
        cure_obj.append(Vaccine(self._x_cord, self._y_cord, Chemist.__vac_indeks, cell))
        Chemist.__vac_indeks += 1

    def generate_medicine(self, cell, cure_obj):
        cure_obj.append(Medicine(self._x_cord, self._y_cord, Chemist.__med_indeks, cell))
        Chemist.__med_indeks += 1

    @staticmethod
    def check_amount():
        return Chemist.__amount