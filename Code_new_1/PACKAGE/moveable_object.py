from abc import ABC, abstractmethod
import random

# ILOSC METOD: 11 (w tym konstruktor i 5 metod zwracajacych)

class MoveableObject(ABC):

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Inicjujemy wsporzedne obiektu poruszajacego sie, okreslamy ID

    def __init__(self, x, y, ID):
        self._x_cord = - 1
        self._y_cord = - 1
        self.change_cord(x, y)
        self._ID = ID
        self._x_move_to = -1
        self._y_move_to = -1

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Nadzoruje proces ruchu obiektu

    @abstractmethod
    def move(self, fields, xsize, ysize):
        pass

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Dostepne interakcje jakie obiekt wykonuje

    @abstractmethod
    def interaction(self, cell, humans, viruses, doctors, respirators, vaccines, medicines):
        pass

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Zmiana wspolrzednych obiektu. UWAGA! Metoda wywolywana tylko przy inicjalizacji programu

    def change_cord(self, x, y):

        self._x_cord = random.randint(0, x - 1)
        self._y_cord = random.randint(0, y - 1)

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Metoda losuje, gdzie dany obiekt ma sie ruszyc

    def where_to_move(self, xsize, ysize):


        self._x_move_to = random.choice([self._x_cord - 1, self._x_cord, self._x_cord + 1])

        # Jesli wspolrzedna wychodzi poza zakres, powtorz proces
        while self._x_move_to < 0 or self._x_move_to > xsize - 1:
            self._x_move_to = random.choice([self._x_cord - 1, self._x_cord, self._x_cord + 1])

        self._y_move_to = random.choice([self._y_cord - 1, self._y_cord, self._y_cord + 1])

        # Jesli wspolrzedna wychodzi poza zakres, powtorz proces
        while self._y_move_to < 0 or self._y_move_to > ysize - 1:
            self._y_move_to = random.choice([self._y_cord - 1, self._y_cord, self._y_cord + 1])


        # Wylosowane wspolrzedne na ktore obiekt musi sie ruszyc nie moga byc takie same jak wspolrzedne
        # okreslajace jego wczesniejsza pozycje. Jesli jednak tak jest procesy wyzej zostana powtorzone
        while self._x_move_to == self._x_cord and self._y_move_to == self._y_cord:

            self._x_move_to = random.choice([self._x_cord - 1, self._x_cord, self._x_cord + 1])
            while self._x_move_to < 0 or self._x_move_to > xsize - 1:
                self._x_move_to = random.choice([self._x_cord - 1, self._x_cord, self._x_cord + 1])

            self._y_move_to = random.choice([self._y_cord - 1, self._y_cord, self._y_cord + 1])
            while self._y_move_to < 0 or self._y_move_to > ysize - 1:
                self._y_move_to = random.choice([self._y_cord - 1, self._y_cord, self._y_cord + 1])

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Metoda sprawdza, czy dane obiekt nie jest otoczony w taki sposob, ze nie ma calkowicie
    # jak sie ruszyc

    def neighbour(self, fields, xsize, ysize, x, y):

        n = -1
        m = -1

        # critic_count liczy ile kratek wokol obiektu jest wolnych (moze na nie wejsc)
        critic_count = 0

        petla = 0

        while n <= 1:
            while m <= 1:
                if x + n >= 0 and x + n < xsize and y + m >=0 and y + m < ysize:
                    if not(n == 0 and m == 0):

                        if fields[x + n][y + m].check_status()[0] < 2:
                            critic_count += 1
                        petla += 1
                m += 1
            n += 1
            m = -1

        if critic_count >= 1:
            return False
        else:
            return True


    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Metody zwracajace

    def x_cor(self):
        return self._x_cord

    def y_cor(self):
        return self._y_cord

    def x_move(self):
        return self._x_move_to

    def y_move(self):
        return self._y_move_to

    def check_id(self):
        return self._ID