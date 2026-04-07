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
        # 1. Traverse the Linked list and pop the last element and return it
        # 2. the previous node will have a .next = None and the tail equal to the previous node

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

        node = self.head

        # while the next node is still not None
        while node.next is not None:
            # keep track of the previous node
            current_node = node
            print(
                "Current node:",
                current_node.value if current_node is not None else current_node,
            )
            node = node.next
        else:
            print("Current node:", node.value if node is not None else node)
            popped_node = node
            current_node.next = None
            self.tail = current_node

            print("Next node:", node.next if node is not None else node)
            print("---------")

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
