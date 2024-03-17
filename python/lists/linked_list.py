from typing import Tuple


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"

    def __str__(self):
        return f"{self.data}"


class LinkedList:
    """LinkedList"""

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        """True if the list is empty"""
        return self.head is None

    def length(self) -> int:
        """the size of the linked list

        Returns:
            _type_: _description_
        """
        return self.size

    def append(self, data):
        """insert an element at the end of the list

        Args:
            data (_type_): _description_
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node
        self.size += 1

    def prepend(self, data):
        """insert an element at the beginning of the list

        Args:
            data (_type_): _description_
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.size += 1

    def remove(self, value):
        """remove

        Args:
            value (_type_): _description_
        """
        curr = self.head
        if self.is_empty():
            return

        found = False
        prev = None

        while not found and curr is not None:
            found = curr.data == value
            if found:
                # special cases
                if self.head == curr:
                    self.head = curr.next
                if self.tail == curr:
                    self.tail = prev
                if prev is not None:
                    prev.next = curr.next
            else:
                prev = curr
                curr = curr.next
        self.size -= 1

    def __move_to_index__(self, at_index: int) -> Tuple[Node, Node]:
        """_summary_

        Args:
            at_index (int): _description_

        Raises:
            IndexError: _description_
            IndexError: _description_

        Returns:
            Tuple[Node, Node]: prev, curr nodes
        """
        if at_index < 0:
            raise IndexError

        curr_idx = 0
        curr = self.head
        prev = None

        # move curr to desired index
        while curr is not None and curr_idx < at_index:
            prev = curr
            curr = curr.next
            curr_idx += 1

        if curr_idx < at_index:
            raise IndexError

        return (prev, curr)

    def insert(self, at_index: int, data):
        """insert

        Args:
            at_index (int): _description_
            data (_type_): _description_
        """
        # no need to calculate anything
        if at_index == 0:
            self.prepend(data)
            return

        try:
            (prev, curr) = self.__move_to_index__(at_index)
        except IndexError as exc:
            raise exc

        new_node = Node(data)
        if curr is not None:
            new_node.next = curr

        if prev is not None:
            prev.next = new_node

        self.size += 1

    def delete(self, at_index: int):
        """delete at index

        Args:
            at_index (int): _description_
            data (_type_): _description_
        """
        if at_index == 0:
            self.head = self.head.next
            self.size -= 1
            return

        (prev, curr) = self.__move_to_index__(at_index)
        if curr is not None and prev is not None:
            prev.next = curr.next

        self.size -= 1

    def reverse(self):
        """reverse

        Reverses the order of the nodes, w/o copying
        """

        if self.is_empty() or self.length() == 1:
            return

        head = self.head
        tail = self.tail

        # we now now we have at least 2 nodes to swap
        prev = None
        curr = head
        next_node = curr.next

        while next_node is not None:
            print(f"Processing {self}")
            curr.next = prev
            prev = curr
            curr = next_node
            if next_node is not None:
                next_node = next_node.next
            print(f"Result {self}")

        curr.next = prev

        self.head = tail
        self.tail = head

    def extend(self, at_index: int, data):
        raise NotImplementedError

    def count(self, value) -> int:
        raise NotImplementedError

    def __repr__(self):
        tokens = []
        curr = self.head

        while curr is not None:
            arrow = "" if curr.next is None else " -> "
            tokens.append(curr.data)
            tokens.append(arrow)
            curr = curr.next

        return "".join(tokens)
