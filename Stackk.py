
'''

Author - Shaunak Deshmukh

This program creates a class stack that has few methods as below.
Create an object of the stack,push few elements and exercise other methods.

'''




class Stack:
    def __init__(self):
        self.items=[]
    
    def isempty(self):
        return self.items==[]
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
s=Stack()
s.push('3')
s.push('4')
s.push('3')
s.push('3')
print(s.size())
print(s.isempty())
print(s.peek())
