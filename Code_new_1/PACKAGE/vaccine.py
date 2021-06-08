class Vaccine:

    __amount = 0

    # -------------------------------------------------------------------------
    def __init__(self, x, y, ID, fields):
        self.__x_cord = x
        self.__y_cord = y
        self.__ID = ID
        Vaccine.__amount += 1
        fields.change_obj_amount(1, "Vaccine", self.__ID)

    def give_immunity(self, immunity):
        if immunity == 0:
            return int(3) # Zwraca czas chwilowej odpornosci
        else:
            return int(3)


    def destroy(self, fields):
        self.__x_cord = -1
        self.__y_cord = -1
        Vaccine.__amount -= 1
        fields.change_obj_amount(-1, "Vaccine", -1)
        #Chemist.indeks -= 1

    @staticmethod
    def check_amount():
        return Vaccine.__amount