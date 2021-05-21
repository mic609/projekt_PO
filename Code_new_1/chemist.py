from field import Field
from moveable_object import MoveableObject
from vaccine import Vaccine
from medicine import Medicine
import random

class Chemist(MoveableObject):

    __amount = 0

    def __init__(self, fields, ID, x, y):
        super().__init__(x, y, ID)
        self.__amount += 1
        fields[self._x_cord][self._y_cord].change_obj_amount(1, "Chemist", self._ID)

    def move(self, fields):

        super().where_to_move()
        lastcell = fields[int(super()._x_cord())][int(super()._y_cord())]
        cell = fields[int(super()._x_move_to())][int(super()._y_move_to())]

        while cell.answer() == False:
            super().where_to_move()  # Obiekt zmienia swoj ruch
            cell = fields[int(super()._x_move_to())][int(super()._y_move_to())]

        super()._x_cord = super()._x_move_to
        super()._y_cord = super()._y_move_to
        cell.change_obj_amount(1, "Chemist", super()._ID)
        lastcell.change_obj_amount(-1, "Chemist", -1)

    def interaction(self, cell, humans, viruses, doctors, respirators, vaccines, medicines):

        if cell.check_status()[0] < 2:

            chosen = random.choice([0, 1])

            if int(chosen) == 0:
                self.generate_vaccine(cell, vaccines)
            elif int(chosen) == 1:
                self.generate_medicine(cell, medicines)

        return cell

    def generate_vaccine(self, cell, cure_obj):
        cure_obj.append(Vaccine(super()._x_cord, super()._y_cord, cure_obj.check_amount(), cell))

    def generate_medicine(self, cell, cure_obj):
        cure_obj.append(Medicine(super()._x_cord, super()._y_cord, cure_obj.check_amount(), cell))
