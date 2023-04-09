#Node definition
'''class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

#Single Linked List definition
class SLinkedList:
    def __init__(self):
        self.headval = None
        
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
            
    def atBeginning(self, newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode
        
    def atEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return 
        last_ele = self.headval
        while(last_ele.nextval):
            last_ele = last_ele.nextval
        last_ele.nextval = NewNode

    def inBetween(self, middle_node, newdata):
        if middle_node is None:
            print("The mentioned node is absent.")
            return
        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

    def deleteAtStart(self):
        if self.headval is None:
            print("list has no element")
            return
        else:
            temp = self.headval
            self.headval = self.headval.next
            temp.next = None
            
list = SLinkedList()
list.headval = Node("Monday")
e2 = Node("Tuesday")
e3 = Node("Wednesday")
#creating links
list.headval.nextval = e2
e2.nextval = e3
# list.listprint()
list.atBeginning("Sunday")
list.atEnd("Saturday")
list.inBetween(list.headval.nextval,"Thursday")
list.listprint()
'''
class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None
class LinkedList:
    def __init__(self):
        self.start_node = None

def traverse_list(self):
    if self.start_node is None:
        print("List has no element")
        return
    else:
        n = self.start_node
        while n is not None:
            print(n.item , " ")
            n = n.ref
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node= new_node
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n= n.ref
        n.ref = new_node;
    def insert_after_item(self, x, data):

        n = self.start_node
        print(n.ref)
        while n is not None:
            if n.item == x:
                break
            n = n.ref
        if n is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    def insert_at_index (self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
        i = 1
        n = self.start_node
        while i < index-1 and n is not None:
            n = n.ref
            i = i+1
        if n is None:
            print("Index out of bound")
        else: 
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    def get_count(self):
        if self.start_node is None:
            return 0;
        n = self.start_node
        count = 0;
        while n is not None:
            count = count + 1
            n = n.ref
        return count
    def reverse_linkedlist(self):
        prev = None
        n = self.start_node
        while n is not None:
            next = n.ref
            n.ref = prev
            prev = n
            n = next
        self.start_node = prev
        