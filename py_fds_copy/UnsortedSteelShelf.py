from SteelShelf import SteelShelf


class UnsortedSteelShelf(SteelShelf):
    def __init__(self):
        super().__init__()

    def can_add_crate(self, crate: tuple[str, int]):
        return self.__total_weight + crate[1] <= self.MAX_WEIGHT
