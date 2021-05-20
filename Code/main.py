from human import Human
from virus import Virus
from cure_object import CureObject


h1 = Human(100, 100, 20)
print(h1)
h1.reduce_health_bar(30)
v1 = Virus(100, 100)
Virus.infect(h1)
print(h1)
error = CureObject(20, 30)
