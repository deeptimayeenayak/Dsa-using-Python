'''
# # # Selection sort in Python
# # def selectionSort(array, size):
# # 	for ind in range(size):
# # 		min_index = ind
# # 		for j in range(ind + 1, size):
# # 			if array[j] < array[min_index]:
# # 				min_index = j

# # 		(array[ind], array[min_index]) = (array[min_index], array[ind])

# # arr = [20,12,10,15,2]
# # size = len(arr)
# # selectionSort(arr, size)
# # print('array in sorted area:')
# # print(arr)


# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class SortList:  
#     #Represent the head and tail of the singly linked list  
#     def __init__(self):  
#         self.head = None;  
#         self.tail = None;  
          
#     #addNode() will add a new node to the list  
#     def addNode(self, data):  
#         #Create a new node  
#         newNode = Node(data);  
          
#         #Checks if the list is empty  
#         if(self.head == None):  
#             #If list is empty, both head and tail will point to new node  
#             self.head = newNode;  
#             self.tail = newNode;  
#         else:  
#             #newNode will be added after tail such that tail's next will point to newNode  
#             self.tail.next = newNode;  
#             #newNode will become new tail of the list  
#             self.tail = newNode;  
              
#     #sortList() will sort nodes of the list in ascending order  
#     def sortList(self):  
#         #Node current will point to head  
#         current = self.head  
#         index = None;  
#         l=[] 
#         if(self.head == None):  
#             return;  
#         else:  
#             while(current != None):  
#                 #Node index will point to node next to current  
#                 index = current.next;  
                  
#                 while(index != None):  
#                     if(current.data > index.data):  
#                         temp = current.data;  
#                         current.data = index.data;  
#                         index.data = temp;  
#                     index = index.next;  
#                 current = current.next;  
#                 l.append(index) 
            
#     #display() will display all the nodes present in the list  
#     def display(self):  
#         #Node current will point to head 
#         current = self.head
#         if(self.head == None):  
#             print("List is empty");  
#             return;  
#         while(current != None):  
#             #Prints each node by incrementing pointer  
#             print(current.data)  
#             current = current.next
#         return " "
#     def replace(self,data):
#         current = self.head
#         while(current.next.next != None):
#             current = current.next
#         current.next.item=data
#         return current.next.item
#     def deallocation(self,x):
#               if self.head is None:
#                   print("The list has no element to delete")
#                   return
#               if self.head.data==x:
#                   self.head=self.head.next
#                   return
#               n=self.head
#               while n.next is not None:
#                   if n.next.data==x:
#                       break
#                   n=n.next
#               if n.next==None:
#                   print("item not found in the list")
#               else:
#                   n.next=n.next.next
#     def allocation(self,index,data):
#         if index==1:
#             Newnode=Node(data)
#             Newnode.next=self.head
#             self.head=Newnode
#         i=1
#         n=self.head
#         while i<index-1 and n is not None:
#             i+=1
#             n=n.ref
#         if n is None:
#             print("index out of range")
#         else:
#             Newnode=Node(data)
#             Newnode.next=n.next
#             n.next=Newnode     
        
              
# sList = SortList();    
# sList.addNode(9);  
# sList.addNode(7);  
# sList.addNode(2);  
# sList.addNode(5);  
# sList.addNode(4);  
# print(sList.display())  
# sList.deallocation(2)
# print(sList.display()) 
# sList.allocation(2,2)
# print(sList.display())


#quick sort
def partition(array, low, high):
	pivot = array[high]
	i = low - 1
	for j in range(low, high):
		if array[j] <= pivot:
			i = i + 1
			(array[i], array[j]) = (array[j], array[i])
	(array[i + 1], array[high]) = (array[high], array[i + 1])
	return i + 1
def quickSort(array, low, high):
	if low < high:
		pi = partition(array, low, high)
		quickSort(array, low, pi - 1)
		quickSort(array, pi + 1, high)
data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)
size = len(data)
quickSort(data, 0, size - 1)
print('Sorted Array in Ascending Order:')
print(data)


class Node:
    def _init_(self,data):
        self.data=data
        self.next=None
class SortList:  
    #Represent the head and tail of the singly linked list  
    def _init_(self):  
        self.head = None;  
        self.tail = None;  
          
    #addNode() will add a new node to the list  
    def addNode(self, data):  
        #Create a new node  
        newNode = Node(data);  
          
        #Checks if the list is empty  
        if(self.head == None):  
            #If list is empty, both head and tail will point to new node  
            self.head = newNode;  
            self.tail = newNode;  
        else:  
            #newNode will be added after tail such that tail's next will point to newNode  
            self.tail.next = newNode;  
            #newNode will become new tail of the list  
            self.tail = newNode;  
              
    #sortList() will sort nodes of the list in ascending order  
    def sortList(self):  
        #Node current will point to head  
        current = self.head  
        index = None;  
        l=[] 
        if(self.head == None):  
            return;  
        else:  
            while(current != None):  
                #Node index will point to node next to current  
                index = current.next;  
                  
                while(index != None):  
                    if(current.data > index.data):  
                        temp = current.data;  
                        current.data = index.data;  
                        index.data = temp;  
                    index = index.next;  
                current = current.next;  
                l.append(index) 
            
    #display() will display all the nodes present in the list  
    def display(self):  
        #Node current will point to head 
        current = self.head
        if(self.head == None):  
            print("List is empty");  
            return;  
        while(current != None):  
            #Prints each node by incrementing pointer  
            print(current.data)  
            current = current.next
        return " "
    def replace(self,data):
        current = self.head
        while(current.next.next != None):
            current = current.next
        current.next.item=data
        return current.next.item
    def deallocation(self,x):
              if self.head is None:
                  print("The list has no element to delete")
                  return
              if self.head.data==x:
                  self.head=self.head.next
                  return
              n=self.head
              while n.next is not None:
                  if n.next.data==x:
                      break
                  n=n.next
              if n.next==None:
                  print("item not found in the list")
              else:
                  n.next=n.next.next
    def allocation(self,index,data):
        if index==1:
            Newnode=Node(data)
            Newnode.next=self.head
            self.head=Newnode
        i=1
        n=self.head
        while i<index-1 and n is not None:
            i+=1
            n=n.ref
        if n is None:
            print("index out of range")
        else:
            Newnode=Node(data)
            Newnode.next=n.next
            n.next=Newnode     
        
              
sList = SortList();    
sList.addNode(9);  
sList.addNode(7);  
sList.addNode(2);  
sList.addNode(5);  
sList.addNode(4);  
print(sList.display())  
sList.deallocation(2)
print(sList.display()) 
sList.allocation(2,2)
print(sList.display())

class FruitInfo:
    fruit_name_list = ['Apple', 'Guava', 'Orange', 'Grape', 'Sweet Lime']
    fruit_price_list = [200, 80, 70, 110, 60]

    def get_fruit_price(fruit_name):
        if fruit_name in FruitInfo.fruit_name_list:
            index = FruitInfo.fruit_name_list.index(fruit_name)
            return FruitInfo.fruit_price_list[index]
        else:
            return -1

class Purchase:
    counter = 101

    def _init_ (self, customer, fruit_name, quantity):
        self.__purchase_id = 'P' + str(Purchase.counter)
        Purchase.counter += 1
        self.__customer = customer
        self.__fruit_name = fruit_name
        self.__quantity = quantity

    def calculate_price(self):
        price_per_kg = FruitInfo.get_fruit_price(self.__fruit_name)
        if price_per_kg == -1:
            return -1

        total_price = price_per_kg * self.__quantity

        if price_per_kg == max(FruitInfo.fruit_price_list) and self.__quantity > 1:
            total_price *= 0.98  # 2% discount
        elif price_per_kg == min(FruitInfo.fruit_price_list) and self.__quantity >= 5:
            total_price *= 0.95  # 5% discount

        if self.__customer == 'wholesale':
            total_price *= 0.9  # 10% discount

        return total_price

    def get_purchase_id(self):
        return self.__purchase_id

    def get_customer(self):
        return self.__customer

    def get_fruit_name(self):
        return self.__fruit_name

    def get_quantity(self):
        return self.__quantity

class Customer:
    def _init_(self, customer_name):
        self.__customer_name = customer_name

    def get_customer_name(self):
        return self.__customer_name


customer1 = Customer('Litu')
purchase1 = Purchase(customer1.get_customer_name(), 'Apple', 2)
print(purchase1.calculate_price())

customer2 = Customer('Harsha')
purchase2 = Purchase(customer2.get_customer_name(), 'Grape', 6)
print(purchase2.calculate_price())

customer3 = Customer('Sumit')
purchase3 = Purchase(customer3.get_customer_name(), 'Mango', 4)
print(purchase3.calculate_price())


'''



'''
class BakeHouse:
    def __init__(self):
        self.__occupied_table_list = []
        
    def get_occupied_table_list(self):
        return self.__occupied_table_list

    def allocate_table(self):
        table_num = 1
        while table_num in self.__occupied_table_list:
            table_num+=1
        self.__occupied_table_list.append(table_num)
        self.__occupied_table_list.sort()
        return table_num

    def deallocate_table(self, table_num):
        if table_num in self.__occupied_table_list:
            self.__occupied_table_list.remove(table_num)
            return "Table De-Allocated"
        else:
            return "Table already vacant"

bh = BakeHouse()
print(bh.get_occupied_table_list())
table1 = bh.allocate_table()
table2 = bh.allocate_table()
table3 = bh.allocate_table()
table4 = bh.allocate_table()
print(bh.get_occupied_table_list())
bh.deallocate_table(table3)
bh.deallocate_table(table2)
print(bh.get_occupied_table_list())
new = bh.allocate_table()
print(bh.get_occupied_table_list())
'''

# Quick Sort
# Python3 implementation of QuickSort
'''

def partition(array, low, high):

    pivot = array[high]

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:

            i = i + 1

            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1


def quick_sort(array, low, high):
    if low < high:
       pi = partition(array, low, high)
       quick_sort(array, low, pi - 1)
       quick_sort(array, pi + 1, high)


array = [10, 7, 8, 9, 1, 5]
quick_sort(array, 0, len(array) - 1)
print(f'Sorted array: {array}')
'''
'''
Write a python program that accepts a text and displays a 
string which contains the word with the largest frequency
 in the text and the 
frequency itself separated by a space.
Rules:
The word should have the largest frequency.
In case multiple words have the same frequency, then choose 
the word that has the maximum length.
Assumptions:
The text has no special characters other than space.
The text would begin with a word and there will be only a 
single space between the words.
Perform case insensitive string comparisons wherever 
necessary

'''
'''
def find_most_frequent_word(text):
    # Convert the text to lowercase and split into words
    words = text.lower().split()

    # Count the frequency of each word
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    # Find the word with the maximum frequency
    max_frequency = 0
    max_word = ''
    for word, freq in frequency.items():
        if freq > max_frequency:
            max_frequency = freq
            max_word = word
        elif freq == max_frequency:
            if len(word) > len(max_word):
                max_word = word

    # Return the word with its frequency
    return max_word + ' ' + str(max_frequency)

# Example usage
text = ('Betty bought a bit of butter but the bit of butter was a little bitter so Betty bought a bit of better butter to make the bitter butter better.')
print(find_most_frequent_word(text)) # Expected output: 'the 2'   
'''

'''
3.The number, 197, is called a circular prime because all
 rotations of the digits: 197, 971, and 719, are themselves
 prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 
13, 17, 31, 37, 71, 73, 79, and 97.

Write a python program to find and display the number of 
circular primes less than the given limit.
'''
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_circular_prime(n):
    str_n = str👎
    for i in range(len(str_n)):
        rotated_str = str_n[i:] + str_n[:i]
        rotated_num = int(rotated_str)
        if not is_prime(rotated_num):
            return False
    return True

def count_circular_primes(limit):
    count = 0
    for n in range(2, limit):
        if is_circular_prime(n):
            count += 1
    return count

# Example usage
limit = 100
print(count_circular_primes(limit))