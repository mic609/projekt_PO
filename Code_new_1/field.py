# CHECKED

class Field:

    __fresh = True # atrybut informujacy czy kratki dopiero co powstaja, potrzebny do uwzglednienia maksymalnej liczby
                   # obiektow znajdujacych sie w kratce
    __amount = 0

    # -------------------------------------------------------------------------
    # Zainicjowanie kratki- jej ID w postaci wspolrzednych, inicjujemy tez poczatkowa liczbe obiektow
    # Na niej sie znajdujacych- 0, czyli pusta kratka

    def __init__(self, xcord, ycord):
        self.__xcord = xcord
        self.__ycord = ycord

        # self.__status- kolejno liczba:
        # wszystkich obiektow w kratce, ludzi, wirusow, lekarzy, chemikow, respiratorow, szczepionek, lekarstw
        self.__status = [0, 0, 0, 0, 0, 0, 0, 0]

        # self.__ID- kolejno ID: ludzi, wirusow, lekarzy, chemikow, respiratorow, szczepionek, lekarstw
        # -1 to wartosc domyslna oznaczajaca brak ID
        self.__ID = [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]] #przechowuje id obiektow

        self.__amount += 1

    # -------------------------------------------------------------------------
    # Funkcja zmieniajaca status kratki - zmienia wartosc ogolnej liczby obiektow znajdujacej sie na niej

    def change_obj_amount(self, sign, type, ID): # kazdy obiekt ma swoj ID - indeks

        # sign zawiera informację o tym czy zwiększyć czy zmniejszyć, type informuje o typie obiektu, ID- jaki konkretny
        # obiekt wchodzi na kratke

        if sign == -1 and self.__status[0]> 0:
            self.__status[0] += sign
        elif sign == 1 and self.__status[0] < 2:
            self.__status[0] += sign

        if type == "Human":
            self.__ifobj(sign, ID, 1)
        elif type == "Virus":
            self.__ifobj(sign, ID, 2)
        elif type == "Doctor":
            self.__ifobj(sign, ID, 3)
        elif type == "Chemist":
            self.__ifobj(sign, ID, 4)
        elif type == "Respirator":
            self.__ifobj(sign, ID, 5)
        elif type == "Vaccine":
            self.__ifobj(sign, ID, 6)
        elif type == "Medicine":
            self.__ifobj(sign, ID, 7)

    # -------------------------------------------------------------------------
    # funkcja pomocnicza dla change_obj_amount(), zapisuje ilosc konkretnych obiektow

    def __ifobj(self, sign, ID, nr):
        self.__status[nr] += sign

        if sign == 1: # Dodajemy ID
            if self.__ID[1][0] >= 0:
                self.__ID[1][1] = ID
            else:
                self.__ID[1][0] = ID
        else: # Usuwamy ID
            if self.__ID[1][1] == self.__ID:
                self.__ID[1][1] = ID
            else:
                self.__ID[1][0] = ID

    # -------------------------------------------------------------------------
    # Zwraca informacje czy mozna na dana kratke wejsc

    def answer(self):  # dawna funkcja- def return_no_place(self):
        if self.__fresh is True:
            if self.__status[0] == 1:
                return False  # Funkcja zwraca tu jedynie wartosc domyslna, ktora nie daje efektu???
        else:
            if self.__status[0] == 2:
                return False

    # -------------------------------------------------------------------------
    # Funkcja ktora zwraca aktualny status kratki (zwroci liste licznikow)

    def check_status(self):
        return self.__status

    # -------------------------------------------------------------------------
    # Funkcja ktora zwroci dokladnie jakie obiekty sie na niej znajduja (ID tych obiektow)

    def check_ID(self):
        return self.__ID

    # -------------------------------------------------------------------------
    @staticmethod
    def fresh_change():
        Field.__fresh = False
