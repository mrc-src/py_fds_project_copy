from Shelf import Shelf


class SteelShelf(Shelf):
    def __init__(self):
        super().__init__()
        self.MAX_WEIGHT = 2000
        self.MAX_CRATES = 15
