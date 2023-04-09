# Binary Search Tree operations in Python
''''
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def inorder(root):
    if root is not None:
        
        inorder(root.left)
        print(str(root.key) + "->", end=' ')
        inorder(root.right)


def insert(node, key):

    if node is None:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node


def minValueNode(node):
    current = node

    while (current.left is not None):
        current = current.left

    return current


def deleteNode(root, key):

    if root is None:
        return root

    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif (key > root.key):
        root.right = deleteNode(root.right, key)
    else:

        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minValueNode(root.right)

        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)

    return root


root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)

print("Inorder traversal: ", end=' ')
inorder(root)

print("\nDelete 10")
root = deleteNode(root, 10)
print("Inorder traversal: ", end=' ')
inorder(root)
print("\nDelete 10")
root = deleteNode(root, 10)
print("Inorder traversal: ", end=' ')
inorder(root)
'''
# 2 7 9 4 6 5 10
'''
Odd Queue:
7 9 5
Even Queue:
2 4 6 10
1.Given a queue of integers, write a python program to split it into
two queues, one containing odd numbers and another even numbers. The relative
order of elements must be maintained. E.g: Input queue: 2,7,9,4,6,5,10 
Output queues: 7,9,5 and 2,4,6,10 Note:Assume that all the three queues are of the 
same size.
'''
'''
class Queue:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None]*self.__max_size
        self.__rear = -1
        self.__front= 0

    def is_full(self):
        if (self.__rear == self.__max_size-1):
            return True
        return False

    def is_empty(self):
        if (self.__front > self.__rear):
            return True
        return False

    def enqueue(self, data):
        if self.is_full():
            print("Queue Full!")
        else:
            self.__rear += 1
            self.__elements[self.__rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue Empty!")
        else:
            data = self.__elements[self.__front]
            self.__front += 1
            return data

    def display(self):
        for index in range(self.__front, self.__rear+1):
            print(self.__elements[index])

    def get_max_size(self):
        return self.__max_size

def check_even_odd(numQ):
    size = numQ.get_max_size()
    evenQ = Queue(size)
    oddQ = Queue(size)
    while size > 0:
        ele = numQ.dequeue() 
        print("Elements: ", ele)
        if ele%2 == 0:
            evenQ.enqueue(ele)
        else:
            oddQ.enqueue(ele)
        size -= 1
    print("ODD Queue:")
    while not oddQ.is_empty():
        print(oddQ.dequeue())

    print("EVEN Queue:")
    while not evenQ.is_empty():
        print(evenQ.dequeue())

numQ = Queue(7)
numQ.enqueue(2)
numQ.enqueue(7)
numQ.enqueue(9)
numQ.enqueue(4)
numQ.enqueue(6)
numQ.enqueue(5)
numQ.enqueue(10)
check_even_odd(numQ)
'''
'''
2.Write a python function which accepts two linked lists containing integer data and an integer,
 n and merges the two linked lists, such that list2 is merged with list1 after n number of nodes. 
 Assume that value of n will always be less than or equal to
the number of nodes in list1.
Sample Input               Expected Output
list1  1->2->4->3->5
list2  9->8->11
'''
'''
class Node:
    def __init__(self, dataval=None):
        self.data = dataval
        self.next = None

def merge_lists(list1, list2, n):
    if n == 0:
        list2_tail = list2
        while list2_tail.next is not None:
            list2_tail = list2_tail.next
        list2_tail.next = list1
        return list2
    else:
        curr1 = list1
        for i in range(n-1):
            curr1 = curr1.next
        curr2 = list2
        while curr2.next is not None:
            curr2 = curr2.next
        curr2.next = curr1.next
        curr1.next = list2
        return list1

#LIST1
list1 = Node(1)
e2 = Node(2)
e3 = Node(4)
e4 = Node(3)
e5 = Node(5)
list1.next = e2
e2.next = e3
e3.next = e4
e4.next = e5

#LIST 2 - CAN ALSO BE DECLARED LIKE THIS
list2 = Node(9)
list2.next = Node(8)
list2.next.next = Node(11)

merged = merge_lists(list1, list2, 2)

while merged is not None:
    print(merged.data, end=" ")
    merged=merged.next

'''
'''
Q3.Original List:                      new list:
12                                     12
95                                     95
140                                    100
110                                    110
40                                     40
'''
'''
class Node:
    def __init__(self, data=None):
        
'''

#Program to retrieve all the data(name,age,gender) for the given gender from a queue of people

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def get_people_by_gender(self, gender):
        people = []
        for person in self.items:
            if person.gender == gender:
                people.append(person)
        return people


q = Queue()
q.enqueue(Person('Alice', 25, 'female'))
q.enqueue(Person('Bob', 30, 'male'))
q.enqueue(Person('Charlie', 20, 'male'))
q.enqueue(Person('David', 27, 'male'))
q.enqueue(Person('Eve', 22, 'female'))

people = q.get_people_by_gender('male')
if people:
    for person in people:
        print(f"Name: {person.name}, Age: {person.age}, Gender: {person.gender}")
else:
    print("No people of the given gender found in the queue.")