class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = head

    def length(self):
        # Check if the list is empty
        if not self.head:
            return 0

        counter = 1
        current_node = self.head

        while current_node.next:  # as long as it is not null
            counter += 1
            current_node = current_node.next

        return counter

    def append(self, value):
        if self.head is None:
            self.head = Node(value=value)
        else:
            # If we already have a head, let's traverse the linked list and find which is the last element to append to
            # I always need to traverse the linked list starting from the head
            last = self.head
            # while a next value does exists, then the last element will be equal to that next value
            while last.next:
                last = last.next
            last.next = Node(value=value)

    def prepend(self, value):
        # 1. create a new node
        # 2. make this new node poiting to the head
        # 3. make this node the new head
        first_node = Node(value=value)
        first_node.next = self.head
        self.head = first_node

    def insert(self, value, index):
        # if the index is the first one, then prepend
        if index == 0:
            self.prepend(value=value)
        else:
            # Exception handling: if the head does not exist, the linked list is empty. Raise a ValueError
            if self.head is None:
                raise IndexError("Index out of bounds")
            else:
                # if the head is not None
                last = self.head

                # Then, we iterate through the linked list
                for i in range(
                    index - 1
                ):  # index - 1 because we want to go before the next element to insert the new node
                    if last.next is None:
                        # Raise an error becuase it means that
                        raise IndexError("Index out of bounds")
                    last = last.next

                new_node = Node(value=value)
                new_node.next = last.next
                last.next = new_node

    def search(self, value):
        """
        Search for a specific value in the Linked List.

        Parameters
        ----------
        value : int
            An integer to be search on in a Linked List.

        Returns
        -------
        str
            A string representation of the output: either the value has been found at a specific index or not.
        """
        # Check if the list is empty
        if not self.head:
            return "List is empty"

        # initial index: if the head is the same as the value, the idx is 0. Otherwise, increment it.
        idx = 0

        if self.head.value == value:
            return f"Value {value} at index {idx}"
        else:
            current_node = self.head
            while current_node:
                if current_node.value == value:
                    return f"Value {value} at index {idx}"
                # If value not yet found, move the current node pointer and increment the index
                current_node = current_node.next
                idx += 1
            return "Value not found"

    def delete(self, value):
        dummy = Node(value=0)
        dummy.next = self.head

        previous_node = dummy

        # while the current node value is not the same as value, move the previous and the next pointers
        while previous_node.next:
            if previous_node.next.value != value:
                previous_node = previous_node.next
            else:
                # Modify the pointers from the previous node and the current node: the previous goes to the next one and the current to None
                previous_node.next = previous_node.next.next

        # update the head
        self.head = dummy.next

        return self.head

    def delete2(self, value):
        dummy = Node(value=0)
        dummy.next = self.head

        iteration = 0

        current_node = dummy
        while current_node.next:
            iteration += 1

            if current_node.next.value != value:
                print(
                    f"Iteration {iteration} | Current value: {current_node.value} | Next value: {current_node.next.value}"
                )

                current_node = current_node.next
            else:
                print(
                    f"Iteration {iteration} | Current value: {current_node.value} | Next value: {current_node.next.value}"
                )
                current_node.next = current_node.next.next

        # Once you reach the end, you can only display None as next value
        print(
            f"Final Step -> Current value: {current_node.value} | Next value: {current_node.next}"
        )
        self.head = dummy.next

        return self.head

    def pop(self, index):
        """
        Pop an element based on index.

        Parameters
        ----------
        index : int
            Value at which to pop the element.

        Returns
        -------
        int
            The element popped from the Linked List.
        """
        dummy = Node(value=0)
        dummy.next = self.head

        if index == 0:
            self.head = self.head.next
            return

        previous_node, current_node = dummy, self.head

        idx = 0
        while current_node:  # until the next pointer is not None
            if idx == index:
                # pop the value at the current index and return it. First change the next pointer to the next.next value
                print(
                    f"Value at idx {idx} is {current_node.value} | Searched index is: {index} | Previous node: {previous_node.value}"
                )
                previous_node.next = current_node.next
                return
            else:
                print(
                    f"Current idx is: {idx} | Current value is: {current_node.value} | Searched index is: {index} | Previous node: {previous_node.value}"
                )
                idx += 1
                current_node = current_node.next
                previous_node = previous_node.next

    def get(self, index):
        dummy = Node(value=0)
        dummy.next = self.head

        if index == 0:
            self.head = self.head.next
            return

        current_node = self.head

        idx = 0
        while current_node:  # until the next pointer is not None
            if idx == index:
                # pop the value at the current index and return it. First change the next pointer to the next.next value
                return current_node.value
            else:
                idx += 1
                current_node = current_node.next

    def traverse(self):
        """
        Traverse the list and display it.
        """
        current_node = self.head

        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next

        print("null")


# create instance of the class and nodes
# pass the entire existing node chain as the head so that any changes will be flowing on the same LinkedList
linked_list = LinkedList()
linked_list.append(value=2)
linked_list.append(value=5)
linked_list.append(value=19)
linked_list.append(value=20)
linked_list.append(value=7)

# print("---------")
# print("Original:")
# linked_list.traverse()
# print("---------")
# linked_list.pop(index=4)
# print("After Popping out the value:")
# linked_list.traverse()
# print(linked_list.get(index=44))
