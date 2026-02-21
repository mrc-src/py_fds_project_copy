from typing import List

from arrival_queue_node import ArrivalQueueNode
from shelf import Shelf


class Warehouse:
    """
    Warehouse class for managing all other classes
    The program must create a Warehouse (a class-container for the code) that contains:
        - 10 Shelves that form a node-backed linked list
            ~ each shelf can store up to 4 crates and 1000kgs
        - Arrival Queue - node-backed queue in which the crates are stored before processing
            ~ no weight or size limitations
        - Sorting Floor
            ~ only defined and still unused, but will be used to sort crates in the future
    """

    # not used. but required by the assignment
    sortingFloor = []

    # the warehouse contains 10 shelves, which form a node-backed Linked List
    shelves_head = None

    # instantiating the arrival queue
    arrival_queue_head = ArrivalQueueNode(None)

    def __init__(self, crates: List[tuple[str, int]]):
        # instantiate 10 shelves per warehouse
        for _ in range(10):
            next_shelf = Shelf()
            next_shelf.next = self.shelves_head
            self.shelves_head = next_shelf

        # populate the arrival_queue with all elements from the argument
        for crate in crates[::-1]:
            self.arrival_queue_head.crate = crate
            self.arrival_queue_head = ArrivalQueueNode(self.arrival_queue_head)

        # this generates an additional empty arrivalQueueNode, so skip it
        self.arrival_queue_head = self.arrival_queue_head.next

        # start populating the shelves with elements from the arrival queue
        self.empty_arrival_queue()

    def empty_arrival_queue(self):
        # get a copy of the pointer to the first shelf
        copy_shelves_head = self.shelves_head

        # iterate through the entire queue
        while self.arrival_queue_head is not None:
            crate = self.arrival_queue_head.crate

            if copy_shelves_head.can_add_crate(crate):
                # if crate can be added, add it and advance the queue
                copy_shelves_head.add_crate(crate)
                self.arrival_queue_head = self.arrival_queue_head.next

            else:
                # check the next shelf
                # by the assignment, the crates are ordered in such a way that we needn't backtrack
                copy_shelves_head = copy_shelves_head.next

    # validator
    def validate(self) -> str:
        msg = ''
        shelf = self.shelves_head

        while shelf is not None:
            msg += '|'

            # if the weight is under the limit, print "Good"
            # otherwise, print "Bad"
            msg += '  Good   ' if shelf.total_weight <= 1000 and len(shelf.crates) <= 4 else '   Bad   '

            # advance the shelf
            shelf = shelf.next

        return msg
