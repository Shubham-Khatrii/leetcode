class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.min_stack=[]
        

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or self.min_stack[-1]>=val:
            self.min_stack.append(val)
        """
        :type val: int
        :rtype: None
        """
        

    def pop(self):
        if self.stack:
            val=self.stack.pop()
            if val==self.min_stack[-1]:
                self.min_stack.pop()
        """
        :rtype: None
        """
        

    def top(self):
        if self.stack:
            return self.stack[-1]
        """
        :rtype: int
        """
        

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]
        """
        :rtype: int
        """
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()