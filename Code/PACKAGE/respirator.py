import random
from PACKAGE.field import Field

# ILOSC METOD: 8 (w tym konstruktor)

class Respirator:

    __amount = 0

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Konstruktor

    def __init__(self, respirator, fields, x, y, ID):
        self.__x_cord = random.randint(0, x - 1)
        self.__y_cord = random.randint(0, y - 1)
        self.__on_respirator = respirator
        self.__ID = ID
        Respirator.__amount += 1
        fields[self.__x_cord][self.__y_cord].change_obj_amount(1, "Respirator", self.__ID)

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Metoda, ktora zmienia status on/off respiratora i ktora dodatkowo po wylaczeniu przywraca
    # czlowiekowi pelnie zdrowia

    def change_status(self, on_off, human, health = 10000):

        # Jesli czlowiek zostaje odlaczony od respiratora
        if on_off == False:
                self.__on_respirator = on_off

                human.full_restore_health(True)
                return self.__on_respirator

        # Jesli czlowiek zostaje podlaczony do respiratora
        elif health <= 30:
            self.__on_respirator = on_off
            return self.__on_respirator

        else:
            return self.__on_respirator

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Zmiena wspolrzedne respiratora (gdy to potrzebne)

    def change_cord(self, x, y):
        self.__x_cord = random.randint(0, x - 1)
        self.__y_cord = random.randint(0, y - 1)

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Zwraca status respiratora on/off

    def check_status(self):
        if self.__on_respirator == True:
            return 1
        else:
            return 0

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------

    def x_cor(self):
        return self.__x_cord

    def y_cor(self):
        return self.__y_cord

    def check_id(self):
        return self.__ID

    @staticmethod
    def check_amount():
        return Respirator.__amount
