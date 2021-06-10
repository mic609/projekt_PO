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

# ILOSC METOD: 6 (w tym konstruktor)

class Board:

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Atrybuty obiektu, tworzymy listy obiektow znajdujacych sie na planszy

    __current_infected = 0
    __overall_infected = 0
    __immuned = 0
    __on_respirator = 0

    def __init__(self, xsize, ysize, hum, vir, doc, che, res):

        # Wymiary planszy, początkowa ilość obiektów

        self.__xsize = xsize
        self.__ysize = ysize
        self.__human_num = hum
        self.__virus_num = vir
        self.__doctor_num = doc
        self.__chemist_num = che
        self.__respirator_num = res

        self.__cure_num = 0 #???

        # Przygotowanie pustych list na obiekty

        self.__ffields = []
        self.__humans = []
        self.__viruses = []
        self.__doctors = []
        self.__chemists = []
        self.__respirators = []
        self.__vaccines = []
        self.__medicines = []

        # Tworzymy kratki:

        self.__ffields = [[Field(x, y) for y in range(self.__ysize)] for x in range(self.__xsize)]

        # Niżej powstają obiekty na planszy:

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
    # -------------------------------------------------------------------------
    # Metoda losuje wspolrzedne obiektow, obiekty nadzoruja by zespawnowac sie tak by kazdy z nich zawieral sie
    # w osobnej kratce (metoda konfiguracyjna, wywolywana na poczatku programu)

    def start(self):

        iterator = 1 # zmienna pomocnicza

        for objects in [self.__humans, self.__viruses, self.__doctors, self.__chemists, self.__respirators]:

            for o in objects:
                cell = self.__ffields[o.x_cor()][o.y_cor()]
                oldcell = cell

                if not cell.answer_first():

                    # Losujemy wspolrzedne obiektu
                    o.change_cord(self.__xsize, self.__ysize)

                    # Zapisujemy na ktorej kratce wyladowal obiekt
                    cell = self.__ffields[o.x_cor()][o.y_cor()]

                    # Jesli na wybranej kratce jest juz jakis obiekt, powtorz powyzszy proces
                    while not cell.answer():

                        o.change_cord(self.__xsize, self.__ysize)
                        cell = self.__ffields[o.x_cor()][o.y_cor()]

                # W zaleznosci jaki obiekt pojawil sie na kratce, zmien jej status (ilosc obiektow na niej sie znajdujacej)

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
    # -------------------------------------------------------------------------
    # Wykonuje cykl ruchu obiektow. Cykl jest to okres po ktorym wszystkie obiekty na
    # planszy przemieszczaja sie o jedno pole. Kazdy obiekt porusza sie oddzielnie, kolejno:
    # ludzie, wirusy, lekarze i chemicy. Po kazdym takim cyklu sa zbierane dane

    def cycle(self):

        # Nadzorujemy ruch ludzi:

        for i in range(self.__human_num):
            if self.__humans[i].x_cor() >= 0 and self.__humans[i].y_cor() >= 0: # Jesli obiekt istnieje

                # Obiekt wybiera na ktora kratke chce sie ruszyc, potem sie na nia przemieszcza
                cell = self.__humans[i].move(self.__ffields, self.__xsize, self.__ysize)

                # Obiekt w zaleznosci od sytuacji wykona nastepujace nizej polecenia:
                self.__humans[i].decrease_immunity_time()
                self.__humans[i].reduce_health(cell)

                # Obiekt sprawdza czy moze wejsc z jakims obiektem w interakcje
                self.__humans[i].interaction(cell, self.__humans, self.__viruses, self.__doctors, self.__respirators, self.__vaccines, self.__medicines)

        # Nadzorujemy ruch wirusow:

        for i in range(self.__virus_num):
            if self.__viruses[i].x_cor() >= 0 and self.__viruses[i].y_cor() >= 0: # Jesli obiekt istnieje

                # Obiekt wybiera na ktora kratke chce sie ruszyc, potem sie na nia przemieszcza
                cell = self.__viruses[i].move(self.__ffields, self.__xsize, self.__ysize)

                # Obiekt sprawdza czy moze wejsc z jakims obiektem w interakcje
                self.__viruses[i].interaction(cell, self.__humans, self.__viruses, self.__doctors, self.__respirators, self.__vaccines, self.__medicines)

        # Nadzorujemy ruch lekarzy:

        for i in range(self.__doctor_num):

            # Obiekt wybiera na ktora kratke chce sie ruszyc, potem sie na nia przemieszcza
            cell = self.__doctors[i].move(self.__ffields, self.__xsize, self.__ysize)

            # Obiekt sprawdza czy moze wejsc z jakims obiektem w interakcje
            self.__doctors[i].interaction(cell, self.__humans, self.__viruses, self.__doctors, self.__respirators, self.__vaccines, self.__medicines)

        # Nadzorujemy ruch chemikow:

        for i in range(self.__chemist_num):

            # Chemik pobiera tutaj tylko kratke na ktorej stoi
            cell = self.__chemists[i].move(self.__ffields, self.__xsize, self.__ysize)

            # Chemik wyprodukuje lekarstwo lub szczepionke, jesli ogolna ich liczba nie przekracza dopuszczalnej
            # Chemik wyprodukuje lekarstwo tylko wtedy, gdy stoi na kratce sam
            if Medicine.check_amount() + Vaccine.check_amount() <= int(0.1 * self.__xsize * self.__ysize):
                self.__chemists[i].interaction(cell, self.__humans, self.__viruses, self.__doctors, self.__respirators, self.__vaccines, self.__medicines)

            # Po wykonaniu czynnosci chemik finalnie przemieszcza sie
            self.__chemists[i].move(self.__ffields, self.__xsize, self.__ysize)


    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Metoda pokaze cykl populacji, zapisze dane do pliku .csv

    def show_cycle(self, dzien):

        os.system('cls')

        # Zliczana jest ilosc ludzi obecnie zarazonych, odpornych i podlaczonych do respiratora (za pomoca specjalnych funkcji)
        for objects in self.__humans:
            Board.__current_infected += objects.human_infected("current")
            Board.__immuned += objects.human_current_immuned()
        for objects in self.__respirators:
            Board.__on_respirator += objects.check_status()

        print("DZIEŃ "+str(dzien)+"\n")
        print("Ilosc lekarzy: " + str(Doctor.check_amount()))
        print("Ilosc chemikow: " + str(Chemist.check_amount()))
        print("Ilosc respiratorow: " + str(Respirator.check_amount()))
        print("\n")

        print("Ilosc ludzi: " + str(Human.check_amount()))
        print("Zarazonych obecnie: " + str(Board.__current_infected))
        print("Odpornych obecnie: " + str(Board.__immuned))
        print("Na respiratorze: " + str(Board.__on_respirator))

        print("Ilosc wirusow: " + str(Virus.check_amount()))
        print("Ilosc szczepionek: " + str(Vaccine.check_amount()))
        print("Ilosc lekarstw: " + str(Medicine.check_amount()))

        plik = open("Dane.txt", "a")

        if plik.writable():

            plik.write("---------------------------------------------------------")
            plik.write("\nDZIEŃ " + str(dzien) + "\n\n")
            plik.write("Ilosc lekarzy: " + str(Doctor.check_amount()) + "\n")
            plik.write("Ilosc chemikow: " + str(Chemist.check_amount())+ "\n")
            plik.write("Ilosc respiratorow: " + str(Respirator.check_amount()) + "\n\n")

            plik.write("Ilosc ludzi: " + str(Human.check_amount()) + "\n")
            plik.write("Zarazonych obecnie: " + str(Board.__current_infected) + "\n")
            plik.write("Odpornych obecnie: " + str(Board.__immuned) + "\n")
            plik.write("Na respiratorze: " + str(Board.__on_respirator) + "\n")

            plik.write("Ilosc wirusow: " + str(Virus.check_amount()) + "\n")
            plik.write("Ilosc szczepionek: " + str(Vaccine.check_amount()) + "\n")
            plik.write("Ilosc lekarstw: " + str(Medicine.check_amount()) + "\n\n")

        plik.close()

        # Po kazdym cyklu trzeba zresetowac dane (zeby co kazdy cykl sie zmienialy)
        Board.__current_infected = 0
        Board.__immuned = 0
        Board.__on_respirator = 0

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Metoda przedstawia graficzne rozstawienie obiektow po zakonczeniu danego cyklu

    def show_graphic_representation(self):

        print("\nPo ruchu wszystkich obiektów:\n")

        j = self.__xsize -1
        i = 0

        while j >= 0:
            while i < self.__ysize:
                if self.__ffields[j][i].check_status()[0] == 2 and self.__ffields[j][i].check_status()[1] == 1 and self.__ffields[j][i].check_status()[2] == 1:
                    print("! ", end=' ')
                elif self.__ffields[j][i].check_status()[0] == 2:
                    print("? ", end=' ')
                elif self.__ffields[j][i].check_status()[0] == 0:
                    print(". ", end=' ')
                else:
                    if self.__ffields[j][i].check_status()[1] == 1:
                        print("H ", end= ' ')
                    if self.__ffields[j][i].check_status()[2] == 1:
                        print("V ", end= ' ')
                    if self.__ffields[j][i].check_status()[3] == 1:
                        print("D ", end= ' ')
                    if self.__ffields[j][i].check_status()[4] == 1:
                        print("C ", end= ' ')
                    if self.__ffields[j][i].check_status()[5] == 1:
                        print("R ", end= ' ')
                    if self.__ffields[j][i].check_status()[6] == 1:
                        print("S ", end= ' ')
                    if self.__ffields[j][i].check_status()[7] == 1:
                        print("L ", end= ' ')
                i += 1
            j -= 1
            i = 0
            print(end='\n')

        plik = open("Dane.txt", "a", encoding="utf-8")
        plik.write("\nPo ruchu wszystkich obiektów:\n\n")

        j = self.__xsize - 1
        i = 0

        while j >= 0:
            while i < self.__ysize:
                if self.__ffields[j][i].check_status()[0] == 2 and self.__ffields[j][i].check_status()[1] == 1 and self.__ffields[j][i].check_status()[2] == 1:
                    plik.write("! ")
                elif self.__ffields[j][i].check_status()[0] == 2:
                    plik.write("? ")
                elif self.__ffields[j][i].check_status()[0] == 0:
                    plik.write(". ")
                else:
                    if self.__ffields[j][i].check_status()[1] == 1:
                        plik.write("H ")
                    if self.__ffields[j][i].check_status()[2] == 1:
                        plik.write("V ")
                    if self.__ffields[j][i].check_status()[3] == 1:
                        plik.write("D ")
                    if self.__ffields[j][i].check_status()[4] == 1:
                        plik.write("C ")
                    if self.__ffields[j][i].check_status()[5] == 1:
                        plik.write("R ")
                    if self.__ffields[j][i].check_status()[6] == 1:
                        plik.write("S ")
                    if self.__ffields[j][i].check_status()[7] == 1:
                        plik.write("L ")
                i += 1
            j -= 1
            i = 0
            plik.write("\n")
        plik.write("\n")
        plik.close()

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Metoda uruchamia funkcje z klasy Human o nazwie chart

    def chart(self, ID):
        self.__humans[ID].chart()