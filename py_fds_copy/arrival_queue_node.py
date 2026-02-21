class ArrivalQueueNode:
    """
    Limitations:
        - no weight or quantity limitations
    """

    def __init__(self, nxt: 'ArrivalQueueNode' = None):
        self.crate = None
        self.next = nxt
