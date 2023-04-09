#Tree
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def insert(node,data):
    if node is None:
        return Node(data)
    if data <= node.data:
        node.left = insert(node.left,data)
    else:
        node.right = insert(node.right,data)
    return node
     
def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.data)+"->",end="")
        inorder(root.right)
        
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.data)+"->",end="")
#Depth First Search
def preorder(root):
    if root:
        print(str(root.data)+"->",end="")
        preorder(root.left)
        preorder(root.right)

root  = None
root = insert(root,10)
root = insert(root,11)
root = insert(root,12)
root = insert(root,13)
root = insert(root,14)
root = insert(root,15)
root = insert(root,16)
root = insert(root,17)
root = insert(root,18)
root = insert(root,19)
inorder(root)

'''
'''Q.1. A teacher has given a project assignment to a class of 10 students.

She wants to store the marks (out of 100 ) scored by each student. The marks scored are as mentioned below:
89,78,99,76,77,67,99,98,90

Write a python program to store the marks in a list and perform the following:

    1. The teacher forgot to include the marks of one student. Insert 78 at index position, 8 and display the marks of all 10 students.
    2. The teacher also wants to know the marks scored by students represented by index positions, 5 and 7. Identify and display the two marks.
'''
'''
def update_mark_list(mark_list, new_element, pos):
    mark_list.append(0)
    l=len(mark_list)-1
    for i in range(len(mark_list)-pos-1):
        mark_list[l],mark_list[l-1]=mark_list[l-1],mark_list[l]
        l-=1
    mark_list[pos]=new_element
    return mark_list

def find_mark(mark_list,pos1,pos2):
    lst=[]
    lst.append(mark_list[pos1])
    lst.append(mark_list[pos2])
    return lst

mark_list=[89,78,99,76,77,72,88,99]
new_element=69
pos=2
pos1=5
pos2=8
print(update_mark_list(mark_list, new_element, pos))
print(find_mark(mark_list, pos1, pos2))'''

"""A train is identified by its name and list of compartments.
The compartments are identified by its name,total seating
capacity and the number of passengers.
Implement the class Train as given in the class diagram.
Train
- train_name
- compartment_list
_init_(train_name,compartment_list)
+ get_train_name()
+ get_compartment_list()
+ count_compartments ()
+ check_vacancy()
Write a python program to implement the following:
count_compartments()- returns the total number of compartments
 in the train
check_vacancy()-returns the count of the compartments in which
 more than 50% of the seats are vacant
Note : Compartment list is maintained as a linked list where
data in each node refers to a compartment.
"""
'''
class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None
    def get_data(self):
        return self.__data
    def set_data(self, data):
        self.__data = data
    def get_next(self):
        return self.__next
    def set_next(self, next_node):
        self.__next = next_node

class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
    def get_head(self):
        return self.__head
    def get_tail(self):
        return self.__tail
    def add(self, data):
        new_node = Node(data)
        if (self.__head is None):
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node
    def insert(self, data, data_before):
        new_node = Node(data)
        if (data_before == None):
            new_node.set_next(self.__head)
            self.__head = new_node
            if (new_node.get_next() == None):
                self.__tail = new_node
        else:
            node_before = self.find_node(data_before)
            if (node_before is not None):
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if (new_node.get_next() is None):
                    self.__tail = new_node
            else:
                print(data_before, "is not present in the Linked list")
    def display(self):
        temp = self.__head
        while (temp is not None):
            print(temp.get_data())
            temp = temp.get_next()
    def find_node(self, data):
        temp = self.__head
        while (temp is not None):
            if (temp.get_data() == data):
                return temp
            temp = temp.get_next()
        return None
    def delete(self, data):
        node = self.find_node(data)
        if (node is not None):
            if (node == self.__head):
                if (self.__head == self.__tail):
                    self.__tail = None
                self.__head = node.get_next()
            else:
                temp = self.__head
                while (temp is not None):
                    if (temp.get_next() == node):
                        temp.set_next(node.get_next())
                        if (node == self.__tail):
                            self.__tail = temp
                        node.set_next(None)
                        break
                    temp = temp.get_next()
        else:
            print(data, "is not present in Linked list")
    # You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp = self.__head
        msg = []
        while (temp is not None):
            msg.append(str(temp.get_data()))
            temp = temp.get_next()
        msg = " ".join(msg)
        msg = "Linkedlist data(Head to Tail): " + msg
        return msg

class Compartment:
    def __init__(self, compartment_name, no_of_passengers, total_seats):
        self.__compartment_name = compartment_name
        self.__no_of_passengers = no_of_passengers
        self.__total_seats = total_seats
    def get_compartment_name(self):
        return self.__compartment_name
    def get_no_of_passengers(self):
        return self.__no_of_passengers
    def get_total_seats(self):
        return self.__total_seats

class Train:
    def __init__(self, train_name, compartment_list):
        self.__train_name = train_name
        self.__compartment_list = compartment_list
    def get_train_name(self):
        return self.__train_name
    def get_compartment_list(self):
        return self.__compartment_list
    def count_compartments(self):
        temp = self.__compartment_list.get_head()
        count = 0
        while (temp):
            count += 1
            temp = temp.get_next()
        return count
    def check_vacancy(self):
        count = 0
        temp = self.__compartment_list.get_head()
        while (temp):
            per = (temp.get_data().get_total_seats() - temp.get_data().get_no_of_passengers()) / temp.get_data().get_total_seats()
            if per > 0.5:
                count += 1
            temp = temp.get_next()
        return count


compartment1 = Compartment("SL", 250, 400)
compartment2 = Compartment("2AC", 125, 280)
compartment3 = Compartment("3AC", 120, 300)
compartment4 = Compartment("FC", 160, 300)
compartment5 = Compartment("1AC", 100, 210)
compartment_list = LinkedList()
compartment_list.add(compartment1)
compartment_list.add(compartment2)
compartment_list.add(compartment3)
compartment_list.add(compartment4)
compartment_list.add(compartment5)
train1 = Train("Shatabdi", compartment_list)
count = train1.count_compartments()
print("The number of compartments in the train:", count)
vacancy_count = train1.check_vacancy()
print("The number of compartments which have more than 50% vacancy:", vacancy_count)
'''
'''
Mary is a kindergarten teacher. She has given a task to the children after teaching them a list of words. 
The task is to find the unknown words (other than the words they already know) from the given text. 
Write a python function which accepts the text and the known list of words and returns the set of unknown words found. 
Return -1 if there are no unknown words. 
Estimated Time: 20 minutes

Sample Input
Text: "the sun rises in the east"
Vocabulary: ["sun", "in", "east", "doctor", "day"] 

Expected Output: {'rises', 'the'}'''

text = "the sun rises in the east"
voc = ["sun", "in", "east", "doctor", "day"]

def known_unknown(text, voc):
    unknown = set()
    for i in text.split():
        if i not in voc:
            unknown.add(i)
    return unknown if len(unknown)>0 else -1

print((known_unknown(text, voc)))