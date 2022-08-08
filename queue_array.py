
class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type 
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        if(capacity < 0):
            self.capacity = 0
        else:
            self.capacity = capacity
        self.items = [None]*capacity
        self.num_items = 0 
        self.front = 0
        self.back = 0


    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise'''
        if(self.num_items == 0): #checks for empty stack
            return True
        return False


    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise'''
        if(self.num_items == self.capacity): #checks for full stack
            return True
        return False


    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError'''
        if(self.num_items >= self.capacity):
            raise IndexError('queue full')
        else:
            self.items[self.back] = item
            if(self.back == self.capacity -1):
                self.back = 0
            else:
                self.back += 1
            self.num_items += 1


    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError'''
        if (self.num_items <= 0):
            raise IndexError('empty queue')
        else:
            n = self.items[self.front]
            if(self.front == self.capacity -1):
                self.front = 0
            else:
                self.front += 1
            self.num_items -= 1
            return n


    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity'''
        return self.num_items 

