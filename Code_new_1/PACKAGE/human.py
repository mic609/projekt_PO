# CHECKED

from PACKAGE.moveable_object import MoveableObject
from PACKAGE.virus import Virus
from PACKAGE.field import Field

class Human(MoveableObject):

    __amount = 0

    # -------------------------------------------------------------------------
    # Przypisujemy obiektowi wartosci poczatkowe
    def __init__(self, HP, infected, immunity, age, resp, fields, ID, x, y): # immunity przechowuje od tej pory czas!
        self.__HP_points = HP
        self.__infected = infected
        self.__immunity = immunity
        self.__age = age
        self.__resp = resp
        super().__init__(x, y, ID)

        Human.__amount += 1 #ZROB TAK WSZEDZIE!!!

        fields[self._x_cord][self._y_cord].change_obj_amount(1, "Human", self._ID) # ZMIANA!!!

    # -------------------------------------------------------------------------
    # Nadzoruje proces ruchu obiektu, zwraca kratke na ktora wchodzi

    def move(self, fields, xsize, ysize):

        lastcell = fields[self._x_cord][self._y_cord]

        if self.__resp == False:

            # print("super().neighbour(fields, xsize, ysize, self._x_cord, self._y_cord): ")
            # print(super().neighbour(fields, xsize, ysize, self._x_cord, self._y_cord))
            if super().neighbour(fields, xsize, ysize, self._x_cord, self._y_cord) == False:

                lastcell.change_obj_amount(-1, "Human", -1)
                super().where_to_move(xsize, ysize)
                cell = fields[self._x_move_to][self._y_move_to]

                while (cell.answer() == False):
                    super().where_to_move(xsize, ysize)  # Obiekt zmienia swoj ruch
                    cell = fields[self._x_move_to][self._y_move_to]

                self._x_cord = self._x_move_to
                self._y_cord = self._y_move_to

                cell.change_obj_amount(1, "Human", self._ID)

                return cell

            else:
                return lastcell

        else: # DODANE
            return lastcell

    # -------------------------------------------------------------------------
    # Obiekt wchodzi w mozliwe interakcje

    def interaction(self, cell, humans, viruses, doctors, respirators, vaccines, medicines):

        if cell.check_status()[1] > 1:  # Napotyka na innego czlowieka

            # print("Natrafilem na innego czlowieka: " )
            # print(self._ID)

            if self.__infected == True:

                i = cell.check_ID()[0][1]

                self.infect_hum(humans[i], cell)

        elif cell.check_status()[2] > 0:  # Napotyka na wirusa
            # print("ZARAZAM")
            i = cell.check_ID()[1][0]

            # print("Natrafilem na wirusa: ")
            # print(self._ID)

            if i != -1:
                # print("wirus i: " + str(i))
                if self.__immunity == 0:
                    # print("HUMAN self: ")
                    # print(self)
                    viruses[i].infect(self, cell)

                    # viruses[i].destroy(cell)

                else:
                    viruses[i].destroy(cell)

        elif cell.check_status()[3] > 0: # Napotyka na lekarza
            i = cell.check_ID()[2][0]

            # print("Natrafilem na lekarza: ")
            # print(self._ID)

            if i != -1:
                doctors[i].heal(self)

        elif cell.check_status()[5] > 0: # Napotyka na respirator
            i = cell.check_ID()[4][0]

            # print("Natrafilem na respirator: ")
            # print(self._ID)

            if (i != -1 and self.__infected == True and self.__resp != True):
                # print("ZOSTALEM PODLACZONY! ")
                self.__resp = respirators[i].change_status(True, self, self.__HP_points)

        elif cell.check_status()[6] > 0: # Napotyka na szczepionke
            i = cell.check_ID()[5][0]

            # print("Natrafilem na szczepionke: ")
            # print(self._ID)

            if i != -1:
                self.__immunity = vaccines[i].give_immunity(self.__immunity)
                vaccines[i].destroy(cell)

        elif cell.check_status()[7] > 0: # Napotyka na lekarstwo
            i = cell.check_ID()[6][0]

            # print("Natrafilem na lekarstwo: ")
            # print(self._ID)

            if i != -1:

                self.__HP_points = medicines[i].heal(self.__HP_points)

                if self.__infected == True:
                    self.__infected = False
                    self.__immunity = 30

                medicines[i].destroy(cell)


        # elif cell.check_status()[4] > 0:
        #     print("Natrafilem na chemika")
        #     print(self._ID)
        # else:
        #     print("Na nic nie natrafilem")
        #     print(self._ID)

    # -------------------------------------------------------------------------
    # Funkcja obniza HP czlowieka w zaleznosci od wieku

    def reduce_health(self, cell): # COS TU NIE GRA!!!

        # print("self.__immunity: " + str(self.__immunity))
        # print("self.__resp: " + str(self.__resp))
        # print("self.__infected: " + str(self.__infected))

        if self.__immunity == 0 and self.__resp == False and self.__infected == True:
            # print("JESTEM NIE PRZEJMUJ SIE!")
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
                        Human.__amount -= 1
                        cell.change_obj_amount(-1, "Human", -1)
                        break
                reduce += 2
                expected_age += 25

        # print("HEALTH: " + str(self.__HP_points))
        # print("ID: " + str(self._ID))

    # -------------------------------------------------------------------------
    # Funkcja zaraza wybranego czlowieka, jesli czlowiek jest odporny, wirus zostaje unicestwiony

    def infect_hum(self, human, cell, virus = None):

        # print("ZARAZAM 2")
        # print("virus: ")
        # print(virus)
        # print(human.__immunity)

        if human.__immunity == 0:

            # print("HUMAN: ")
            # print(human)

            human.__infected = True
            # print("human infect: ")
            # print(human.__infected)
            #human.reduce_health(cell)

        elif virus != None:

            if cell.check_ID()[1][0] >= 0:
                virus.destroy(cell)

    # -------------------------------------------------------------------------
    # Funkcja przywraca czlowiekowi w pelni zdrowie

    def full_restore_health(self, resp_call):

        if resp_call == False:

            # if self.__HP_points < 100:
                # print("LEKARZ LECZY: ")
                # print("ID: " + str(self._ID))
                # print(self.__HP_points)

            if self.__HP_points < 100 and self.__infected == True:
                self.__infected = False
                self.__HP_points = 100
                self.__immunity = 30

            # print("PO: " + str(self.__HP_points))
            # print("\n\n\n")

        else: # Kiedy czlowiek jest odlaczany od respiratora
            self.__infected = False
            self.__HP_points = 100
            self.__resp = False

            # print("RESP CALL")
            # print("Czlowiek nr: " + str(self._ID))
            # print("Podlaczony do respiratora: ")
            # print(self.__resp)
            # print("\n\n\n")

    # -------------------------------------------------------------------------
    # Funkcja nadzoruje czas trwania chwilowej odpornosci
    def decrease_immunity_time(self):
        # print("IMMUNITY: "+str(self.__immunity))
        if self.__immunity > 0:
            self.__immunity -= 1

    # -------------------------------------------------------------------------
    # Funkcja usmierca obiekt ludzki
    def kill(self, fields):
        self._x_cord = -1
        self._y_cord = -1
        self.__amount -= 1
        self.__infected = False
        self.__resp = False
        fields.change_obj_amount(-1, "Human", -1)

    @staticmethod
    def check_amount():
        return Human.__amount





    def human_current_infected(self):
        # print("ID: " + str(self._ID))
        # print("Zainfekowany: ")
        # print(self.__infected)
        # print("PUNKTY HP: ")
        # print(self.__HP_points)
        # print("ODPORNOSC: ")
        # print(self.__immunity)
        # print("RESPIRATOR: ")
        # print(self.__resp)
        # print("\n\n\n")

        if self._x_cord != -1:
            if self.__infected == True:
                return 1
            elif self.__infected == False:
                return 0
        else:
            return 0

    def human_current_immuned(self):

        if self._x_cord != -1:
            if self.__immunity > 0:
                return 1
            else:
                return 0
        else:
            return 0