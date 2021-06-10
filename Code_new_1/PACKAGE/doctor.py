from PACKAGE.moveable_object import MoveableObject

# ILOSC METOD: 6 (w tym konstruktor)

class Doctor(MoveableObject):

    __amount = 0

    def __init__(self, fields, ID, x, y):
        super().__init__(x, y, ID)
        Doctor.__amount += 1
        fields[self._x_cord][self._y_cord].change_obj_amount(1, "Doctor", self._ID)

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Nadzoruje proces ruchu obiektu

    def move(self, fields, xsize, ysize):

        lastcell = fields[self._x_cord][self._y_cord]

        # Obiekt sie ruszy, jesli ma miejsce. Jesli bylby otoczony, nie ruszy sie:
        if super().neighbour(fields, xsize, ysize, self._x_cord, self._y_cord) == False:

            super().where_to_move(xsize, ysize)
            cell = fields[self._x_move_to][self._y_move_to]

            # Napotka na obiekty lecznicze (nie ruszy sie)
            if cell.check_status()[6] == 1 or cell.check_status()[7] == 1:
                return lastcell

            # Napotyka na kratke z respiratorem (nie ruszy sie)
            elif (cell.check_status()[5] > 0 and cell.check_status()[1] > 0):
                return cell

            # Nie Napotyka na kratke z respiratorem
            else:
                if super().neighbour(fields, xsize, ysize, self._x_cord, self._y_cord) == False:

                    lastcell.change_obj_amount(-1, "Doctor", -1)

                    # Jesli obiekt bedzie chcial sie ruszyc tam, gdzie nie ma miejsca, zmien kordynaty:
                    while (cell.answer() == False):
                        super().where_to_move(xsize, ysize)
                        cell = fields[self._x_move_to][self._y_move_to]

                    # Ostateczne zmiany:
                    self._x_cord = self._x_move_to
                    self._y_cord = self._y_move_to
                    cell.change_obj_amount(1, "Doctor", self._ID)

                    return cell
        else:
            return lastcell


    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Obiekt wchodzi w mozliwe interakcje

    def interaction(self, cell, humans, viruses, doctors, respirators, vaccines, medicines): #,medicines, vaccines): # NAPRAW!!!

        # Lekarz natrafia na czlowieka podlaczonego do respiratora:
        if (cell.check_status()[5] > 0 and cell.check_status()[1] > 0):

            i = cell.check_ID()[4][0]
            j = cell.check_ID()[0][0]

            self.respirator_out(respirators[i], humans[j])

        # Lekarz natrafia na czlowieka (nie podlaczonego) i go leczy
        elif cell.check_status()[1] > 0:

            if cell.check_ID()[0][0] > 0:
                i = cell.check_ID()[0][0]
            else:
                i = cell.check_ID()[0][1]

            self.heal(humans[i])

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Lekarz leczy wybranego czlowieka

    def heal(self, human):
        human.full_restore_health(False)

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Lekarz odlacza czlowieka od respiratora, zmienia status respiratora

    def respirator_out(self, respirator, human):
        respirator.change_status(False, human)

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Zwraca ilosc obiektow

    @staticmethod
    def check_amount():
        return Doctor.__amount