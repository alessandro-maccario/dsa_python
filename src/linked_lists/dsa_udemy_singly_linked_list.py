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
        # if only one node is available
        elif self.length == 1:
            # save the element to be popped before pointing the head to None
            node = self.head
            self.head = None
            self.tail = None
            self.length -= 1

            return node

        ##############
        # Two-Pointer Technique
        temp = self.head
        previous = self.head

        while temp.next is not None:
            previous = temp
            temp = temp.next
        else:
            self.tail = previous
            self.tail.next = None

        # remove 1 to the total length
        self.length -= 1
        # return the last node that was popped from the linked list
        return temp if temp is not None else None

    def prepend(self, value):
        """
        Prepend a value to a Singly Linked List.

        Parameters
        ----------
        value : int
            The value to append as a new node at the beginning of the Singly Linked List.
        """

        # Create the new node
        new_node = Node(value=value)

        ##############
        # Edge cases #
        ##############
        # in case the Linked List is empty, the node will create the Singly Linked List
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.tail.next = None
        else:
            ##################
            # Standard cases #
            ##################
            new_node.next = self.head
            self.head = new_node

        # increment the length by 1
        self.length += 1
        return True

    def pop_first(self):
        """
        Pop the first element of the Singly Linked List.

        Returns
        -------
        int
            The first element of the Singly Linked List.
        """
        ##############
        # Edge cases #

        # in case the Linked List is empty, cannot pop anything
        if self.length == 0:
            return None
        # if only one node is available
        elif self.length == 1:
            # save the element to be popped before pointing the head to None
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1

            return temp

        ##################
        # Standard cases #
        ##################
        # Save the node to be popped and to be returned
        first_node = self.head
        # Point the head to the next node, resulting in removing the the first node
        self.head = self.head.next
        # detach the first from the rest of the Singly Linked List
        first_node.next = None

        # decrement the counter by 1
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return first_node

    # TODO: continue from here
    def get(self, index):
        pass

    def print_list(self):
        node = self.head

        while node is not None:
            print(node.value, "\n")
            node = node.next

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
# linked_list.append(value=25)
# linked_list.append(value=40)
# linked_list.append(value=50)
# pop and print the value
# print(linked_list.pop().value)
print(linked_list.append(value=10))
print(linked_list.append(value=20))
print(linked_list)
print(linked_list.pop_first())
print(linked_list.pop_first())
print(linked_list.pop_first())

# 4. Check if the new node has been added to the linked list
print(linked_list)
