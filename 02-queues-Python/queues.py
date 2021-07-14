"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""

class Queue:
    def _init_(self, head=None):
        self.list = [head]


    def enqueue(self, new_element):
        return self.list.append(new_element)

    def dequeue(self):
        return self.list.pop(0)

    def peek(self):
        return (self.list[0])