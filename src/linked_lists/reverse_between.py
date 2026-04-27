class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True

    def print_list(self):
        values = []
        temp = self.head
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        result = " -> ".join(values) if values else "Empty"
        print(result + " -> None")
        return result

    def make_empty(self):
        self.head = None
        self.length = 0

    def reverse_between(self, start_index, end_index):
        """
        A method reverses the nodes of the linked list from start_index to end_index
        (inclusive using 0-based indexing) in one pass and in-place.

        Parameters
        ----------
        start_index : int
            Index from where to start reversing the linked list.
        end_index : int
            Index from where to end reversing the linked
        """

        # if empty linked list, return None
        if self.head is None:
            return None

        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        idx_counter = 0

        # we need to stop the prev on the Node before the start_index
        while idx_counter < start_index:
            prev = prev.next
            idx_counter += 1
        else:
            current = prev.next
            for _ in range(end_index - start_index):
                to_move = current.next
                # print(
                #     f"Prev: {prev.value} | Current: {current.value} | to_move:{to_move.value}"
                # )
                current.next = to_move.next
                to_move.next = prev.next
                prev.next = to_move

        # at this point, place the head at the beginning of the linked list by replacing the dummy
        self.head = dummy.next

        return self.head


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# NOTE: video test cases
# # Reverse a sublist within the linked list
# linked_list.reverse_between(1, 3)
# print("Reversed sublist (1, 3): ")
# linked_list.print_list()

# # Reverse a sublist within the linked list
# linked_list.reverse_between(2, 4)
# print("Reversed sublist (2, 4): ")
# linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# # Reverse a sublist of length 1 within the linked list
# linked_list.reverse_between(3, 3)
# print("Reversed sublist of length 1 (3, 3): ")
# linked_list.print_list()

# # Reverse an empty linked list
# empty_list = LinkedList(0)
# empty_list.make_empty()
# empty_list.reverse_between(0, 0)
# print("Reversed empty linked list: ")
# empty_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Original linked list: 
    1 -> 2 -> 3 -> 4 -> 5 -> None
    Reversed sublist (2, 4): 
    1 -> 2 -> 5 -> 4 -> 3 -> None
    Reversed entire linked list: 
    3 -> 4 -> 5 -> 2 -> 1 -> None
    Reversed sublist of length 1 (3, 3): 
    3 -> 4 -> 5 -> 2 -> 1 -> None
    Reversed empty linked list: 
    Empty -> None
    
"""
