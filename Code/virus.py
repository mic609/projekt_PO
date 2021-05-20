from movableObject import MovableObject


class Virus(MovableObject):

    amount = 0

    # -------------------------------------------------------------------------
    def __init__(self, x_coordinate, y_coordinate):
        super().__init__(x_coordinate, y_coordinate)
        Virus.amount += 1

    # -------------------------------------------------------------------------
    @staticmethod
    def infect(human):
        human.infected = True

    # -------------------------------------------------------------------------
    def __str__(self):
        return f"Virus(x:{self.x_coordinate}, y:{self.y_coordinate})"
