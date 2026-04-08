class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

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
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            # 2. Point the tail.next and tail to the new node
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        """
        Pop method to pop the last element in a Singly Linked List.

        Approach:
            1. Traverse the Linked list and pop the last element; return it
            2. The previous to last node will have a .next = None and the tail will be set equal to the previous node (moving the tail back one node)

        Returns
        -------
        int
            Popped element from the Singly Linked List.
        """

        ##############
        # Edge cases #

        # in case the Linked List is empty, cannot pop anything
        if self.length == 0:
            return None
        elif self.length == 1:
            # save the element to be popped
            node = self.head
            self.head = None
            self.tail = None

            return node

        ##############
        # Two-Pointer Technique
        temp = self.head
        previous = self.head

        while temp.next is not None:
            previous = temp
            temp = temp.next
        else:
            popped_node = temp
            previous.next = None
            self.tail = previous

        # remove 1 to the total length
        self.length -= 1
        # return the popped node
        return popped_node

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


# Create Linked List and Nodes
linked_list = LinkedList()

# Append a new node
linked_list.append(value=25)
linked_list.append(value=40)
linked_list.append(value=50)
# pop and print the value
print(linked_list.pop().value)

# 4. Check if the new node has been added to the linked list
print(linked_list)
