class ArrivalQueueNode:
    """
    Arrival Queue Node - a way to create a Linked List
    and use it as an arrival queue in the warehouse
    Limitations:
        - no weight or quantity limitations
    """

    def __init__(self, nxt: 'ArrivalQueueNode' = None):
        self.crate = None
        self.next = nxt
