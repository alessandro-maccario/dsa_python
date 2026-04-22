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
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def partition_list(self, x):
        """
        This method partitions the list such that all nodes with values less than x
        come before nodes with values greater than or equal to x.


        Parameters
        ----------
        x : int
            Threshold value.

        Returns
        -------
        Linked List: obj
            Return the concatenated linked list.

        Examples
        --------
        Example 1:
        Input:
        Linked List: 3 -> 8 -> 5 -> 10 -> 2 -> 1 x: 5

        Output:
        Linked List: 3 -> 2 -> 1 -> 8 -> 5 -> 10

        Example 2:
        Input:
        Linked List: 1 -> 4 -> 3 -> 2 -> 5 -> 2 x: 3

        Output:
        Linked List: 1 -> 2 -> 2 -> 4 -> 3 -> 5
        """
        # dummy1 = for elements smaller than x
        dummy1 = Node(0)
        # dummy2 = for elements greater than x
        dummy2 = Node(0)
        prev1 = dummy1
        prev2 = dummy2

        current = self.head
        if current is None:
            return

        while current is not None:
            print(current.value)
            if current.value < x:
                prev1.next = current
                prev1 = current
            else:
                prev2.next = current
                prev2 = current

            current = current.next

        # severe the connection that is still available in the last node of the second list, otherwise you will cause an infinite loop
        prev2.next = None
        # once finished, the prev1 will be connected to the same node as dummy2.next to be able to reconnect the current and the next node
        prev1.next = dummy2.next
        # point the head to the dummy1 to remove the influence of dummy1 on the linked list
        self.head = dummy1.next

        return self.head

    #   +===================================================+
    #   |               WRITE YOUR CODE HERE                |
    #   | Description:                                      |
    #   | - This method partitions a linked list around a   |
    #   |   value `x`.                                      |
    #   | - It rearranges the nodes so that all nodes less  |
    #   |   than `x` come before all nodes greater or equal |
    #   |   to `x`.                                         |
    #   |                                                   |
    #   | Tips:                                             |
    #   | - We use two dummy nodes, `dummy1` and `dummy2`,  |
    #   |   to build two separate lists: one for elements   |
    #   |   smaller than `x` and one for elements greater   |
    #   |   or equal to `x`.                                |
    #   | - `prev1` and `prev2` help us keep track of the   |
    #   |   last nodes in these lists.                      |
    #   | - Finally, we merge these two lists by setting    |
    #   |   `prev1.next = dummy2.next`.                     |
    #   | - The head of the resulting list becomes          |
    #   |   `dummy1.next`.                                  |
    #   +===================================================+


#  +=====================================================+
#  |                                                     |
#  |          THE TEST CODE BELOW WILL PRINT             |
#  |              OUTPUT TO "USER LOGS"                  |
#  |                                                     |
#  |  Use the output to test and troubleshoot your code  |
#  |                                                     |
#  +=====================================================+


# Function to convert linked list to Python list
def linkedlist_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result


# Function to test partition_list
def test_partition_list():
    test_cases_passed = 0

    print("-----------------------")

    # Test 1: Partition in Middle
    print("Test 1: Partition in Middle")
    x = 5
    print(f"x = {x}")
    ll = LinkedList(5)
    for i in [8, 3, 10, 2, 4]:
        ll.append(i)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [3, 2, 4, 5, 8, 10]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 2: Partition at Start
    print("Test 2: Partition at Start")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(5)
    for i in [8, 3, 10, 2, 4]:
        ll.append(i)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [2, 5, 8, 3, 10, 4]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 3: Partition at End
    print("Test 3: Partition at End")
    x = 11
    print(f"x = {x}")
    ll = LinkedList(5)
    for i in [8, 3, 10, 2, 4]:
        ll.append(i)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [5, 8, 3, 10, 2, 4]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 4: Empty List
    print("Test 4: Empty List")
    x = 5
    print(f"x = {x}")
    ll = LinkedList(1)
    ll.make_empty()
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if ll.head is None:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 5: All Greater or Equal
    print("Test 5: All Greater or Equal")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(5)
    for i in [6, 7, 8]:
        ll.append(i)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [5, 6, 7, 8]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 6: Single Element
    print("Test 6: Single Element")
    x = 5
    print(f"x = {x}")
    ll = LinkedList(4)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [4]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 7: Duplicates Equal to x
    print("Test 7: Duplicates Equal to x")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    for i in [1, 3, 2, 3]:
        ll.append(i)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 2, 3, 3, 3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Test 8: Already Partitioned
    print("Test 8: Already Partitioned")
    x = 5
    print(f"x = {x}")
    ll = LinkedList(1)
    for i in [2, 5, 8, 10]:
        ll.append(i)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 2, 5, 8, 10]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    # Summary
    print(f"{test_cases_passed} out of 8 tests passed.")


# Run the test function
test_partition_list()
