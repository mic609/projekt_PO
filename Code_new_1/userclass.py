# CHECKED

from board import Board

class Userclass:

    __xsize = 0
    __ysize = 0
    __fullamount = 0
    # give oznacza ile obiektow chce uzytkownik
    __givehuman = 0
    __givedoctor = 0
    __givechemist = 0
    __givevirus = 0
    __giverespirator = 0

    # -------------------------------------------------------------------------
    # Uzytkownik ustawia wielkosc planszy i ilosc poszczegolnych obiektow
    @staticmethod
    def __set_numbers():

        try:
            print("Podaj wartość x: ")
            Userclass.__xsize = int(input())
            print("Podaj wartość y: ")
            Userclass.__ysize = int(input())
            print("Podaj ilosc ludzi: ")
            Userclass.__givehuman = int(input())
            print("Podaj ilosc wirusow: ")
            Userclass.__givevirus = int(input())
            print("Podaj ilosc lekarzy: ")
            Userclass.__givedoctor = int(input())
            print("Podaj ilosc chemikow: ")
            Userclass.__givechemist = int(input())
            print("Podaj ilosc respiratorow: ")
            Userclass.__giverespirator = int(input())
        except ValueError:
            print("Wprowadzone wartosi musza byc liczbami calkowitymi!")

    # -------------------------------------------------------------------------
    # Sprawdzamy czy dane podane przez uzytkownika spelniaja standard programu
    @staticmethod
    def __check_if_good():
        Userclass.__fullamount = Userclass.__givehuman + Userclass.__givevirus + Userclass.__givedoctor + Userclass.__givechemist + Userclass.__giverespirator
        while Userclass.__fullamount >= int(0.7 * Userclass.__xsize * Userclass.__ysize):
            print("Za duzo obiektow! Wprowadz Wartości jeszcze raz: ")
            Userclass.__set_numbers()

    @staticmethod
    def main():
        Userclass.__set_numbers()
        Userclass.__check_if_good()
        plansza = Board(Userclass.__xsize, Userclass.__ysize, Userclass.__givehuman, Userclass.__givevirus, Userclass.__givedoctor, Userclass.__givechemist, Userclass.__giverespirator)
        print("breakpoint")
        plansza.start()

        decision = "y"

        while decision == "y":
            print("acihf")
            plansza.cycle()
            print("Kontynuować symulację? y/n: ")
            decision = input()

Userclass.main()