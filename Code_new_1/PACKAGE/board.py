from PACKAGE.field import Field
from PACKAGE.human import Human
from PACKAGE.respirator import Respirator
from PACKAGE.virus import Virus
from PACKAGE.doctor import Doctor
from PACKAGE.chemist import Chemist
from PACKAGE.vaccine import Vaccine
from PACKAGE.medicine import Medicine
import random
import os

class Board:

    # -------------------------------------------------------------------------
    # Atrybuty obiektu, tworzymy listy obiektow znajdujacych sie na planszy

    __current_infected = 0
    __overall_infected = 0
    __immuned = 0
    __on_respirator = 0

    def __init__(self, xsize, ysize, hum, vir, doc, che, res):
        self.__xsize = xsize
        self.__ysize = ysize
        self.__human_num = hum
        self.__virus_num = vir
        self.__doctor_num = doc
        self.__chemist_num = che
        self.__respirator_num = res

        self.__cure_num = 0

        self.__ffields = []
        self.__humans = []
        self.__viruses = []
        self.__doctors = []
        self.__chemists = []
        self.__respirators = []
        self.__vaccines = []
        self.__medicines = []

        self.__ffields = [[Field(x, y) for y in range(self.__ysize)] for x in range(self.__xsize)]

        # NIZEJ POWSTAJA OBIEKTY NA PLANSZY

        for x in range(self.__human_num):
            self.__humans.append(Human(100, False, 0, random.randint(0, 100), False, self.__ffields, x, self.__xsize, self.__ysize))

        for x in range(self.__virus_num):
            self.__viruses.append(Virus(self.__ffields, x, self.__xsize, self.__ysize))

        for x in range(self.__doctor_num):
            self.__doctors.append(Doctor(self.__ffields, x, self.__xsize, self.__ysize))

        for x in range(self.__chemist_num):
            self.__chemists.append(Chemist(self.__ffields, x, self.__xsize, self.__ysize))

        for x in range(self.__respirator_num):
            self.__respirators.append(Respirator(False, self.__ffields, self.__xsize, self.__ysize, x))  # Respirator false - nie jest nikt do niego podłączony


    # -------------------------------------------------------------------------
    # Metoda losuje wspolrzedne obiektow, obiekty nadzoruja by zespawnowac sie tak by kazdy z nich zawieral sie
    # w osobnej kratce (metoda konfiguracyjna, wywolywana na poczatku programu)
    def start(self):

        iterator = 1

        for objects in [self.__humans, self.__viruses, self.__doctors, self.__chemists, self.__respirators]:

            for o in objects:
                cell = self.__ffields[o.x_cor()][o.y_cor()]
                oldcell = cell

                if not cell.answer_first():
                    o.change_cord(self.__xsize, self.__ysize)
                    cell = self.__ffields[o.x_cor()][o.y_cor()]  # Nowa kratka na ktora przechodzi obiekt

                    while not cell.answer():

                        o.change_cord(self.__xsize, self.__ysize)
                        cell = self.__ffields[o.x_cor()][o.y_cor()] # Nowa kratka na ktora przechodzi obiekt

                if iterator == 1:
                    oldcell.change_obj_amount(-1, "Human", -1)
                    cell.change_obj_amount(1, "Human", o.check_id())

                elif iterator == 2:
                    oldcell.change_obj_amount(-1, "Virus", -1)
                    cell.change_obj_amount(1, "Virus", o.check_id())

                elif iterator == 3:
                    oldcell.change_obj_amount(-1, "Doctor", -1)
                    cell.change_obj_amount(1, "Doctor", o.check_id())

                elif iterator == 4:
                    oldcell.change_obj_amount(-1, "Chemist", -1)
                    cell.change_obj_amount(1, "Chemist", o.check_id())

                elif iterator == 5:
                    oldcell.change_obj_amount(-1, "Respirator", -1)
                    cell.change_obj_amount(1, "Respirator", o.check_id())
            iterator += 1

        print("---------------------------------------------------------")

        Field.fresh_change()


    # -------------------------------------------------------------------------
    # Nadzoruje jeden cykl ruchu obiektow

    def cycle(self):

        # print(self.__human_num)
        # for i in range(self.__human_num):
        #     print("x:" + str(self.__humans[i].x_cor()))
        #     print("y:" + str(self.__humans[i].y_cor()))

        #self.show_cycle()

        for i in range(self.__human_num):
            if self.__humans[i].x_cor() >= 0 and self.__humans[i].y_cor() >= 0: # Jesli obiekt istnieje

                # krok 1: Czlowiek wybiera na ktora kratke chce sie ruszyc, potem sie na nia przemieszcza
                # oldcell = self.__humans[i].move(self.__ffields, self.__xsize, self.__ysize)
                cell = self.__humans[i].move(self.__ffields, self.__xsize, self.__ysize) # Obiekt ustala gdzie chce sie ruszyc (na jaka kratke)

                # print("\n\n\n\n\n")

                # krok 2: Czlowiek w zaleznosci od sytuacji wykona nastepujace nizej polecenia:
                self.__humans[i].decrease_immunity_time()
                self.__humans[i].reduce_health(cell)

                # krok 3: Czlowiek sprawdza czy moze wejsc z jakims obiektem w interakcje
                self.__humans[i].interaction(cell, self.__humans, self.__viruses, self.__doctors, self.__respirators, self.__vaccines, self.__medicines)

        # print("PO EKSPANSJI CZLOWIEKA: ")
        #self.show_cycle()

        for i in range(self.__virus_num):
            if self.__viruses[i].x_cor() >= 0 and self.__viruses[i].y_cor() >= 0:
                cell = self.__viruses[i].move(self.__ffields, self.__xsize, self.__ysize)
                self.__viruses[i].interaction(cell, self.__humans, self.__viruses, self.__doctors, self.__respirators, self.__vaccines, self.__medicines)

       #self.show_cycle()

        for i in range(self.__doctor_num):
            cell = self.__doctors[i].move(self.__ffields, self.__xsize, self.__ysize)
            self.__doctors[i].interaction(cell, self.__humans, self.__viruses, self.__doctors, self.__respirators, self.__vaccines, self.__medicines)

        #self.show_cycle()

        for i in range(self.__chemist_num):
            cell = self.__chemists[i].move(self.__ffields, self.__xsize, self.__ysize)

            if Medicine.check_amount() + Vaccine.check_amount() <= int(0.1 * self.__xsize * self.__ysize):
                self.__chemists[i].interaction(cell, self.__humans, self.__viruses, self.__doctors, self.__respirators, self.__vaccines, self.__medicines)

            self.__chemists[i].move(self.__ffields, self.__xsize, self.__ysize)

        #self.show_cycle()

    # -------------------------------------------------------------------------
    # Metoda pokaze cykl populacji, zapisze dane do pliku .csv
    def show_cycle(self):

        os.system('cls')

        for objects in self.__humans:
            Board.__current_infected += objects.human_current_infected()
            Board.__immuned += objects.human_current_immuned()
        for objects in self.__respirators:
            Board.__on_respirator += objects.check_status()

        print("Ilosc ludzi: " + str(Human.check_amount()))
        print("Zarazonych obecnie: " + str(Board.__current_infected))
        print("Odpornych obecnie: " + str(Board.__immuned))
        print("Na respiratorze: " + str(Board.__on_respirator))
        Board.__current_infected = 0
        Board.__immuned = 0
        Board.__on_respirator = 0


        print("Ilosc wirusow: " + str(Virus.check_amount()))
        # print("Ilosc lekarzy: " + str(Doctor.check_amount()))
        # print("Ilosc chemikow: " + str(Chemist.check_amount()))
        # print("Ilosc respiratorow: " + str(Respirator.check_amount()))
        print("Ilosc szczepionek: " + str(Vaccine.check_amount()))
        print("Ilosc lekarstw: " + str(Medicine.check_amount()))

    def show_graphic_representation(self):
        for objects in self.__ffields:
            for o in objects:
                if o.check_status()[0] == 2 and o.check_status()[1] == 1 and o.check_status()[2] == 1:
                    print("! ", end=' ')
                elif o.check_status()[0] == 2:
                    print("? ", end=' ')
                else:
                    if o.check_status()[0] == 0:
                        print(". ", end=' ')
                    if o.check_status()[1] == 1:
                        print("H ", end= ' ')
                    if o.check_status()[2] == 1:
                        print("V ", end= ' ')
                    if o.check_status()[3] == 1:
                        print("D ", end= ' ')
                    if o.check_status()[4] == 1:
                        print("C ", end= ' ')
                    if o.check_status()[5] == 1:
                        print("R ", end= ' ')
                    if o.check_status()[6] == 1:
                        print("S ", end= ' ')
                    if o.check_status()[7] == 1:
                        print("L ", end= ' ')

            print(end='\n')