from Board import Board

class Userclass: #(moze byc mainem, ale nie wiem teraz)

    __xsize = 0
    __ysize = 0
    __fullamount = 0
    __givehuman = 0 # give oznacza ile obiektow chce uzytkownik
    __givedoctor = 0
    __givechemist = 0
    __givevirus = 0
    __giverespirator = 0

    # -------------------------------------------------------------------------
    # Uzytkownik ustawia wielkosc planszy i ilosc poszczegolnych obiektow
    @staticmethod
    def __set_numbers(self):

        try:
            print("Podaj wartość x: ")
            self.__xsize = int(input())
            print("Podaj wartość y: ")
            self.__ysize = int(input())
            print("Podaj ilosc ludzi: ")
            self.__givehuman = int(input())
            print("Podaj ilosc wirusow: ")
            self.__givevirus = int(input())
            print("Podaj ilosc lekarzy: ")
            self.__givedoctor = int(input())
            print("Podaj ilosc chemikow: ")
            self.__givechemist = int(input())
            print("Podaj ilosc respiratorow: ")
            self.__giverespirator = int(input())
        except ValueError:
            print("Wprowadzone wartosi musza byc liczbami calkowitymi!")

    # -------------------------------------------------------------------------
    # Sprawdzamy czy dane podane przez uzytkownika spelniaja standard programu
    @staticmethod
    def __check_if_good(self):
        self.__fullamount = self.__givehuman + self.__givevirus + self.__givedoctor + self.__givechemist + self.__giverespirator
        while self.__fullamount >= int(0.7 * self.__xsize * self.__ysize):
            print("Za duzo obiektow! Wprowadz Wartości jeszcze raz: ")
            self.__set_numbers()

    # -------------------------------------------------------------------------
    # Po upewnieniu sie ze wszystko w porzadku, tworzymy plansze! Tuz po stworzeniu planszy, przyjmujemy, ze
    # poczatkowa liczba obiektow moze wynosic na kazdej kratce maksymalnie 1
    @staticmethod
    def __start(self):
        plansza = Board(self.__xsize, self.__ysize, self.__givehuman, self.__givevirus, self.__givedoctor, self.__givechemist, self.__giverespirator)
