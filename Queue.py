from collections import deque
class Queue:
    def __init__(self):
        self.queue = deque()
    def insert(self,value):
        self.value = value
        self.queue.appendleft(value)
        print(self.queue)
    def delete(self):
        self.queue.pop()
        print(self.queue)
    def length(self):
        if len(self.queue)==0:
            print("Empty")
        else:
            print(len(self.queue))
if __name__ =='__main__':
    q = Queue()
    q.insert(100)
    q.insert(200)
    q.delete()
    q.length()