from typing import List

from arrival_queue_node import ArrivalQueueNode
from Shelf import Shelf
from SteelShelf import SteelShelf
from UnsortedSteelShelf import UnsortedSteelShelf


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

    # used to sort the crates to fit as many as possible
    sorting_floor = []

    # the warehouse contains 10 shelves, which form a node-backed Linked List
    shelves_head = None
    # and 5 steel shelves
    steel_shelf_head = None
    # and 5 unsorted steel shelves
    unsorted_shelf_head = None

    # instantiating the arrival queue
    arrival_queue_head = ArrivalQueueNode(None)

    def __init__(self, crates: List[tuple[str, int]]):
        # instantiate 10 shelves per warehouse
        for _ in range(10):
            next_shelf = Shelf()
            next_shelf.next = self.shelves_head
            self.shelves_head = next_shelf

        for _ in range(5):
            next_steel_shelf = SteelShelf()
            next_unsorted_shelf = UnsortedSteelShelf()

            next_steel_shelf.next = next_steel_shelf
            next_unsorted_shelf.next = next_unsorted_shelf

            self.steel_shelf_head = next_steel_shelf
            self.unsorted_shelf_head = next_unsorted_shelf

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

        # loop will be iterating over shelves multiple times
        # this flag variable stops the loop if current crate cannot be inserted
        changes: bool = True
        second_iter: bool = False

        # try to insert all crates in arrival_queue
        # stop if a crate cannot be inserted
        while changes:
            while self.arrival_queue_head or self.sorting_floor:
                changes = False

                # get current crate and advance arrival_queue
                current_crate = self.arrival_queue_head.crate
                self.arrival_queue_head = self.arrival_queue_head.next

                # iterate until we insert crate and there are no leftover
                # crates from previous insertions
                while copy_shelves_head and current_crate:
                    if copy_shelves_head.can_add_crate(current_crate):
                        changes = True

                        # if crate can be added, remove all lighter crates from the stack
                        while copy_shelves_head.peek_crate():
                            if copy_shelves_head.peek_crate()[1] < current_crate[1]:
                                self.sorting_floor.append(copy_shelves_head.pop_crate())
                            else:
                                break

                        # add crate to stack
                        copy_shelves_head.add_crate(current_crate)
                        current_crate = None

                        # add all possible crates from sorting_floor to shelf
                        # at the end, crates that could not be inserted (if any)
                        # will be stored in current_crate
                        while self.sorting_floor:
                            if copy_shelves_head.can_add_crate(self.sorting_floor[-1]):
                                copy_shelves_head += self.sorting_floor.pop()
                            else:
                                copy_shelves_head = copy_shelves_head.next

                                # if a crate in the sorting floor cannot be added,
                                # make it the new current_crate
                                current_crate = self.sorting_floor.pop()
                    # if crate cannot be added to the current shelf,
                    # try the next shelf
                    else:
                        copy_shelves_head = copy_shelves_head.next
            # we can only get to this code snippet if
            # - we have no more crates to add
            # - we iterated through all the shelves
            # if we did iterate through all the shelves, reset the head pointer
            # to try to pack as many crates as possible
            copy_shelves_head = self.shelves_head
            if not second_iter:
                second_iter = True
                changes = True
                continue
            changes = True
            steel_shelf_head_copy = self.steel_shelf_head
            while changes:
                changes = False
                while steel_shelf_head_copy and self.arrival_queue_head:
                    if steel_shelf_head_copy.can_add_crate(self.arrival_queue_head.crate):
                        steel_shelf_head_copy.add_crate(self.arrival_queue_head.crate)
                        self.arrival_queue_head = self.arrival_queue_head.next
                        changes = True
                        break
                    else:
                        steel_shelf_head_copy = steel_shelf_head_copy.next

            unsorted_shelf_head_copy = self.unsorted_shelf_head
            changes = True
            while changes:
                changes = False
                while unsorted_shelf_head_copy and self.arrival_queue_head:
                    if unsorted_shelf_head_copy.can_add_crate(self.arrival_queue_head.crate):
                        unsorted_shelf_head_copy.add_crate(self.arrival_queue_head.crate)
                        self.arrival_queue_head = self.arrival_queue_head.next
                        changes = True
                        break
                    else:
                        unsorted_shelf_head_copy = unsorted_shelf_head_copy.next

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
