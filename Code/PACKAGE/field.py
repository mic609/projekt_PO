# ILOSC METOD: 8 (w tym konstruktor)

class Field:

    __fresh = True # atrybut informujacy czy kratki dopiero co powstaja, potrzebny do uwzglednienia maksymalnej liczby
                   # obiektow znajdujacych sie w kratce
    __amount = 0

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Zainicjowanie kratki- jej ID w postaci wspolrzednych, inicjujemy tez poczatkowa liczbe obiektow
    # Na niej sie znajdujacych- 0, czyli pusta kratka

    def __init__(self, xcord, ycord):
        self.xcord = xcord
        self.ycord = ycord

        # self.__status- kolejno liczba:
        # [0: wszystkich obiektow w kratce, 1: ludzi, 2: wirusow, 3: lekarzy, 4: chemikow, 5: respiratorow
        # 6: szczepionek, 7: lekarstw]
        self.__status = [0, 0, 0, 0, 0, 0, 0, 0]

        # self.__ID- kolejno ID: [0: ludzi, 1: wirusow, 2: lekarzy, 3: chemikow, 4: respiratorow, 5: szczepionek, 6: lekarstw]
        # -1 to wartosc domyslna oznaczajaca brak ID
        self.__ID = [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]] #przechowuje id obiektow

        Field.__amount += 1

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Funkcja zmieniajaca status kratki - zmienia wartosc ogolnej liczby obiektow znajdujacej sie na niej

    # sign zawiera informację o tym czy zwiększyć czy zmniejszyć, type informuje o typie obiektu, ID- jaki konkretny
    # obiekt wchodzi na kratke
    # ID - indeks
    def change_obj_amount(self, sign, type, ID):

        # Zmien liczbe ogolnej ilosci obiektow
        if sign == -1 and self.__status[0]> 0:
            self.__status[0] += sign
        elif sign == 1:
            self.__status[0] += sign

        # Zmien liczbe konkretnych obiektow
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
    # -------------------------------------------------------------------------
    # Metoda pomocnicza dla change_obj_amount(), zapisuje ilosc konkretnych obiektow

    def __ifobj(self, sign, ID, nr):

        # Zmien liczbe obiektow
        if sign == -1 and self.__status[nr]> 0:
            self.__status[nr] += sign
        elif sign == -1 and self.__status[nr] == 0:
            self.__status[nr] = 0
        else:
            self.__status[nr] += sign

        # Przypisz do kratki ID obiektow, ktore na nie wchodza:

        # Dodajemy ID
        if sign == 1:
            if self.__ID[nr-1][0] >= 0:
                self.__ID[nr-1][1] = ID
            else:
                self.__ID[nr-1][0] = ID
        # Usuwamy ID
        else:
            if self.__ID[nr-1][1] == self.__ID:
                self.__ID[nr-1][1] = ID
            else:
                self.__ID[nr-1][0] = ID

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Zwracaja informacje czy mozna na dana kratke wejsc
    # self.__fresh informuje o stanie kratki (czy moga sie na niej znajdywac max 1 lub 2 obiekty)

    def answer_first(self):

        if self.__fresh is True:
            if self.__status[0] > 1:
                return False
            else:
                return True

    def answer(self):

        if self.__fresh is True:
            if self.__status[0] >= 1:
                return False
            else:
                return True
        else:
            if self.__status[0] == 2:
                return False
            else:
                return True

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Funkcja ktora zwraca aktualny status kratki (zwroci liste licznikow)

    def check_status(self):
        return self.__status

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Funkcja ktora zwroci dokladnie jakie obiekty sie na niej znajduja (ID tych obiektow)

    def check_ID(self):
        return self.__ID

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Zmienia status kratek "fresh" z true na false

    @staticmethod
    def fresh_change():
        Field.__fresh = False