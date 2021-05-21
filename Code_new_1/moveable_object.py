from abc import ABC, abstractmethod
import random

class MoveableObject(ABC):

    def __init__(self, x, y, ID):
        self._x_cord = x - 1
        self._y_cord = y - 1
        self._x_range = x
        self._y_range = y
        self.change_cord(self._x_cord, self._y_cord)
        self._ID = ID
        # self._x_move_to = -1
        # self._y_move_to = -1

    # -------------------------------------------------------------------------
    # Nadzoruje proces ruchu obiektu
    @abstractmethod
    def move(self, fields):
        pass

    # -------------------------------------------------------------------------
    # Dostepne interakcje jakie obiekt wykonuje
    @abstractmethod
    def interaction(self, cell, humans, viruses, doctors, respirators, vaccines, medicines):
        pass

    # -------------------------------------------------------------------------
    # Zmiana wspolrzednych obiektu. UWAGA! Metoda wywolywana tylko przy inicjalizacji programu
    def change_cord(self, x, y):
        while True:
            self._x_cord = random.randint(0, x - 1)
            self._y_cord = random.randint(0, y - 1)
            if 0 < self._x_cord < self._x_range and 0 < self._y_cord < self._y_range:
                break

    # -------------------------------------------------------------------------
    # Metoda losuje, gdzie dany obiekt ma sie ruszyc
    def where_to_move(self):

        self._x_move_to = random.choice([self._x_cord - 1, self._x_cord, self._x_cord + 1])
        self._y_move_to = random.choice([self._y_cord - 1, self._y_cord, self._y_cord + 1])


    # -------------------------------------------------------------------------
    def x_cor(self):
        return self._x_cord
    def y_cor(self):
        return self._y_cord

    ############################################

    def x_move(self):
        return self._x_move_to

    def y_move(self):
        return self._y_move_to
