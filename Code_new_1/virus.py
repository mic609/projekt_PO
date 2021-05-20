from moveable_object import MoveableObject

class Virus(MoveableObject):

    __amount = 0

    def __init__(self, fields, ID):
        super().__init__(ID)
        self.__amount += 1
        fields[super()._x_cord][super()._y_cord].change_obj_amount(1, "Virus", super()._ID)

    # -------------------------------------------------------------------------

    def interaction(self, cell, humans, viruses, doctors, respirators):#, medicines, vaccines): # NAPRAW!!!

        if cell.check_status()[1] > 0:

            if cell.check_ID()[0][0] > 0:
                i = cell.check_ID()[0][0]
            else:
                i = cell.check_ID()[0][1]

            self.infect(humans[i], cell)

    # -------------------------------------------------------------------------

    def infect(self, cell, human):
        human.infect(human, cell, self)

    # -------------------------------------------------------------------------

    def destroy(self, fields):
        super()._x_cord = -1
        super()._y_cord = -1
        self.__amount -= 1
        fields.change_obj_amount(-1, "Virus", -1)