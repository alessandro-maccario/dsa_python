class MyQueue(object):
    def __init__(self):
        self.queue = []

    def push(self, x) -> None:
        """
        Insert/Enqueue an element at the rear/back of the queue.

        Parameters
        ----------
        x : object
            An element to push into the stack.

        Return
        ------
        None
        """
        self.queue.append(x)

    def pop(self):
        """
        Pop/Dequeue and return the first element of the queue if not empty, else None.

        Returns
        -------
        x: object | None
            Either return the object popped from the front of the stack.
        """
        if self.queue:
            return self.queue.pop(0)
        else:
            return None

    def peek(self):
        """
        Return the first element of the queue (FIFO) if the queue is not empty, else None.

        Returns
        -------
        x: object | None
            Return either the first element in the stack or None if the stack is empty.
        """
        if self.queue:
            return self.queue[0]
        else:
            return None

    def empty(self) -> bool:
        """
        Return True if the queue is empty. Return False if the queue is not empty.

        Returns
        -------
        bool
            Return True if the queue is not empty, otherwise False.
        """
        return not self.queue


#################
### TEST CASE ###
#################

x = 3

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(x)
print(obj.peek())
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
print(param_2)
print(param_3)
print(param_4)
