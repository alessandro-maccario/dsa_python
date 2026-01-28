class Node:
    def __init__(self, value):
        # actual value of the node
        self.value = value
        # reference to the next node
        self.next = None
        # reference to the previous node
        self.previous = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def traverse(self):
        """
        Traverse the list and display it.
        """
        current_node = self.head

        while current_node:
            print(current_node.value, end=" ⇄ ")
            current_node = current_node.next

        print("null")

    def length(self):
        """
        Count the length of the doubly linked list.
        """
        counter = 0
        current_node = self.head

        while current_node:
            counter += 1
            current_node = current_node.next

        return counter

    def append(self, value):
        if self.head is None:
            self.head = Node(value=value)
            # if there is only one node, the head and tail reference to the only node available
            # self.head → [5] ← self.tail
            #              ↓
            #             None
            self.tail = self.head
        else:
            # If we already have a head, let's traverse the linked list and find which is the last element to append to
            # I always need to traverse the linked list starting from the head
            # self.head → [5] ⇄ [9] ← self.tail
            # 1. Create the new node that need to be placed at the end of the list
            last_node = Node(value=value)
            # 2. This means that you are setting the last_node.previous to be referencing the same NODE that the self.tail is referencing. Note: we are talking about references/pointers in here
            # self.head → [5] ⇄ [10] ← self.tail
            #                     ↑
            #                    [15]
            last_node.previous = self.tail
            # 3. Move the tail.next POINTER to reference the newly created node
            self.tail.next = last_node
            # 4. Move the tail itself to point to the newly created node
            self.tail = last_node

    def prepend(self, value):
        """
        Prepend a value to the doubly linked list.

        Parameters
        ----------
        value : int
            An integer to be appended to the doubly linked list.
        """
        # edge case: if the head is None
        if self.head is None:
            self.head = Node(value=value)
            self.tail = self.head
        else:
            # 1. Create the new node to prepend
            new_node = Node(value=value)
            # 2. Let the next pointer of the new node point to the same reference (the node) that the head is currently pointing to
            new_node.next = self.head
            # 2. Let the head previous pointer point to the new node
            self.head.previous = new_node
            # 3. Let the head element point to the new node
            self.head = new_node

    # TODO: to be done
    def insert(self, index, value):
        """
        Insert a value in a doubly linked list.

        Parameters
        ----------
        index : int
            The index at which the value will be inserted.

        value : int
            Value to be inserted.
        """
        length = self.length()
        print("Index is:", index)
        if index > length - 1 or index < 0:
            return ValueError("Index Out of bounds")

        current_node = self.head
        # if you want to insert a value at index 0, then prepend
        if index == 0:
            self.prepend(value=value)
            return

        # In all of the other cases, you need to insert a value somewhere in the middle of the linked list

        # if you want to insert a value at the last position of the doubly linked list (for this
        # you would have to traverse the doubly linked list), then it's append.

        # Insert at the end of the Doubly Linked List using the append method
        if length == index:
            for i in range(length):
                if current_node.next is None:
                    self.append(value=value)
                current_node = current_node.next
            return

        # Insert at a specific index: continue to update the current_node pointer until index - 1 has been reached
        for i in range(index - 1):
            current_node = current_node.next
        # go through the doubly linked list until the previous node, then do the switch
        new_node = Node(value=value)
        new_node.next = (
            current_node.next
        )  # the new_node.next will point at the same element as the currrent_node.next
        new_node.previous = current_node.next
        current_node.next = new_node

    def delete(self, value):
        """
        Delete a value from the doubly linked list.

        Parameters
        ----------
        value : int
            An integer to be deleted.
        """
        current_node = self.head
        # 1. if the element to be deleted is only the head

        # 2. if the element to be deleted is the tail

        # 3. if the element to be deleted is anywhere in the linked list
        while current_node.next:
            if current_node.next.value != value:
                current_node = current_node.next
            else:
                current_node.next = current_node.next.next
                return


doubly_linked_list = DoublyLinkedList()
doubly_linked_list.append(value=2)
doubly_linked_list.append(value=5)
doubly_linked_list.append(value=19)
doubly_linked_list.append(value=20)
doubly_linked_list.append(value=78)
doubly_linked_list.prepend(value=100)
doubly_linked_list.prepend(value=500)
doubly_linked_list.traverse()
print(doubly_linked_list.length())
doubly_linked_list.insert(index=2, value=-3)
doubly_linked_list.traverse()
print(doubly_linked_list.length())
doubly_linked_list.delete(value=2)
doubly_linked_list.traverse()
