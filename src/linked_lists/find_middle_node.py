from typing import Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        """
        Append a node to the end of a Linked List.

        Parameters
        ----------
        value : int
            Integer to append to the Linked List.
        """
        # 1. Create a new node
        new_node = Node(value=value)

        # in case the Linked List is empty just point to the new node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # 2. Point the tail.next and tail to the new node
            self.tail.next = new_node
            self.tail = new_node
        return True

    def find_middle(self) -> bool:
        """
        Given a linked list, find the middle value.
        No length attribute is given and the list can be traversed only once.

        Parameters
        ----------
        head : Optional[Node]
            The head of the linked list.

        Returns
        -------
        Node
            The middle Node.

        Examples
        --------
        Example 1
        Input: head = [1, 2, 3, 4, 5]
        Output: 3

        Example 2
        Input: head = [1, 2, 3, 4]
        Output: 3
        """
        current = self.head
        after = self.head

        while after is not None and after.next is not None:
            after = after.next.next
            current = current.next

        return current

    def __repr__(self) -> str:
        """
        Create custom representation of the Linked List.

        Returns
        -------
        str
            The string representation of the Linked List
        """

        node = self.head
        nodes = []

        while node is not None:
            nodes.append(str(node.value))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


#################
### TEST CASE ###
#################

# Create Linked List and Nodes
linked_list = LinkedList()
print(linked_list.append(1))
print(linked_list.append(2))
print(linked_list.append(3))
print(linked_list.append(4))
print(linked_list.append(5))
# Print the linked list
print(linked_list)

# Apply the find_middle method: it should return the middle value
print(linked_list.find_middle().value)
