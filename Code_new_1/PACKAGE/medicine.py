# ILOSC METOD: 4 (w tym konstruktor)

class Medicine:

    __amount = 0

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Konstruktor

    def __init__(self, x, y, ID, fields):
        self.__x_cord = x
        self.__y_cord = y
        self.__ID = ID
        Medicine.__amount += 1
        fields.change_obj_amount(1, "Medicine", self.__ID)

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Metoda zwraca czlowiekowi podwyzszona wartosc punktow HP

    def heal(self, HP):
        if HP < 90:
            return HP + 10
        else:
            return 100

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Metoda "niszczy" obiekt leczniczy (zaraz po tym jak obiekt ludzki je wezmie)

    def destroy(self, fields):
        self.__x_cord = -1
        self.__y_cord = -1
        Medicine.__amount -= 1
        fields.change_obj_amount(-1, "Medicine", -1)

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------

    @staticmethod
    def check_amount():
        return Medicine.__amount