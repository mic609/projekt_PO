class Human:
    def __init__(self, x_coordinate, y_coordinate, age, health_points=100):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.age = age
        self.health_points = health_points

    def reduce_health_bar(self, n):
        self.health_points -= n

    def who_am_i(self):
        print(f"My (x,y) = ({self.x_coordinate}, {self.y_coordinate}), age = {self.age}, hp = {self.health_points}")


human1 = Human(100, 20, 40)
human2 = Human(80, 30, 70)
human1.who_am_i()
human1.reduce_health_bar(10)
human1.who_am_i()
human2.who_am_i()
