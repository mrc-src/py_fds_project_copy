class Shelf:
    """
    Limitations:
        - store crates in an array
        - up to 4 crates
        - up to 1000kgs max
        - must form a node-backed linked list with other shelves
    """
    MAX_WEIGHT = 1000

    def __init__(self):
        self.crates = []
        self.total_weight = 0
        self.next = None

    def add_crate(self, crate: tuple[str, int]):
        if self.can_add_crate(crate):
            self.crates.append(crate)
            self.total_weight += crate[1]

    def can_add_crate(self, crate: tuple[str, int]):
        if len(self.crates) >= 4:
            return False
        if crate in self.crates:
            return False
        if self.total_weight + crate[1] > self.MAX_WEIGHT:
            return False
        return True

