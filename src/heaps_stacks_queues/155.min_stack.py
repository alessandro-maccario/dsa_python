class MinStack:
    """
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    Implement the MinStack class:
    - MinStack() initializes the stack object.
    - void push(int val) pushes the element val onto the stack.
    - void pop() removes the element on the top of the stack.
    - int top() gets the top element of the stack.
    - int getMin() retrieves the minimum element in the stack.

    You must implement a solution with O(1) time complexity for each function.

    Examples
    --------
    Example 1:

    Input
    ["MinStack","push","push","push","getMin","pop","top","getMin"]
    [[],[-2],[0],[-3],[],[],[],[]]

    Output
    [null,null,null,null,-3,null,0,-2]

    Explanation
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin(); // return -3
    minStack.pop();
    minStack.top();    // return 0
    minStack.getMin(); // return -2
    """

    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, val: int) -> None:
        """
        Push a value to the stack and the minimum stack to keep them in sync.

        Parameters
        ----------
        val : int
            Value to be appended to the stack.
        """
        self.stack.append(val)
        # if the self.minimum is empty, append first value
        if not self.minimum:
            self.minimum.append(val)
        else:
            if self.minimum[-1] > val:
                self.minimum.append(val)
            else:
                self.minimum.append(self.minimum[-1])

    def pop(self) -> None:
        """
        Remove value from the stack and the minimum stack.
        """
        self.stack.pop(-1)
        self.minimum.pop(-1)

    def top(self) -> int:
        """
        Peek at the top of the stack.

        Returns
        -------
        int
            Value at the top of the stack.
        """
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        """
        The minimum value corresponds to the minimum value of the stack at that specific point in time.

        Returns
        -------
        int
            Minimum value of the stack.
        """
        if self.minimum:
            return self.minimum[-1]
        else:
            return None


#################
### TEST CASE ###
#################

# Your MinStack object will be instantiated and called as such:
val_1 = -2
val_2 = 0
val_3 = -3
obj = MinStack()
print(f"Current stack: {obj}")
obj.push(val_1)
obj.push(val_2)
obj.push(val_3)
print(obj.minimum)
print("Get Min:", obj.getMin())
# print("Get Top:", obj.top())
obj.pop()
print("Top Object:", obj.top())
# print(obj.minimum)
print("Get Min:", obj.getMin())
print("Minimum list:", obj.minimum)

# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
