from typing import List


class Shelf:
    """
    Shelf class for storing crates
    Limitations:
        - store crates in an array
        - up to 4 crates
        - up to 1000kgs max
        - must form a node-backed linked list with other shelves
    """
    MAX_WEIGHT = 1000

    def __init__(self):
        self.__crates = []
        self.__total_weight = 0
        self.__next = None

    def add_crate(self, crate: tuple[str, int]):
        if self.can_add_crate(crate):
            self.__crates.append(crate)
            self.__total_weight += crate[1]

    def can_add_crate(self, crate: tuple[str, int]):
        if len(self.__crates) >= 4:
            return False
        if crate in self.__crates:
            return False
        if self.__total_weight + crate[1] > self.MAX_WEIGHT:
            return False
        return True

    @property
    def crates(self):
        return self.__crates

    @property
    def total_weight(self):
        return self.__total_weight

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value: 'Shelf'):
        if value is None or value is self:
            raise ValueError('invalid next shelf')
        self.__next = value
