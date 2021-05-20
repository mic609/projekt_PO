class CureObject:

    # -------------------------------------------------------------------------
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    # -------------------------------------------------------------------------
    @staticmethod
    def heal(human, n):
        human.restore_health(n)
