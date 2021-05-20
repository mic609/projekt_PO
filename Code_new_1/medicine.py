class Medicine:

    __amount = 0

    # -------------------------------------------------------------------------
    def __init__(self, x, y, ID, fields): # cell - kratka- obiekt
        self.__x_cord = x
        self.__y_cord = y
        self.__ID = ID
        self.__amount += 1
        fields.change_obj_amount(1, "Medicine", self.__ID)

    # -------------------------------------------------------------------------
    # Metoda zwraca czlowiekowi podwyzszona wartosc punktow HP
    def heal(self, HP):
        if HP <= 90:
            return [HP + 10, False] # Drugi argument dotyczy tego czy czlowiek jest zarazony
        else:
            return [100, True]

    # -------------------------------------------------------------------------
    # Metoda "niszczy" obiekt leczniczy (zaraz po tym jak obiekt ludzki je wezmie)
    def destroy(self, fields):
        self.__x_cord = -1
        self.__y_cord = -1
        self.__amount -= 1
        fields.change_obj_amount(-1, "Medicine", -1)

    @staticmethod
    def check_amount(self):
        return self.__amount