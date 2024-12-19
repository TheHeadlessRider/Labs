from abc import ABC, abstractmethod

class GameObject(ABC):
    _id_counter = 1  # cчетчик для уникальных идентификаторов объектов

    def __init__(self, name, x, y):
        self._id = GameObject._id_counter  # уникальное ID
        GameObject._id_counter += 1
        self._name = name
        self._x = x
        self._y = y

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y


class Moveable(ABC):
    @abstractmethod
    def move(self, dx, dy):
        pass

class Attacker(ABC):
    @abstractmethod
    def attack(self, unit):
        pass

class Unit(GameObject): # класс, описывающий юниты, которые можно контролировать
    def __init__(self, name, x, y, hp):
        super().__init__(name, x, y) # инициализация родительского класса GameObject
        self._hp = hp

    def is_alive(self):
        return self._hp > 0

    def get_hp(self):
        return self._hp

    def receive_damage(self, damage):

        self._hp -= damage
        if self._hp < 0:
            self._hp = 0

class Archer(Unit, Attacker, Moveable): # класс лучника, наследует Unit и реализует интерфейсы Attacker и Moveable

    def __init__(self, x, y, hp=100):
        super().__init__("Archer", x, y, hp)
        self._attack_power = 20

    def attack(self, unit): #атака друго юнита
        if isinstance(unit, Unit) and unit.is_alive():
            unit.receive_damage(self._attack_power)

    def move(self, dx, dy):
        self._x += dx
        self._y += dy


class Building(GameObject): # построки
    def __init__(self, name, x, y, built=False):
        super().__init__(name, x, y)
        self._built = built  # флаг, построена ли постройка

    def is_built(self):
        return self._built

class Fort(Building, Attacker): # класс крепости

    def __init__(self, x, y, built=True):
        super().__init__("Fort", x, y, built)
        self._attack_power = 50  # Сила атаки крепости

    def attack(self, unit):
        if isinstance(unit, Unit) and unit.is_alive():
            unit.receive_damage(self._attack_power)

class MobileHouse(Building, Moveable):
    def __init__(self, x, y, built=True):
        super().__init__("MobileHouse", x, y, built)

    def move(self, dx, dy):
        self._x += dx
        self._y += dy

