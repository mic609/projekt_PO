from movable_object import MovableObject

HEALTH_CAP = 100


class Human(MovableObject):

    amount = 0

    # -------------------------------------------------------------------------
    def __init__(self, x_coordinate, y_coordinate, age, health_points=HEALTH_CAP, resp=False, immunity=False,
                 infected=False):
        super().__init__(x_coordinate, y_coordinate)
        self.age = age
        self.health_points = health_points
        self.resp = resp
        self.immunity = immunity
        self.infected = False
        Human.amount += 1

    # -------------------------------------------------------------------------
    def reduce_health_bar(self, n):
        new_hp = self.health_points - n
        self.health_points = new_hp if new_hp >= 0 else 0

    # -------------------------------------------------------------------------
    def restore_health(self, n):
        new_hp = self.health_points + n
        self.health_points = new_hp if new_hp <= HEALTH_CAP else HEALTH_CAP

    # -------------------------------------------------------------------------
    def full_restore_health(self):
        self.health_points = HEALTH_CAP

    # -------------------------------------------------------------------------
    def __str__(self):
        return f"Human(x:{self.x_coordinate}," \
               f" y:{self.y_coordinate}," \
               f" age:{self.age}," \
               f" hp:{self.health_points}," \
               f" resp:{self.resp}," \
               f" immunity:{self.immunity}," \
               f" infected:{self.infected})"
