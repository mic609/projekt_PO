import random

class Respirator():

    __amount = 0

    def __init__(self, respirator, x, y, ID, fields):
        self.__x_cord = random.randint(0, x - 1)
        self.__y_cord = random.randint(0, y - 1)
        self.__on_respirator = respirator
        self.__ID = ID
        self.__amount += 1
        fields.change_obj_amount(1, "Respirator", self.__ID)

    # -------------------------------------------------------------------------
    # Metoda, ktora zmienia status on/off respiratora i ktora dodatkowo po wylaczeniu przywraca
    # czlowiekowi pelnie zdrowia

    def change_status(self, on_off, human):
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