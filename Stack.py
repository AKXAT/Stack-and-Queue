from collections import deque
class Stack:
    def __init__(self):
        self.bucket = deque()
    def push(self,value):
        self.value = value 
        self.bucket.append(value)
    def pop(self): 
        #print(self.bucket.pop())
        return self.bucket.pop()
    def last_inserted_value(self):
        #print(self.bucket[-1])
        return self.bucket[-1]
    def is_empty(self):
        if len(self.bucket)==0:
            #print("True")
            return True 
        else :
            #print(len(self.bucket))
            return len(self.bucket)

if __name__ == '__main__':
    S = Stack()
    S.push(12)
    S.push(11)
    S.push(12)
    #S.pop()
    S.last_inserted_value()
    #S.is_empty()