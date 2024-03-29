from PACKAGE.moveable_object import MoveableObject

class Virus(MoveableObject):

    __amount = 0

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Konstruktor

    def __init__(self, fields, ID, x, y):
        super().__init__(x, y, ID)
        Virus.__amount += 1
        fields[self._x_cord][self._y_cord].change_obj_amount(1, "Virus", self._ID)

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Nadzoruje proces ruchu obiektu

    def move(self, fields, xsize, ysize):

        # Wirus wybiera gdzie sie ruszyc:
        super().where_to_move(xsize, ysize)
        lastcell = fields[self._x_cord][self._y_cord]

        # Obiekt sie ruszy, jesli ma miejsce. Jesli bylby otoczony, nie ruszy sie:
        if super().neighbour(fields, xsize, ysize, self._x_cord, self._y_cord) == False:
            cell = fields[self._x_move_to][self._y_move_to]

            # Jesli wirus widzi lekarstwo lub szczepionke, nie ruszy sie
            if cell.check_status()[6] == 1 or cell.check_status()[7] == 1:
                return lastcell

            else:

                # Jesli obiekt bedzie chcial sie ruszyc tam, gdzie nie ma miejsca, zmien kordynaty:
                while (cell.answer() == False):
                    super().where_to_move(xsize, ysize)  # Obiekt zmienia swoj ruch
                    cell = fields[self._x_move_to][self._y_move_to]

                # Ostateczne zmiany:
                self._x_cord = self._x_move_to
                self._y_cord = self._y_move_to
                cell.change_obj_amount(1, "Virus", self._ID)
                lastcell.change_obj_amount(-1, "Virus", -1)
                return cell
        else:
            return lastcell

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Dostepne interakcje jakie obiekt wykonuje

    def interaction(self, cell, humans, viruses, doctors, respirators, vaccines, medicines):

        # Wirus natrafia na czlowieka
        if cell.check_status()[1] > 0:

            if cell.check_ID()[0][0] > 0:
                i = cell.check_ID()[0][0]
            else:
                i = cell.check_ID()[0][1]
            self.infect(humans[i], cell)

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Metoda zarazi wybranego czlowieka

    def infect(self, human, cell):
        human.infect_hum(human, cell, self)

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Unicestwi wirusa znajdujacego sie na wybranej kratce

    def destroy(self, fields):
        self._x_cord = -1
        self._y_cord = -1
        Virus.__amount -= 1
        fields.change_obj_amount(-1, "Virus", -1)

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------

    @staticmethod
    def check_amount():
        return Virus.__amount