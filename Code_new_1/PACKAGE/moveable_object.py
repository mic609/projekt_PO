from abc import ABC, abstractmethod
import random

class MoveableObject(ABC):

    def __init__(self, x, y, ID):
        self._x_cord = - 1
        self._y_cord = - 1
        self.change_cord(x, y)
        self._ID = ID
        self._x_move_to = -1  # ?????????????????????????????????
        self._y_move_to = -1 # ?????????????????????????????????

    # -------------------------------------------------------------------------
    # Nadzoruje proces ruchu obiektu
    @abstractmethod
    def move(self, fields, xsize, ysize):
        pass

    # -------------------------------------------------------------------------
    # Dostepne interakcje jakie obiekt wykonuje
    @abstractmethod
    def interaction(self, cell, humans, viruses, doctors, respirators, vaccines, medicines):
        pass

    # -------------------------------------------------------------------------
    # Zmiana wspolrzednych obiektu. UWAGA! Metoda wywolywana tylko przy inicjalizacji programu
    def change_cord(self, x, y):
        # print("WSPOLRZEDNE przed: ")
        # print(self._x_cord)
        # print(self._y_cord)

        self._x_cord = random.randint(0, x - 1)
        self._y_cord = random.randint(0, y - 1)

        # print("WSPOLRZEDNE po: ")
        # print(self._x_cord)
        # print(self._y_cord)
        # print(x)
        # print(y)

    # -------------------------------------------------------------------------
    # Metoda losuje, gdzie dany obiekt ma sie ruszyc
    def where_to_move(self, xsize, ysize):


        self._x_move_to = random.choice([self._x_cord - 1, self._x_cord, self._x_cord + 1])
        while self._x_move_to < 0 or self._x_move_to > xsize - 1:
            self._x_move_to = random.choice([self._x_cord - 1, self._x_cord, self._x_cord + 1])

        self._y_move_to = random.choice([self._y_cord - 1, self._y_cord, self._y_cord + 1])
        while self._y_move_to < 0 or self._y_move_to > ysize - 1:
            self._y_move_to = random.choice([self._y_cord - 1, self._y_cord, self._y_cord + 1])



        while self._x_move_to == self._x_cord and self._y_move_to == self._y_cord:
            # print("WSPOLRZEDNE 1: " + str(self._x_move_to) + " " + str(self._y_move_to))
            # print("XCORD YCORD: " + str(self._x_cord) + " " + str(self._y_cord))
            self._x_move_to = random.choice([self._x_cord - 1, self._x_cord, self._x_cord + 1])
            while self._x_move_to < 0 or self._x_move_to > xsize - 1:
                self._x_move_to = random.choice([self._x_cord - 1, self._x_cord, self._x_cord + 1])

            self._y_move_to = random.choice([self._y_cord - 1, self._y_cord, self._y_cord + 1])
            while self._y_move_to < 0 or self._y_move_to > ysize - 1:
                self._y_move_to = random.choice([self._y_cord - 1, self._y_cord, self._y_cord + 1])

            # print("CZLOWIEK")
            # print("WSPOLRZEDNE 2: " + str(self._x_move_to) +" "+ str(self._y_move_to))
            # print("XCORD YCORD: " + str(self._x_cord) + " " + str(self._y_cord))

    # -------------------------------------------------------------------------
            # METODA NEIGHBOUR (CHYBA W MOVEABLE_OBJECT)

    def neighbour(self, fields, xsize, ysize, x, y):

        n = -1
        m = -1
        critic_count = 0

        petla = 0

        while n <= 1:
            while m <= 1:
                if x + n >= 0 and x + n < xsize and y + m >=0 and y + m < ysize:
                    if not(n == 0 and m == 0):

                        # print("SKURWIALA: ")
                        # print(fields[self._x_cord + n][self._y_cord + m].check_status())

                        if fields[x + n][y + m].check_status()[0] < 2:
                            critic_count += 1
                        petla += 1
                m += 1
            n += 1
            m = -1
        # print("DLA X I Y: " + str(x)+" "+str(y))
        # print("CRITIC: " + str(critic_count))

        if critic_count >= 1:
            # print("DOBRZE!!!!!!")
            return False
        else:
            # print("ZLE!!!!!!")
            return True


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

    def check_id(self):
        return self._ID