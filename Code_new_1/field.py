class Field:

    __fresh = True # atrybut informujacy czy kratki dopiero co powstaja, potrzebny do uwzglednienia maksymalnej liczby
                   # obiektow znajdujacych sie w kratce
    __amount = 0

    # -------------------------------------------------------------------------
    # Zainicjowanie kratki- jej ID w postaci wspolrzednych, inicjujemy tez poczatkowa liczbe obiektow
    # Na niej sie znajdujacych- 0, czyli pusta kratka
    def __init__(self, xcord, ycord, xsize, ysize):
        self.__xcord = xcord
        self.__ycord = ycord
        self.__status = [0, 0, 0, 0, 0, 0, 0, 0] #zmienna przechowujaca status obiektu, pierwsza cyfra - liczba obiektow na kratce
        self.__ID = [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]] #przechowuje id obiektow
        self.__amount += 1
        if self.__amount == xsize * ysize:
            __fresh = False

    # -------------------------------------------------------------------------
    # Funkcja zmieniajaca status kratki - zmienia wartosc ogolnej liczby obiektow znajdujacej sie na niej
    def change_obj_amount(self, sign, type, ID): #Kazdy obiekt ma swoj ID - indeks

        # sign zawiera informację o tym czy zwiększyć czy zmniejszyć, type to nowy atrubut, ktory bedzie zawieral kazdy obiekt
        # na planszy i bedzie ew. atrybutem identyfikujacym obiekt (kratka musi wiedziec jaki obiekt na nia wchodzi)

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
    # Funkcja ktora zwraca aktualny status kratki (zwroci liste licznikow)
    def check_status(self):

        # for i in range(1, 7): # ??????
        #     if self.__status[i] > 0:
        #         self.__status.append(1)
        #     else:
        #         self.__status.append(0)

        return self.__status

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
    # funkcja pomocnicza dla change_obj_amount()
    def __ifobj(self, sign, ID, nr):
        self.__status[nr] += sign
        if self.__ID[1][0] >= 0:
            self.__ID[1][1] = ID
        else:
            self.__ID[1][0] = ID

    # -------------------------------------------------------------------------
    # Funkcja ktora zwroci dokladnie jakie obiekty sie na niej znajduja (ID tych obiektow)
    def check_id(self):
        return self.__ID

    # -------------------------------------------------------------------------
    # Metoda zmieniajaca atrybut kratek "fresh"
    # @staticmethod
    # def fresh_mod(self, fresh_change):
    #     self.__fresh = fresh_change

