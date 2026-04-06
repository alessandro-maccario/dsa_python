class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        # The constructor creates a new node
        new_node = Node(value)
        # attach the head of the linked list to the current new node
        self.head = new_node
        # attach the tail of the linked list to the current new node
        self.tail = new_node
        # we are gonna keep track of the length
        self.length = 1


# Create nodes
node1 = Node(11)
node2 = Node(3)
node3 = Node(23)
node4 = Node(7)
# Link nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None

# Head points to the first node and tail to the last one
head = node1
tail = node4


print(tail.next)


def print_list(head):
    temp = head
    while (
        temp is not None
    ):  # until we haven't reach the end of the list, we print the value
        print(temp.value)
        temp = temp.next


#########################
### Append a new node ###
#########################

# 1. Create a new node
new_node = Node(5)

# 2. Point the last node to the new node
node4.next = new_node

# 3. Point the tail to the new node
tail.next = new_node


# 4. Check if the new node has been added to the linked list
print_list(head=head)
