# CHECKED

from PACKAGE.moveable_object import MoveableObject
from PACKAGE.virus import Virus
from PACKAGE.field import Field

# ILOSC METOD: 12 (w tym konstruktor)

class Human(MoveableObject):

    __amount = 0

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Przypisujemy obiektowi wartosci poczatkowe

    def __init__(self, HP, infected, immunity, age, resp, fields, ID, x, y):
        self.__HP_points = HP
        self.__infected = infected
        self.__immunity = immunity # czas odpornosci
        self.__age = age
        self.__resp = resp
        super().__init__(x, y, ID)

        Human.__amount += 1

        fields[self._x_cord][self._y_cord].change_obj_amount(1, "Human", self._ID)

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Nadzoruje proces ruchu obiektu

    def move(self, fields, xsize, ysize):

        lastcell = fields[self._x_cord][self._y_cord]

        # Jesli czlowiek nie jest podlaczony do respiratora, ruszy sie:
        if self.__resp == False:

            # Obiekt sie ruszy, jesli ma miejsce. Jesli bylby otoczony, nie ruszy sie:
            if super().neighbour(fields, xsize, ysize, self._x_cord, self._y_cord) == False:

                lastcell.change_obj_amount(-1, "Human", -1)
                super().where_to_move(xsize, ysize)
                cell = fields[self._x_move_to][self._y_move_to]

                # Jesli obiekt bedzie chcial sie ruszyc tam, gdzie nie ma miejsca, zmien kordynaty:
                while (cell.answer() == False):
                    super().where_to_move(xsize, ysize)  # Obiekt zmienia swoj ruch
                    cell = fields[self._x_move_to][self._y_move_to]

                # Ostateczne zmiany:
                self._x_cord = self._x_move_to
                self._y_cord = self._y_move_to
                cell.change_obj_amount(1, "Human", self._ID)

                return cell

            else:
                return lastcell

        else:
            return lastcell

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Obiekt wchodzi w mozliwe interakcje

    def interaction(self, cell, humans, viruses, doctors, respirators, vaccines, medicines):

        # Napotyka na innego czlowieka
        if cell.check_status()[1] > 1:

            # Jesli jestes zarazony, zaraz innego czlowieka
            if self.__infected == True:
                i = cell.check_ID()[0][1]
                self.infect_hum(humans[i], cell)

        # Napotyka na wirusa
        elif cell.check_status()[2] > 0:

            i = cell.check_ID()[1][0]

            # Jesli obiekt istnieje:
            if i != -1:

                # Zaraz czlowieka, jesli nie jest odporny:
                if self.__immunity == 0:
                    viruses[i].infect(self, cell)

                # Jesli czlowiek jest odporny, zniszcz wirusa:
                else:
                    viruses[i].destroy(cell)

        # Napotyka na lekarza
        elif cell.check_status()[3] > 0:
            i = cell.check_ID()[2][0]

            # Lecz czlowieka (jesli chory)
            if i != -1:
                doctors[i].heal(self)

        # Napotyka na respirator
        elif cell.check_status()[5] > 0:

            i = cell.check_ID()[4][0]

            # Jesli czlowiek jest chory, rozwaz podlaczenie do respiratora:
            if (i != -1 and self.__infected == True and self.__resp != True):
                self.__resp = respirators[i].change_status(True, self, self.__HP_points)

        # Napotyka na szczepionke
        elif cell.check_status()[6] > 0:

            i = cell.check_ID()[5][0]

            # Nabadz odpornosci dzieki szczepionce
            if i != -1:
                self.__immunity = vaccines[i].give_immunity(self.__immunity)
                vaccines[i].destroy(cell)

        # Napotyka na lekarstwo
        elif cell.check_status()[7] > 0:

            i = cell.check_ID()[6][0]

            if i != -1:

                # Dodaj 10 punktow HP
                self.__HP_points = medicines[i].heal(self.__HP_points)

                # Jesli czlowiek, dzieki lekarstwu odzyska pelnie zdrowia, nadaj mu drugotrwala odpornosc:
                if self.__infected == True and self.__HP_points == 100:
                    self.__infected = False
                    self.__immunity = 30

                medicines[i].destroy(cell)

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Funkcja obniza HP czlowieka w zaleznosci od wieku

    def reduce_health(self, cell):

        # Jesli czlowiek jest chory, nie jest odporny i nie jest podlaczony do respiratora, obniz jego punkty HP (w zaleznosci od wieku)
        if self.__immunity == 0 and self.__resp == False and self.__infected == True:

            reduce = 3
            expected_age = 0

            while reduce <= 9:
                if self.__age >= expected_age and self.__age <= expected_age + 25:

                    # Jesli czlowiek dalej zyje po obnizeniu puktow HP:
                    if self.__HP_points > reduce:
                        self.__HP_points -= reduce
                        break

                    # Jesli finalnie umrze:
                    else:
                        self.__HP_points = 0
                        self.kill(cell)
                        Human.__amount -= 1
                        cell.change_obj_amount(-1, "Human", -1)
                        break
                reduce += 2
                expected_age += 25

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Funkcja zaraza wybranego czlowieka, jesli czlowiek jest odporny, wirus zostaje unicestwiony

    def infect_hum(self, human, cell, virus = None):

        # Czlowiek zaraz czlowieka
        if human.__immunity == 0:
            human.__infected = True

        # Wirus zaraza czlowieka
        elif virus != None:

            if cell.check_ID()[1][0] >= 0:
                virus.destroy(cell)

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Funkcja przywraca czlowiekowi w pelni zdrowie

    def full_restore_health(self, resp_call):

        # Kiedy czlowiek jest zwyczajnie leczony:
        if resp_call == False:

            if self.__HP_points < 100 and self.__infected == True:
                self.__infected = False
                self.__HP_points = 100
                self.__immunity = 30

        # Kiedy czlowiek jest odlaczany od respiratora:
        else:
            self.__infected = False
            self.__HP_points = 100
            self.__immunity = 30 ###
            self.__resp = False

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Funkcja nadzoruje czas trwania chwilowej odpornosci

    def decrease_immunity_time(self):
        if self.__immunity > 0:
            self.__immunity -= 1

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Funkcja usmierca obiekt ludzki

    def kill(self, fields):
        self._x_cord = -1
        self._y_cord = -1
        self.__amount -= 1
        self.__infected = False
        self.__resp = False
        fields.change_obj_amount(-1, "Human", -1)

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Funkcja zwraca informacje czy dany czlowiek jest chory

    def human_infected(self, when):
        if when == "current":
            if self._x_cord != -1:
                if self.__infected == True:
                    return 1
                elif self.__infected == False:
                    return 0
            else:
                return 0

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Funkcja zwraca informacje czy dany czlowiek jest odporny

    def human_current_immuned(self):

        if self._x_cord != -1:
            if self.__immunity > 0:
                return 1
            else:
                return 0
        else:
            return 0

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Funkcja prezentuje karte pacjenta (ktora moze wyswietlic uzytkownik)

    def chart(self):

        print("\n")
        print("JAN KOWALSKI: " + str(self._ID))

        if self._x_cord == -1 and self._y_cord == -1:
            print("Obiekt nie żyje :( Pomódlmy się za jego dusze, Amen", end='')
            print("\n")
        else:
            print("Wsp x: ", end='')
            print(self._y_cord)
            print("Wsp y: ", end='')
            print(self._x_cord)
            print("Wiek: ", end='')
            print(self.__age)
            print("Zainfekowany: ", end='')
            print(self.__infected)
            print("Punkty HP: ", end='')
            print(self.__HP_points)
            print("Czas odpornosci: ", end='')
            print(self.__immunity)
            print("Podlaczony do respiratora: ", end='')
            print(self.__resp)
            print("\n")

        plik = open("Dane.txt", "a", encoding="utf-8")

        if plik.writable():
            plik.write("\n\n")
            plik.write("    JAN KOWALSKI: " + str(self._ID)+"\n")
            if self._x_cord == -1 and self._y_cord == -1:
                plik.write("    Obiekt nie żyje :( Pomódlmy się za jego dusze, Amen\n")
            else:
                plik.write("    Wsp x: "+ str(self._y_cord) +"\n")
                plik.write("    Wsp y: "+ str(self._x_cord) +"\n")
                plik.write("    Wiek: "+ str(self.__age) +"\n")
                plik.write("    Zainfekowany: "+ str(self.__infected) +"\n")
                plik.write("    Punkty HP: "+ str(self.__HP_points) +"\n")
                plik.write("    Czas odpornosci: "+ str(self.__immunity) +"\n")
                plik.write("    Podlaczony do respiratora: "+ str(self.__resp) +"\n\n")

        plik.close()

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Zwraca ilosc obiektow

    @staticmethod
    def check_amount():
        return Human.__amount