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

    def get(self, index):
        """
        Return the node at the specified index.
        The get method should take an integer index as a parameter and return a pointer to the node at the specified index in the linked list.

        Parameters
        ----------
        index : int
            An integer index as a parameter.

        Returns
        -------
        Node
            Return a pointer to the node at the specified index in the linked list.
        """
        ##############
        # Edge cases #
        # in case the index is out of bounds (less than 0 or greater than or equal to the length of the list), the method should return None.
        if index < 0 or index >= self.length:
            return None

        ##############
        current_index = 0

        # Traverse the Singly Linked List
        current_node = self.head

        # if the index is the 0th index, return the head
        if current_index == index:
            return current_node
        else:
            while current_node.next is not None:
                # move the pointer to the next node
                current_node = current_node.next
                # increment the current_index to be used for evaluation against the index
                current_index += 1
                if current_index == index:
                    return current_node
                else:
                    continue

        return current_node

    def set_value(self, index, value):
        """
        The set method replaces the element at the specified position in a LinkedList with a new element.

        Parameters
        ----------
        index : int
            Index of the Node to be set to a different value.
        value : int
            The value to be used for setting the current Node.

        Returns
        -------
        int
            The value of the Node before setting it to a different value.
        """
        ##############
        # Edge cases #
        # in case the index is out of bounds (less than 0 or greater than or equal to the length of the list), the method should return None.
        if index < 0 or index >= self.length:
            return None
        ##############

        # if the current_index is the 0th one, then replace that value immediately
        current_index = 0
        # Traverse the Singly Linked List
        current_node = self.head

        # if the index is the 0th index, return the head
        if current_index == index:
            # replace the current value with the replacement input
            current_node.value = value
            return current_node
        else:
            for _ in range(index):
                if current_node.next is not None:
                    # until the index has not been found, keep proceding forward in the Singly Linked List
                    current_node = current_node.next
            # replace the current value with the replacement input
            current_node.value = value

        return True

    def insert(self, index, value):
        """
        Insert a new node into the Singly Linked List.

        Parameters
        ----------
        index : int
            The index at which you want to insert a new Node.
        value : int
            The Node to be inserted at the specified index.

        Returns
        -------
        bool
        """
        # Create the new node
        new_node = Node(value=value)
        ##############
        # Edge cases #

        # in case the index is out of bounds (less than 0 or greater than or equal to the length of the list), the method should return None.
        if index < 0 or index > self.length:
            return False
        # if the list is empty, add the new node
        if self.length == 0:
            return self.append(value=value)
        # if the length of the list is the same as the index, then we just want to append the Node
        if self.length == index:
            return self.append(value=value)
        # if the index is the 0th index, place the new node before the head
        if index == 0:
            return self.prepend(value=value)

        ##############

        # Traverse the Singly Linked List
        current_node = self.head

        # to insert at a certain index, you need to loop through all the indexes - 1
        for _ in range(index - 1):
            if current_node.next is not None:
                # until the index has not been found, keep proceding forward in the Singly Linked List
                current_node = current_node.next
        # the new node.next will point to the next to the current
        new_node.next = current_node.next
        current_node.next = new_node

        self.length += 1

        return True

    def remove(self, index):
        """
        Remove an item from the Singly Linked List at a specified index.

        Parameters
        ----------
        index : int
            The index from the item must be removed.

        Returns
        -------
        Node
            Return the Node that has been removed.
        """
        ##############
        # Edge cases #
        # In case the index is out of bounds (less than 0 or greater than or equal to the length of the list), the method should return None, as well as if the list is empty, cannot remove any item
        if index < 0 or index >= self.length or self.length == 0:
            return None
        # if the index is the 0th index, place the new node before the head
        if index == 0:
            return self.pop_first()
        if self.length == index:
            return self.pop()
        ##############

        # Traverse the Singly Linked List
        current_node = self.head

        # to insert at a certain index, you need to loop through all the indexes - 1
        for _ in range(index):
            previous_node = current_node
            if current_node.next is not None:
                # until the index has not been found, keep proceding forward in the Singly Linked List
                current_node = current_node.next
        # the new node.next will point to the next to the current, successfully removing the node at the specified index
        previous_node.next = current_node.next
        current_node.next = None

        # decrement the amount of elements in the list
        self.length -= 1

        return current_node

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
# print(linked_list.append(value=0))
# print(linked_list.append(value=1))
# print(linked_list.append(value=2))
# print(linked_list.append(value=3))
# # print(linked_list)
# # print(linked_list.get(index=1).value)
# # print(linked_list.set_value(index=1, value=100))
# # print(linked_list)
# print(linked_list.insert(index=3, value=4))
# print(linked_list)
print(linked_list.append(1))
print(linked_list.append(3))


print("LL before insert():")
print(linked_list)

print(linked_list.insert(1, 2))

print("\nLL after insert(2) in middle:")
print(linked_list)

print(linked_list.insert(0, 0))

print("\nLL after insert(0) at beginning:")
print(linked_list)

print(linked_list.insert(4, 4))

print(linked_list.remove(index=5))

print("\nLL after removing element at index:")
print(linked_list)
