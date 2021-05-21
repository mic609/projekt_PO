import random
from field import Field

class Respirator():

    __amount = 0

    def __init__(self, respirator, fields, x, y, ID):
        self.__x_cord = random.randint(0, x - 1)
        self.__y_cord = random.randint(0, y - 1)
        self.__on_respirator = respirator
        self.__ID = ID
        self.__amount += 1
        fields[self.__x_cord][self.__y_cord].change_obj_amount(1, "Respirator", self.__ID)

    # -------------------------------------------------------------------------
    # Metoda, ktora zmienia status on/off respiratora i ktora dodatkowo po wylaczeniu przywraca
    # czlowiekowi pelnie zdrowia

    def change_status(self, on_off, human, health = 10000):

        if health <=15:

            self.__on_respirator = on_off

        if on_off == False: # Jesli czlowiek zostaje odlaczony od respiratora
                human.full_restore_health(True)

    def change_cord(self, x, y):
        self.__x_cord = random.randint(0, x - 1)
        self.__y_cord = random.randint(0, y - 1)

    # -------------------------------------------------------------------------
    def x_cord(self):
        return self.__x_cord

    def y_cord(self):
        return self.__y_cord
