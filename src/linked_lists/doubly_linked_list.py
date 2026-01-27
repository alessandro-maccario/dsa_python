class NodeDoublyLinkedList:
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
            print(current_node.value, end=" -> ")
            current_node = current_node.next

        print("null")

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
            last_node = NodeDoublyLinkedList(value=value)
            # 2. This means that you are setting the last_node.previous to be referencing the same NODE that the self.tail is referencing. Note: we are talking about references/pointers in here
            # self.head → [5] ⇄ [10] ← self.tail
            #                     ↑
            #                    [15]
            last_node.previous = self.tail
            # 3. Move the tail.next POINTER to reference the newly created node
            self.tail.next = last_node
            # 4. Move the tail itself to point to the newly created node
            self.tail = last_node


doubly_linked_list = DoublyLinkedList()
doubly_linked_list.append(value=2)
doubly_linked_list.append(value=5)
doubly_linked_list.append(value=19)
doubly_linked_list.append(value=20)
doubly_linked_list.append(value=78)
doubly_linked_list.traverse()
