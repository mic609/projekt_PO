from PACKAGE import Board
from PACKAGE.board import Virus
from PACKAGE.board import Human
import os

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
    # -------------------------------------------------------------------------
    # Uzytkownik ustawia wielkosc planszy i ilosc poszczegolnych obiektow

    @staticmethod
    def __set_numbers():

        right = True # zmienna pomocnicza

        while right:
            try:
                print("Podaj wartość x: ")
                Userclass.__ysize = int(input())
                print("Podaj wartość y: ")
                Userclass.__xsize = int(input())
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

                # Sprawdz czy podane wartosci sa dopuszczalne
                Userclass.__check_if_good()

                right = False

                plik = open("Dane.txt", "a", encoding="utf-8")

                if plik.writable():
                    plik.write("---------------------------------------------------------\n")
                    plik.write("---------------------------------------------------------\n")
                    plik.write("---------------------------------------------------------\n\n")
                    plik.write("Wartość x: " + str(Userclass.__ysize)+ "\n")
                    plik.write("Wartość y: "+ str(Userclass.__xsize)+ "\n")
                    plik.write("Ilość ludzi: "+ str(Userclass.__givehuman)+ "\n")
                    plik.write("Ilość wirusow: "+ str(Userclass.__givevirus)+ "\n")
                    plik.write("Ilość lekarzy: "+ str(Userclass.__givedoctor)+ "\n")
                    plik.write("Ilość chemikow: "+ str(Userclass.__givechemist)+ "\n")
                    plik.write("Ilość respiratorow: "+ str(Userclass.__giverespirator)+ "\n\n")

                plik.close()

            except ValueError:
                right = True
                print("Wprowadzone wartosi musza byc liczbami calkowitymi!")

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Sprawdzamy czy dane podane przez uzytkownika spelniaja standard programu

    @staticmethod
    def __check_if_good():
        Userclass.__fullamount = Userclass.__givehuman + Userclass.__givevirus + Userclass.__givedoctor + Userclass.__givechemist + Userclass.__giverespirator
        while Userclass.__fullamount >= int(0.55 * Userclass.__xsize * Userclass.__ysize):
            os.system('cls')
            print("Za duzo obiektow! Wprowadz Wartości jeszcze raz:\n")
            Userclass.__set_numbers()
            Userclass.__fullamount = Userclass.__givehuman + Userclass.__givevirus + Userclass.__givedoctor + Userclass.__givechemist + Userclass.__giverespirator

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Sprawdzamy czy dane podawane przez uzytkownika sa poprawne

    @staticmethod
    def __set_cycle(mode):
        right = True

        while right:

            if mode == 0:
                try:

                    decision = int(input())

                    while decision < -1:
                            print("\nZa mała liczba, wprowadź jeszcze raz: ")
                            decision = int(input())

                    return decision

                except ValueError:
                    right = True
                    print("\nWprowadzone wartosi musza byc liczbami calkowitymi! Wprowadz jeszcze raz: ", end='')

            elif mode == 1:
                decision = input()
                return decision

            else:
                try:
                    decision = int(input())
                    return decision

                except ValueError:
                    right = True
                    print("\nWprowadzone wartosci musza byc liczbami calkowitymi! Wprowadz jeszcze raz: ", end='')

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Metoda main

    @staticmethod
    def main():
        Userclass.__set_numbers()
        plansza = Board(Userclass.__xsize, Userclass.__ysize, Userclass.__givehuman, Userclass.__givevirus, Userclass.__givedoctor, Userclass.__givechemist, Userclass.__giverespirator)
        plansza.start()

        print("Ile cykli? (\"-1\" - wynik symulacji; \"0\" - zakoncz program; \">0\" - ilość cykli): ", end = '')
        decision = Userclass.__set_cycle(0)
        print("Trwa praca programu...")

        hum_overall = Human.check_amount()
        dzien = 0

        while decision != 0:
            while decision != 0:
                while decision:
                    if decision == -1:
                        while Virus.check_amount() > 0 and Human.check_amount() > 0:
                            plansza.cycle()
                            dzien += 1
                        break
                    plansza.cycle()
                    dzien += 1
                    decision -= 1

                plansza.show_cycle(dzien)

                print("\n")
                print("Pokazac reprezentacje graficzna? (\"y\" - tak; != \"y\" - nie): ", end= '')
                decision = Userclass.__set_cycle(1)
                if decision == 'y':
                    print("\n")
                    plansza.show_graphic_representation()
                    print("\n")

                print("\n")
                print("Pokazac karte pacjenta? (\">=0\" - ID pacjenta; != \"<0\" - nie): ", end='')
                decision = Userclass.__set_cycle(2)
                while decision >= 0:

                    while decision >= hum_overall or decision < 0:
                        print("\nZle dane! Wpisz jeszcze raz: (\">=0\" - ID pacjenta; != \"<0\" - nie): ", end='')
                        decision = Userclass.__set_cycle(2)
                    plansza.chart(decision)

                    print("Pokazac karte pacjenta? (\">=0\" - ID pacjenta; != \"<0\" - nie): ", end='')
                    decision = Userclass.__set_cycle(2)

                print("\nIle cykli? (\"-1\" - wynik symulacji; \"0\" - zakoncz program; \">0\" - ilość cykli): ", end = '')
                decision = Userclass.__set_cycle(0)
                print("Trwa praca programu...")

Userclass.main()