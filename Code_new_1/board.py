from field import Field
from human import Human
from respirator import Respirator
from virus import Virus
from doctor import Doctor
from chemist import Chemist
from vaccine import Vaccine
from medicine import Medicine
import random

class Board:

    # -------------------------------------------------------------------------
    # Atrybuty obiektu, tworzymy listy obiektow znajdujacych sie na planszy
    def __init__(self, xsize, ysize, hum, vir, doc, che, res):
        self.__xsize = xsize
        self.__ysize = ysize
        self.__human_num = hum
        self.__virus_num = vir
        self.__doctor_num = doc
        self.__chemist_num = che
        self.__respirator_num = res
        self.__ffields = []
        self.__humans = []
        self.__viruses = []
        self.__doctors = []
        self.__chemists = []
        self.__respirators = []
        self.__vaccines = []
        self.__medicines = []

        self.__ffields = [[Field(x, y, self.__xsize, self.__ysize) for y in range(self.__xsize)] for x in range(self.__ysize)]

        for x in range(self.__human_num):
            self.__humans.append(Human(100, False, 0, random.randint(0, 100), False, self.__ffields, x, self.__xsize, self.__ysize))  # Tutaj powstają obiekty klasy człowiek

        for x in range(self.__virus_num):
            self.__viruses.append(Virus(self.__ffields, x, self.__xsize, self.__ysize))

        for x in range(self.__doctor_num):
            self.__doctors.append(Doctor(self.__ffields, x, self.__xsize, self.__ysize))

        for x in range(self.__chemist_num):
            self.__chemists.append(Chemist(self.__ffields, x, self.__xsize, self.__ysize))

        for x in range(self.__respirator_num):
            self.__respirators.append(Respirator(False, self.__xsize, self.__ysize, x, self.__ffields))  # Respirator false - nie jest nikt do niego podłączony

    # -------------------------------------------------------------------------
    # Metoda losuje wspolrzedne obiektow, obiekty nadzoruja by zespawnowac sie tak by kazdy z nich zawieral sie
    # w osobnej kratce
    def start(self):

        for objects in [self.__doctors, self.__viruses, self.__humans, self.__chemists]:
            for o in objects:
                cell = self.__ffields[int(o.x_cord())][int(o.y_cord())]
                while not cell.answer():
                    o.change_cord(self.__xsize, self.__ysize)

    # -------------------------------------------------------------------------
    # Nadzoruje jeden cykl ruchu obiektow

    def cycle(self):
        for i in range(self.__human_num):
            if self.__humans[i].x_cord() > 0 and self.__humans[i].y_cord() > 0: # Jesli obiekt istnieje
                # krok 1: Czlowiek wybiera na ktora kratke chce sie ruszyc, potem sie na nia przemieszcza
                cell = self.__humans[i].move(self.__ffields) # Obiekt ustala gdzie chce sie ruszyc (na jaka kratke)
                # krok 2: Czlowiek w zaleznosci od sytuacji wykona nastepujace nizej polecenia
                self.__humans[i].decrease_immunity_time()
                self.__humans[i].reduce_health(cell)

                # krok 3: Czlowiek sprawdza czy moze wejsc z jakims obiektem w interakcje
                self.__humans[i].interaction(cell, self.__humans, self.__viruses, self.__doctors, self.__respirators, self.__vaccines, self.__medicines)

        self.show_cycle() # Opcjonalnie

        for i in range(self.__virus_num):
            if self.__viruses[i].x_cord() > 0 and self.__viruses[i].y_cord() > 0:
                cell = self.__viruses[i].move(self.__ffields)
                self.__viruses[i].interaction(cell, self.__humans, self.__viruses, self.__doctors, self.__respirators, self.__vaccines, self.__medicines)

        self.show_cycle()  # Opcjonalnie

        for i in range(self.__doctor_num):
            cell = self.__doctors[i].move(self.__ffields)
            self.__doctors[i].interaction(cell, self.__humans, self.__viruses, self.__doctors, self.__respirators, self.__vaccines, self.__medicines)

        self.show_cycle()  # Opcjonalnie

        for i in range(self.__chemist_num):
            cell = self.__chemists[i].move(self.__ffields)
            self.__chemists[i].move(self.__ffields)
            self.__chemists[i].interaction(cell, self.__humans, self.__viruses, self.__doctors, self.__respirators, self.__vaccines, self.__medicines)

        self.show_cycle()  # Opcjonalnie

    # -------------------------------------------------------------------------
    # Metoda pokaze cykl populacji, zapisze dane do pliku .csv
    def show_cycle(self):
        print("Ilosc ludzi: " + str(self.__human_num))
        print("Ilosc wirusow: " + str(self.__virus_num))
        print("Ilosc lekarzy: " + str(self.__doctor_num))
        print("Ilosc chemikow: " + str(self.__chemist_num))
        print("Ilosc respiratorow: " + str(self.__respirator_num))
        print("Ilosc szczepionek: " + str(Vaccine.check_amount(self)))
        print("Ilosc lekarstw: " + str(Medicine.check_amount(self)))