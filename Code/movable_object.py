class MovableObject:

    # -------------------------------------------------------------------------
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    # -------------------------------------------------------------------------
    def move(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y

