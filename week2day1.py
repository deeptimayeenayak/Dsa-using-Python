# Stack
'''
class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1

    def is_full(self):
        if self.__top==self.__max_size-1:
            return True
        return False
    def is_empty(self):
        if self.__top==-1:
            return True
        return False
    def push(self,data):
        if self.is_full():
            print("The stack is full")
        else:
            self.__top+=1
            self.__elements[self.__top]=data

    def pop(self):
        if self.is_empty():
            print("The stack is empty")
        else:
            data= self.__elements[self.__top]
            self.__top-=1
            return data
    def display(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            index=self.__top
            while(index>=0):
                print(self.__elements[index])
                index-=1
    def get_max_size(self):
        return self.__max_size
    
ball_stack = Stack(4)
print("Is it empty",ball_stack.is_empty())
ball_stack.push(5)
print("Is it empty",ball_stack.is_empty())
ball_stack.push(6)
ball_stack.push(7)
ball_stack.push(8)
ball_stack.display()
print("Size of stack",ball_stack.get_max_size())
print("Popped:",ball_stack.pop())
print("Stack after deleting")
ball_stack.display()
print("Size of stack",ball_stack.get_max_size())'''
'''
#Queue

class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if self.__rear==self.__max_size-1:
            return True
        return False
    def is_empty(self):
        if(self.__front > self.__rear):
            return True
        return False
    
    def enqueue(self,data):
        if self.is_full():
            print("The queue is full")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data
    def dequeue(self):
        if(self.is_empty()):
            print("The queue is empty")
        else:
            data= self.__elements[self.__front]
            self.__front+=1
            return data
    def display(self):
        for index in range(self.__front,self.__rear+1):
            print(self.__elements[index])
    def get_max_size(self):
        return self.__max_size
    
queue1 = Queue(4)
print("Is it full?",queue1.is_full())
print("Is it empty",queue1.is_empty())
queue1.enqueue(100)
queue1.display()
queue1.enqueue(200)
queue1.enqueue(300)
queue1.enqueue(400)
queue1.display()
queue1.enqueue(500)
queue1.display()
print("Element deleted",queue1.dequeue())
queue1.display()

'''
#Q1
'''
Given a queue of whole numbers. Write a python function to return a new queue which contains the evenly divisible numbers.
Note: A number is said to be evenly divisible if it is divisible by all the numbers in the given range without any remainder. Consider the range to be from 1 to 10 (both inclusive).
Assume that there will always be few elements in the input queue, which are evenly divisible by the numbers in the mentioned range.
Example:
Input Queue: 13983, 10080, 7113, 2520, 2500 (front - rear) Output Queue: 10080, 2520 (front-rear)


class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if self.__rear==self.__max_size-1:
            return True
        return False
    def is_empty(self):
        if(self.__front > self.__rear):
            return True
        return False
    
    def enqueue(self,data):
        if self.is_full():
            print("The queue is full")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data
    def dequeue(self):
        if(self.is_empty()):
            print("The queue is empty")
        else:
            data= self.__elements[self.__front]
            self.__front+=1
            return data
    def display(self):
        for index in range(self.__front,self.__rear+1):
            print(self.__elements[index])
    def get_max_size(self):
        return self.__max_size
def check_divisibility(numQueue):
    size = numQueue.get_max_size()
    solQ = Queue(size)
    while size > 0:
        ele = numQueue.dequeue()
        if all(ele%i == 0 for i in range(1,11)):
            solQ.enqueue(ele)

        size-=1
    return solQ
    
numQueue = Queue(5)
numQueue.enqueue(13983)
numQueue.enqueue(10080)
numQueue.enqueue(7113)
numQueue.enqueue(2520)
numQueue.enqueue(2500)
check_divisibility(numQueue).display()

'''
#Q2
'''
Given two lists, both having String elements, write a python program using python lists to create a new string as per the rule given below:
The first element in list1 should be merged with last element in list2, second element in list1 should be merged with second last element
in list2 and so on. If an element in list1/list2 is None, then the corresponding element in the other list should be kept as 
it is in the merged list.
Sample Input
list1=['A', 'app', 'a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y', 'tor', 'e', 'eps', 'ay', None, 'le', 'n']
Expected Output
"An apple a day keeps the doctor away"

list1=['A', 'app', 'a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y', 'tor', 'e', 'eps', 'ay', None, 'le', 'n']

s = " "
list2 = list2[::-1]
for i in range(len(list1)):
    if list1[i] is None:
        s = s + list2[i] + ""
    elif list2[i] is None:
        s = s + list1[i] + ""
    else:
        s = s + list1[i] + list2[i] +" "
print(s)
'''

#Q3
'''
Given two queues, one integer queue and another character queue, write a python program to merge them to form 
a single queue.
 Follow the below rules for merging:
Merge elements at the same position starting with the integer queue.
If one of the queues has more elements than the other, add all the additional elements at the end of the output queue. 
Note: max_size of the merged queue should be the sum of the size of both the queues.
For example,
Input -- queuel: 3,6,8 queue2: b,y,u,t,r,o Output 3,b,6,y,8,u,t,r,o
'''
'''
class Queue: 
     def __init__(self,max_size): 
  
         self.__max_size=max_size 
         self.__elements=[None]*self.__max_size 
         self.__rear=-1 
         self.__front=0 
  
     def is_full(self): 
         if(self.__rear==self.__max_size-1): 
                 return True 
         return False 
  
     def is_empty(self): 
         if(self.__front>self.__rear): 
             return True 
         return False 
  
     def enqueue(self,data): 
         if(self.is_full()): 
             print("Queue is full!!!") 
         else: 
             self.__rear+=1 
             self.__elements[self.__rear]=data 
  
     def dequeue(self): 
         if(self.is_empty()): 
             print("Queue is empty!!!") 
         else: 
             data=self.__elements[self.__front] 
             self.__front+=1 
             return data 
  
     def display(self): 
         for index in range(self.__front, self.__rear+1): 
             print(self.__elements[index]) 
  
  
     def get_max_size(self): 
         return self.__max_size 
  
     #You can use the below __str__() to print the elements of the DS object while debugging 
     def __str__(self): 
         msg=[] 
         index=self.__front 
         while(index<=self.__rear): 
             msg.append((str)(self.__elements[index])) 
             index+=1 
         msg=" ".join(msg) 
         msg="Queue data(Front to Rear): "+msg 
         return msg 
  
def merge_queue(queue1,queue2): 
     list1=[] 
     list2=[] 
     list3=[] 
      
     while (not queue1.is_empty()): 
         list1.append(queue1.dequeue()) 
      
     while (not queue2.is_empty()): 
         list2.append(queue2.dequeue()) 
      
     check=0     
     if len(list1)<len(list2): 
         length=len(list1)     
     else: 
         length=len(list2) 
         check=1 
      
     if str(list1[0]).isdigit(): 
         integer=list1 
         string=list2 
     else: 
         integer=list2 
         string=list1 
     flag=0 
     j,k=0,0 
     for i in range(0,2*length): 
         if flag==0: 
             list3.append(integer[j]) 
             flag=1 
             j+=1 
         elif flag==1: 
             list3.append(string[k]) 
             flag=0 
             k+=1 
     if check==0: 
         for i in list2: 
             if i not in list3: 
                 list3.append(i) 
     elif check==1: 
         for i in list1: 
             if i not in list3: 
                 list3.append(i) 
      
     merged_queue=Queue(len(list3)) 
     for item in list3: 
         merged_queue.enqueue(item) 
     return merged_queue 
  
 #Enqueue different values to both the queues and test your program 
  
queue1=Queue(3) 
queue2=Queue(6) 
queue1.enqueue(3) 
queue1.enqueue(6) 
queue1.enqueue(8) 
queue2.enqueue('b') 
queue2.enqueue('y') 
queue2.enqueue('u') 
queue2.enqueue('t') 
queue2.enqueue('r') 
queue2.enqueue('o') 
  
merged_queue=merge_queue(queue1, queue2) 
print("The elements in the merged queue are:") 
merged_queue.display()
'''

# Traversing a Linked List
class Node:
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tues")
e3 = Node("Wed")
list.headval.nextval = e2
e2.nextval = e3
list.listprint()