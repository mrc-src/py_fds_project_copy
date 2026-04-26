"""
This module contains the ArrivalQueueNode class, which
is responsible for managing the crates read from the text file
and provide temporary storage for them

This class includes only getters and setters for the
different properties
"""


class ArrivalQueueNode:
    """
    Arrival Queue Node - a way to create a Linked List
    and use it as an arrival queue in the warehouse
    Limitations:
        - no weight or quantity limitations
    """

    def __init__(self, nxt: 'ArrivalQueueNode' = None):
        self.__crate = None
        self.__next = nxt

    @property
    def crate(self):
        return self.__crate

    @crate.setter
    def crate(self, value: tuple[str, int]):
        if not (value[0] and value[1] > 0):
            raise ValueError('invalid crate values')
        self.__crate = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, n: 'ArrivalQueueNode'):
        if n is None:
            raise ValueError('next node must not be None')
        if n is self:
            raise ValueError('next node must be different from current nodes')
        self.__next = n
