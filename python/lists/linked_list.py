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
        self.__head__ = None
        self.__tail__ = None
        self.__size__ = 0

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
        if at_index < 0 or at_index > self.__size__:
            raise IndexError(f'Idx {at_index} does not exiust')

        curr_idx = 0
        curr = self.__head__
        prev = None

        # move curr to desired index
        while curr is not None and curr_idx < at_index:
            prev = curr
            curr = curr.next
            curr_idx += 1

        return (prev, curr)

    def __repr__(self):
        tokens = []
        curr = self.__head__

        while curr is not None:
            arrow = "" if curr.next is None else " -> "
            tokens.append(curr.data)
            tokens.append(arrow)
            curr = curr.next

        return "".join(tokens)

    def is_empty(self):
        """True if the list is empty"""
        return self.__head__ is None

    def delete_list(self):
        """Delete the list"""
        self.__head__ = None
        self.__tail__ = None
        self.__size__ = 0

    def length(self) -> int:
        """the size of the linked list

        Returns:
            _type_: _description_
        """
        return self.__size__

    def append(self, data):
        """insert an element at the end of the list

        Args:
            data (_type_): _description_
        """
        new_node = Node(data)

        if self.__head__ is None:
            self.__head__ = new_node

        if self.__tail__ is not None:
            self.__tail__.next = new_node

        self.__tail__ = new_node
        self.__size__ += 1

    def prepend(self, data):
        """insert an element at the beginning of the list

        Args:
            data (_type_): _description_
        """
        new_node = Node(data)

        if self.__head__ is None:
            self.__head__ = new_node
        else:
            new_node.next = self.__head__
            self.__head__ = new_node

        self.__size__ += 1

    def remove(self, value):
        """remove

        Args:
            value (_type_): _description_
        """
        curr = self.__head__
        if self.is_empty():
            return

        found = False
        prev = None

        while not found and curr is not None:
            found = curr.data == value
            if found:
                # special cases
                if self.__head__ == curr:
                    self.__head__ = curr.next
                if self.__tail__ == curr:
                    self.__tail__ = prev
                if prev is not None:
                    prev.next = curr.next
            else:
                prev = curr
                curr = curr.next
        self.__size__ -= 1

    def insert(self, at_index: int, data):
        """insert at a given 0-based index

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

        self.__size__ += 1

    def delete(self, at_index: int):
        """delete at index

        Args:
            at_index (int): _description_
            data (_type_): _description_
        """
        if at_index == 0:
            self.__head__ = self.__head__.next
            self.__size__ -= 1
            return

        (prev, curr) = self.__move_to_index__(at_index)
        if curr is not None and prev is not None:
            prev.next = curr.next

        self.__size__ -= 1

    def reverse(self):
        """reverse

        Reverses the order of the nodes, w/o copying
        """

        if self.is_empty() or self.length() == 1:
            return

        head = self.__head__
        tail = self.__tail__

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

        self.__head__ = tail
        self.__tail__ = head

    def extend(self, at_index: int, data):
        raise NotImplementedError

    def count(self, value) -> int:
        raise NotImplementedError

    def contains(self, value) -> bool:
        """determines if an element is contained in a list

        Args:
            value (_type_): _description_

        Returns:
            bool: _description_
        """
        if self.is_empty():
            return False
        curr = self.__head__
        while curr is not None:
            if curr.data == value:
                return True
            curr = curr.next
        return False

    def find(self, at_index: int, from_end=False) -> str:
        try:
            if from_end:
                target_idx = (self.__size__ - at_index) - 1
            else:
                target_idx = at_index
            (_, curr) = self.__move_to_index__(target_idx)
            return curr.data
        except IndexError as exc:
            raise exc

