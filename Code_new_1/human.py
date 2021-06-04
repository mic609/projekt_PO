# CHECKED

from PACKAGE.moveable_object import MoveableObject
from PACKAGE.virus import Virus
from PACKAGE.field import Field

class Human(MoveableObject):

    __amount = 0

    # -------------------------------------------------------------------------
    # Przypisujemy obiektowi wartosci poczatkowe
    def __init__(self, HP, infected, immunity, age, resp, fields, ID, xsize, ysize): # immunity przechowuje od tej pory czas!
        self.__HP_points = HP
        self.__infected = infected
        self.__immunity = immunity
        self.__age = age
        self.__resp = resp
        super().__init__(xsize, ysize, ID)
        self.__amount += 1
        fields[self._x_cord][self._y_cord].change_obj_amount(1, "Human", self._ID) # ZMIANA!!!

    # -------------------------------------------------------------------------
    # Nadzoruje proces ruchu obiektu, zwraca kratke na ktora wchodzi

    def move(self, fields, xsize, ysize):

        if self.__resp == False:
            super().where_to_move(xsize, ysize)
            lastcell = fields[self._x_cord][self._y_cord]
            cell = fields[self._x_move_to][self._y_move_to]

            while (cell.answer() == False):
                super().where_to_move(xsize, ysize)  # Obiekt zmienia swoj ruch
                cell = fields[self._y_move_to][self._y_move_to]

            self._x_cord = self._x_move_to
            self._y_cord = self._y_move_to
            cell.change_obj_amount(1, "Human", self._ID)
            lastcell.change_obj_amount(-1, "Human", -1)
            return cell

    # -------------------------------------------------------------------------
    # Obiekt wchodzi w mozliwe interakcje

    def interaction(self, cell, humans, viruses, doctors, respirators, vaccines, medicines):

        if cell.check_status()[1] > 1:  # Napotyka na innego czlowieka
            i = cell.check_ID()[0][1]
            self.infect_hum(humans[i], cell)

        elif (cell.check_status())[2] > 0:  # Napotyka na wirusa
            i = cell.check_ID()[1][0]
            if i != -1:
                if self.__immunity == 0:
                    viruses[i].infect(self, cell)
                else:
                    viruses[i].destroy(cell)

        elif (cell.check_status())[3] > 0: # Napotyka na lekarza
            i = cell.check_ID()[2][0]
            if i != -1:
                doctors[i].heal(self)

        elif cell.check_status()[5] > 0: # Napotyka na respirator
            i = cell.check_ID()[4][0]
            if i != -1:
                respirators[i].change_status(True, self, self.__HP_points)
                self.__resp = True

        elif cell.check_status()[6] > 0: # Napotyka na szczepionke
            i = cell.check_ID()[5][0]
            if i != -1:
                self.__immunity = vaccines[i].give_immunity(self.__immunity)
                vaccines[i].destroy(cell)

        elif cell.check_status()[7] > 0: # Napotyka na lekarstwo
            i = cell.check_ID()[6][0]
            if i != -1:
                self.__HP_points = medicines[i].heal(self.__HP_points)[0] # Dobrze to jest???
                self.__infected = medicines[i].heal(self.__HP_points)[1]
                medicines[i].destroy(cell)

    # -------------------------------------------------------------------------
    # Funkcja obniza HP czlowieka w zaleznosci od wieku

    def reduce_health(self, cell):

        if self.__immunity == 0 and self.__resp == False:

            reduce = 3
            expected_age = 0

            while reduce <= 9:
                if self.__age >= expected_age and self.__age <= expected_age + 25:
                    if self.__HP_points > reduce:
                        self.__HP_points -= reduce
                        break
                    else:
                        self.__HP_points = 0
                        self.kill(cell)
                        self.__amount -= 1
                        cell.change_obj_amount(-1, "Human", -1)
                        break
                reduce += 2
                expected_age += 25

    # -------------------------------------------------------------------------
    # Funkcja zaraza wybranego czlowieka, jesli czlowiek jest odporny, wirus zostaje unicestwiony

    def infect_hum(self, human, cell, virus = None):

        if human.__immunity == 0:

            human.infected = True
            human.reduce_health(cell)

        elif virus != None:
            if (cell.check_id())[1][0] >= 0:
                virus.destroy(cell)

    # -------------------------------------------------------------------------
    # Funkcja przywraca czlowiekowi w pelni zdrowie

    def full_restore_health(self, resp_call = False):

        if resp_call == False:
            self.__infected = False
            self.__HP_points = 100

        else: # Kiedy czlowiek jest podlaczany od respiratora
            self.__infected = False
            self.__HP_points = 100
            self.__resp = False

    # -------------------------------------------------------------------------
    # Funkcja nadzoruje czas trwania chwilowej odpornosci
    def decrease_immunity_time(self):
        if self.__immunity > 0:
            self.__immunity -= 1

    # -------------------------------------------------------------------------
    # Funkcja usmierca obiekt ludzki
    def kill(self, fields):
        self._x_cord = -1
        self._y_cord = -1
        self.__amount -= 1
        fields.change_obj_amount(-1, "Human", -1)

    # -------------------------------------------------------------------------
    # Funkcja zwraca ID czlowieka