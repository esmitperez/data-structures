import unittest

from lists.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    """Test LinkedList methods

    Args:
        unittest (_type_): _description_
    """

    def test_length(self):
        """length"""

        llist = LinkedList()
        self.assertEqual(llist.length(), 0)

        llist.append("A")
        self.assertEqual(llist.length(), 1)

        llist.append("B")
        self.assertEqual(llist.length(), 2)

        llist.remove("A")
        self.assertEqual(llist.length(), 1)

        llist.remove("B")
        self.assertEqual(llist.length(), 0)

        llist.append("A")
        llist.append("B")
        llist.append("C")
        self.assertEqual(llist.length(), 3)

        llist.insert(2, "D")
        self.assertEqual(llist.length(), 4)

    def test_append(self):
        """append"""
        llist = LinkedList()
        self.assertEqual(repr(llist), "")

        llist.append("A")
        self.assertEqual(repr(llist), "A")

        llist.append("B")
        self.assertEqual(repr(llist), "A -> B")

        llist.append("C")
        llist.append("D")
        llist.append("E")

        self.assertEqual(repr(llist), "A -> B -> C -> D -> E")

    def test_prepend(self):
        """_summary_"""
        llist = LinkedList()
        self.assertEqual(repr(llist), "")

        llist.prepend("A")
        self.assertEqual(repr(llist), "A")

        llist.prepend("B")
        self.assertEqual(repr(llist), "B -> A")

        llist.prepend("C")
        llist.prepend("D")
        llist.prepend("E")

        self.assertEqual(repr(llist), "E -> D -> C -> B -> A")

    def test_insert(self):
        """insert"""
        llist = LinkedList()
        llist.insert(0, "A")

        self.assertEqual(repr(llist), "A")

        llist.insert(0, "B")
        self.assertEqual(repr(llist), "B -> A")

        llist.insert(1, "C")
        self.assertEqual(repr(llist), "B -> C -> A")

        llist.insert(1, "D")
        self.assertEqual(repr(llist), "B -> D -> C -> A")
        self.assertEqual(llist.length(), 4)

        llist.insert(3, "E")
        self.assertEqual(repr(llist), "B -> D -> C -> E -> A")
        self.assertEqual(llist.length(), 5)

        llist.insert(5, "F")
        self.assertEqual(repr(llist), "B -> D -> C -> E -> A -> F")
        self.assertEqual(llist.length(), 6)

        with self.assertRaises(IndexError):
            llist.insert(10, "F")

        llist = LinkedList()
        with self.assertRaises(IndexError):
            llist.insert(1, "F")

        llist = LinkedList()
        with self.assertRaises(IndexError):
            llist.insert(-1, "F")

    def test_delete_list(self):
        """delete list"""
        llist = LinkedList()
        llist.append("A")
        llist.append("B")
        llist.append("C")
        llist.append("D")
        self.assertEqual(repr(llist), "A -> B -> C -> D")

        llist.delete_list()
        self.assertEqual(repr(llist), "")
        self.assertTrue(llist.is_empty())

    def test_delete(self):
        """delete"""
        llist = LinkedList()
        llist.append("A")
        llist.append("B")
        llist.append("C")
        llist.append("D")

        self.assertEqual(repr(llist), "A -> B -> C -> D")

        llist.delete(1)
        self.assertEqual(repr(llist), "A -> C -> D")

        llist.delete(1)
        self.assertEqual(repr(llist), "A -> D")

        llist = LinkedList()
        llist.append("A")
        llist.append("B")
        llist.delete(1)
        self.assertEqual(repr(llist), "A")

        llist = LinkedList()
        llist.append("A")
        llist.append("B")
        llist.delete(0)
        self.assertEqual(repr(llist), "B")

        llist = LinkedList()
        llist.append("A")
        llist.append("B")
        llist.append("C")
        llist.delete(0)
        llist.delete(0)
        self.assertEqual(repr(llist), "C")

        with self.assertRaises(IndexError):
            llist.delete(10)

        llist = LinkedList()
        with self.assertRaises(IndexError):
            llist.delete(1)

        llist = LinkedList()
        with self.assertRaises(IndexError):
            llist.delete(-1)

    def test_remove(self):
        """remove"""

        llist = LinkedList()
        llist.append("A")
        llist.remove("A")
        self.assertEqual(repr(llist), "")

        llist = LinkedList()
        llist.append("A")
        llist.append("B")
        llist.remove("A")
        self.assertEqual(repr(llist), "B")

        llist = LinkedList()
        llist.append("A")
        llist.append("B")
        llist.remove("B")
        self.assertEqual(repr(llist), "A")

        llist = LinkedList()
        llist.append("A")
        llist.append("B")
        llist.append("C")
        llist.remove("B")
        self.assertEqual(repr(llist), "A -> C")

        llist = LinkedList()
        llist.append("A")
        llist.append("B")
        llist.append("C")
        llist.remove("A")
        llist.remove("C")
        self.assertEqual(repr(llist), "B")

        llist.remove("B")
        self.assertEqual(repr(llist), "")

        llist = LinkedList()
        llist.append("A")
        llist.append("B")
        llist.append("C")
        llist.remove("A")
        self.assertEqual(repr(llist), "B -> C")

    def test_reverse(self):
        """reverse"""

        llist = LinkedList()
        llist.reverse()

        self.assertEqual(repr(llist), "")

        llist = LinkedList()
        llist.append("A")
        llist.reverse()
        self.assertEqual(repr(llist), "A")

        llist = LinkedList()
        llist.append("A")
        llist.append("B")
        llist.reverse()
        self.assertEqual(repr(llist), "B -> A")

        llist.reverse()
        self.assertEqual(repr(llist), "A -> B")

        llist = LinkedList()
        llist.append("AA")
        llist.append("BB")
        llist.append("CC")
        llist.append("DD")
        self.assertEqual(repr(llist), "AA -> BB -> CC -> DD")

        llist.reverse()
        self.assertEqual(repr(llist), "DD -> CC -> BB -> AA")

        llist.reverse()
        self.assertEqual(repr(llist), "AA -> BB -> CC -> DD")
        llist.insert(2, "XX")
        self.assertEqual(repr(llist), "AA -> BB -> XX -> CC -> DD")
        llist.reverse()
        self.assertEqual(repr(llist), "DD -> CC -> XX -> BB -> AA")

    def test_find(self):
        """_summary_
        """

        llist = LinkedList()
        llist.append("A")
        llist.append("B")
        llist.append("C")
        llist.append("D")

        with self.assertRaises(IndexError):
            llist.find(-1)

        with self.assertRaises(IndexError):
            llist.find(100)

        self.assertEqual(llist.find(0), 'A')
        self.assertEqual(llist.find(2), 'C')

        llist.insert(2,"E")
        self.assertEqual(llist.find(2), 'E')
        self.assertEqual(llist.find(3), 'C')

        self.assertEqual(llist.find(3, from_end=True), 'B')
        self.assertEqual(llist.find(0, from_end=True), 'D')

    def test_contains(self):
        """contains
        """
        llist = LinkedList()
        llist.append("A")
        llist.append("B")
        llist.append("C")
        llist.append("D")

        self.assertTrue(llist.contains("A"))
        self.assertFalse(llist.contains("Z"))

        llist = LinkedList()
        self.assertFalse(llist.contains("Z"))

if __name__ == "__main__":
    unittest.main()
