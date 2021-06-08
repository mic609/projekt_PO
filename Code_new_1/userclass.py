from PACKAGE import Board
from PACKAGE.board import Virus
from PACKAGE.board import Human

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
        while Userclass.__fullamount >= int(0.55 * Userclass.__xsize * Userclass.__ysize):
            print("Za duzo obiektow! Wprowadz Wartości jeszcze raz: ")
            Userclass.__set_numbers()

    # -------------------------------------------------------------------------
    # Sprawdzamy czy dane podane przez uzytkownika spelniaja standard programu
    @staticmethod
    def __set_cycle(mode):
        right = True

        while right:

            try:

                decision = int(input())

                if mode == 0:
                    while decision < -1:
                        print("Za mala liczba wprowadz jeszcze raz!: ")
                        decision = int(input())
                else:
                    while decision < -2:
                        print("Za mala liczba wprowadz jeszcze raz!: ")
                        decision = int(input())

                return decision

            except ValueError:
                right = True
                print("Wprowadzone wartosi musza byc liczbami calkowitymi!")

    @staticmethod
    def main():
        Userclass.__set_numbers()
        Userclass.__check_if_good()
        plansza = Board(Userclass.__xsize, Userclass.__ysize, Userclass.__givehuman, Userclass.__givevirus, Userclass.__givedoctor, Userclass.__givechemist, Userclass.__giverespirator)
        plansza.start()

        print("Ile cykli? (\"-1\" - wynik symulacji; \"0\" - zakoncz program; \">0\" - ilość cykli): ")
        decision = Userclass.__set_cycle(0)

        while decision != 0:
            while decision != 0:
                while decision:
                    if decision == -1:
                        while Virus.check_amount() > 0 and Human.check_amount() > 0:
                            plansza.cycle()
                        break
                    plansza.cycle()
                    decision -= 1

                plansza.show_cycle()
                print("Pokazac reprezentacje graficzna? (\"-2\" - tak): ")
                decision = Userclass.__set_cycle(1)

                if decision == -2:
                    plansza.show_graphic_representation()

                print("Ile cykli? (\"-1\" - wynik symulacji; \"0\" - zakoncz program; \">0\" - ilość cykli): ")
                decision = Userclass.__set_cycle(0)

Userclass.main()