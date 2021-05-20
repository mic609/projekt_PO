from field import Field
from moveable_object import MoveableObject
import random

class Chemist(MoveableObject):

    __amount = 0

    def __init__(self, fields, ID):
        super().__init__(ID)
        self.__amount += 1
        fields[super()._x_cord][super()._y_cord].change_obj_amount(1, "Chemist", super()._ID)

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

        chosen = random.choice([0,1])

        if int(chosen) == 0:
            self.generate_vaccine(cell)
        elif int(chosen) == 1:
            self.generate_medicine(cell)

        return cell

    def generate_vaccine(self, cell):
