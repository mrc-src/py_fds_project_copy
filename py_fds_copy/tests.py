from unittest import TestCase, main
from warehouse import Shelf, ArrivalQueueNode, Warehouse


class ShelfTests(TestCase):
    """
    Includes unit tests for most aspects of the program
    """
    def setUp(self):
        self.shelf = Shelf()

    def test_init(self):
        self.assertEqual([], self.shelf.crates)
        self.assertEqual(0, self.shelf._total_weight)
        self.assertEqual(None, self.shelf.next)

    def test_add_crate_valid(self):
        self.shelf.add_crate(('AA', 10))
        self.assertEqual([('AA', 10)], self.shelf.crates)
        self.assertEqual(10, self.shelf.total_weight)

    def test_add_crate_invalid(self):
        self.shelf.add_crate(('AA', 1001))
        self.assertEqual([], self.shelf.crates)
        self.assertEqual(0, self.shelf.total_weight)

    def test_add_too_many_crates(self):
        self.shelf.add_crate(('AA', 1))
        self.shelf.add_crate(('AB', 2))
        self.shelf.add_crate(('AC', 3))
        self.shelf.add_crate(('AD', 4))
        self.shelf.add_crate(('AE', 5))
        self.assertEqual(4, len(self.shelf.crates))
        self.assertEqual(10, self.shelf.total_weight)

    def test_add_crate_overweight(self):
        self.shelf.add_crate(('AA', 999))
        self.shelf.add_crate(('AB', 999))
        self.assertEqual(1, len(self.shelf.crates))
        self.assertEqual(999, self.shelf.total_weight)


class ArrivalQueueNodeTests(TestCase):
    def setUp(self):
        self.aqn = ArrivalQueueNode()

    def test_init_empty(self):
        self.assertEqual(None, self.aqn.crate)
        self.assertEqual(None, self.aqn.next)

    def test_init_other(self):
        test_aqn = ArrivalQueueNode(self.aqn)
        self.assertEqual(self.aqn, test_aqn.next)


class WarehouseTests(TestCase):
    def setUp(self):
        self.crates_list = [
            ('AA', 500),
            ('AB', 500),
            ('AC', 100)
        ]
        self.wh = Warehouse(self.crates_list)

    def test_init(self):
        self.assertEqual(None, self.wh.arrival_queue_head)
        self.assertGreater(len(self.wh.shelves_head.crates), 0)

    def test_emptying_arrival_queue(self):
        self.wh.arrival_queue_head = ArrivalQueueNode()
        self.wh.arrival_queue_head.crate = ('AA', 1)
        self.wh.arrival_queue_head = ArrivalQueueNode(self.wh.arrival_queue_head)
        self.wh.arrival_queue_head.crate = ('AB', 2)

        self.wh.empty_arrival_queue()

        self.assertEqual(None, self.wh.arrival_queue_head)

    def test_emptying_empty_arrival_queue(self):
        self.wh.arrival_queue_head = None

        self.wh.empty_arrival_queue()


if __name__ == '__main__':
    main()
