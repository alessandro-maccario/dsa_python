class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True


def find_kth_from_end(ll, k):
    """
    Return the kth Node from the end of the linked list.

    Parameters
    ----------
    ll : LinkedList
        The linked list from where to find the corresponding node.
    k : int
        The integer corresponding to the kth Node to return.

    Explanation:
    1. Move "fast" kth time.
    2. Move "slow" 1 at a time.
    3. Once "fast" is None, return "slow", this is your pointer to the node that is kth Node from the end of the linked list.
    """
    # Base conditions: if k < 0 and if ll.head is an empty linked list
    if k < 0 or ll.head is None:
        return None

    fast = ll.head  # you are referring to head at the very beginning
    slow = ll.head
    # needed to see if k > length of the linked list
    counter = 0

    for _ in range(k):
        fast = fast.next
        counter += 1
        if fast is None and counter < k:
            return None

    while fast is not None:
        slow = slow.next
        if slow.next is None:
            return slow
        fast = fast.next
    else:
        return None

    return slow


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

k = 0
result = find_kth_from_end(my_linked_list, k)
print(result.value)

# print(result.value)  # Output: 4


"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""
