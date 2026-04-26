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
    MAX_CRATES = 10

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
        self.__next = value

    def __add__(self, other: tuple[str, int]):
        self.add_crate(other)
        return self

    def peek_crate(self):
        if len(self.__crates) == 0:
            return None
        return self.__crates[-1]

    def pop_crate(self):
        if len(self.__crates) == 0:
            return None
        crate = self.__crates.pop()
        self.__total_weight -= crate[1]
        return crate


class SteelShelf(Shelf):
    def __init__(self):
        super().__init__()
        self.MAX_WEIGHT = 2000
        self.MAX_CRATES = 15


class UnsortedSteelShelf(SteelShelf):
    def __init__(self):
        super().__init__()

    def can_add_crate(self, crate: tuple[str, int]):
        return self.__total_weight + crate[1] <= self.MAX_WEIGHT

