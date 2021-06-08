from PACKAGE.moveable_object import MoveableObject
import time

class Doctor(MoveableObject):

    __amount = 0

    def __init__(self, fields, ID, x, y):
        super().__init__(x, y, ID)
        Doctor.__amount += 1
        fields[self._x_cord][self._y_cord].change_obj_amount(1, "Doctor", self._ID)

    # -------------------------------------------------------------------------
    # Lekarz leczy wybranego czlowieka

    def heal(self, human):
        human.full_restore_health(False)

    # -------------------------------------------------------------------------
    # Lekarz odlacza czlowieka od respiratora, zmienia status respiratora

    def respirator_out(self, respirator, human):
        respirator.change_status(False, human)

    # -------------------------------------------------------------------------
    # Nadzoruje proces ruchu obiektu, zwraca kratke na ktora wchodzi

    def move(self, fields, xsize, ysize):

        lastcell = fields[self._x_cord][self._y_cord]

        if super().neighbour(fields, xsize, ysize, self._x_cord, self._y_cord) == False:
            super().where_to_move(xsize, ysize)
            cell = fields[self._x_move_to][self._y_move_to]

            if cell.check_status()[6] == 1 or cell.check_status()[7] == 1:
                return lastcell

            elif (cell.check_status()[5] > 0 and cell.check_status()[1] > 0):  # napotyka na kratke z respiratorem
                return cell

            else:  # nie Napotyka na kratke z respiratorem
                if super().neighbour(fields, xsize, ysize, self._x_cord, self._y_cord) == False:

                    lastcell.change_obj_amount(-1, "Doctor", -1)

                    while (cell.answer() == False):
                        super().where_to_move(xsize, ysize)  # Obiekt zmienia swoj ruch
                        cell = fields[self._x_move_to][self._y_move_to]

                        # print("INNA KRATKA: ")
                        # print(cell.check_status())
                        #
                        # time.sleep(0.5)
                        # print("LEKARZ")

                    self._x_cord = self._x_move_to
                    self._y_cord = self._y_move_to
                    cell.change_obj_amount(1, "Doctor", self._ID)

                    return cell
        else:
            # print("EXEPTION FOUND")
            return lastcell


    # -------------------------------------------------------------------------
    # Obiekt wchodzi w mozliwe interakcje

    def interaction(self, cell, humans, viruses, doctors, respirators, vaccines, medicines): #,medicines, vaccines): # NAPRAW!!!

        if (cell.check_status()[5] > 0 and cell.check_status()[1] > 0): # Napotyka na respirator
            i = cell.check_ID()[4][0]

            j = cell.check_ID()[0][0]
            self.respirator_out(respirators[i], humans[j])

            # else:
            #     j = cell.check_ID()[0][1]
            #     self.respirator_out(respirators[i], humans[j])

        elif cell.check_status()[1] > 0:  # Napotyka na czlowieka
            if cell.check_ID()[0][0] > 0:
                i = cell.check_ID()[0][0]
            else:
                i = cell.check_ID()[0][1]

            self.heal(humans[i])

    @staticmethod
    def check_amount():
        return Doctor.__amount