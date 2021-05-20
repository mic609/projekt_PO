class Vaccine:

    amount = 0

    # -------------------------------------------------------------------------
    def __init__(self, x, y, ID, fields):
        self.__x_cord = x
        self.__y_cord = y
        self.__ID = ID
        self.amount += 1
        fields.change_obj_amount(1, "Medicine", self.__ID)

    def give_immunity(self, immunity):
        if immunity == 0:
            return 3 # Zwraca czas chwilowej odpornosci


    def destroy(self, fields):
        self.__x_cord = -1
        self.__y_cord = -1
        self.amount -= 1
        fields.change_obj_amount(-1, "Vaccine", -1)
