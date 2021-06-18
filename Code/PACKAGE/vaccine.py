# ILOSC METOD: 4 (w tym konstruktor)

class Vaccine:

    __amount = 0

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Konstruktor

    def __init__(self, x, y, ID, fields):
        self.__x_cord = x
        self.__y_cord = y
        self.__ID = ID
        Vaccine.__amount += 1
        fields.change_obj_amount(1, "Vaccine", self.__ID)

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Po wejsciu na szczepionke zwraca czas chwilowej odpornosci

    def give_immunity(self, immunity):
        if immunity == 0:
            return int(3)
        else:
            return int(3)

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # Usuwa szczepionke, gdy zostanie zebrana

    def destroy(self, fields):
        self.__x_cord = -1
        self.__y_cord = -1
        Vaccine.__amount -= 1
        fields.change_obj_amount(-1, "Vaccine", -1)

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------

    @staticmethod
    def check_amount():
        return Vaccine.__amount