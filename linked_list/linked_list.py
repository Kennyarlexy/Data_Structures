"""
We know that dynamic array and list are very good at accessing data (complexity of O(1)). However, it's very bad at inserting or deleting data.

Linked list is one way to solve this problem. It's useful when inserting or deleting takes up most of the operations.

Linked list consists of nodes where each node contains a data and a reference to the next node, except for the tail node.

repr is the abbreviation for read evaluate print loop
"""

class Node:
    data = None
    next_node = None

    """
    A constructor in Python can declare and initialize variables, unlike C++ where a constructor can only initialize
    """
    def __init__(self, data):
        self.data = data
        

    #defining the repr (similar with operator overloading in C++)
    def __repr__(self):
        """
        another way to return a string (good to know)
        return "<Node data: %s>" % self.data, the "%" means substituting
        """
        return "<Node data: " + str(self.data) + ">"


class LinkedList:
    """
    since we identify each linked list by it's head, we just need to store the head and the rest will automatically identified by referencing chain.
    """
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def size(self):
        """
        traverse through the entire linked list until we hit the tail
        """
        current = self.head #current is a Node object
        count = 0

        while current is not None:
            count += 1
            current = current.next_node
        return count
    
    def add(self, data):
        """
        add a new node containing data as the new head of the current linked list, time complexity is O(1)
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, target):
        """
        return the first node that matches the target. if such node doesn't exist, return None
        Worst case of O(n)
        """
        current = self.head
        while current is not None:
            if current.data == target:
                return True
            else:
                current = current.next_node
        return False

    def insert(self, target_position, data):
        """
        inserts at certain position by traversing the linked list till the designated target position (index)
        time complexity of O(n)
        """
        if target_position == 0:
            self.add(data)
        else:
            current_node = self.head
            current_position = 0

            while current_position < target_position - 1:
                current_node = current_node.next_node
                current_position += 1
                if current_node is None:
                    print("Index out of range!")
                    return

            new_node = Node(data)
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node

    def removeData(self, data):
        current = self.head
        #remember that when current node is remove, you need to link prev_node to next_node, so we need to keep track of this prev_node
        prev_node = None

        while current is not None:
            if current.data == data:
                if current == self.head:
                    self.head = current.next_node
                else:
                    prev_node.next_node = current.next_node
                break
            prev_node = current
            current = current.next_node
        return current

    def __repr__(self) -> None:
        """
        Traverse the entire linked list from head to tail to print, complexity of O(n)
        tried to save memory by not using a list to store output but didn't work since __repr__ needs to return a string
        """
        output = []
        current = self.head
        while current is not None:
            if current == self.head:
                output.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                output.append("[Tail: %s]" % current.data)
            else:
                output.append("[%s]" % current.data)
            current = current.next_node

        return " -> ".join(output)

#main
N1 = Node(10)
N2 = Node(20)

N1.next_node = N2

#Keep in mind that before we define the repr for Node objects, Python doesn't know how we are supposed to print the object
print(N1)
print(N1.next_node)

#size() demo
list_A = LinkedList()
list_A.head = N1
print("\nOriginal list", list_A)
print("Size:", list_A.size())

#repr demo
data = 1000
print("\nAdding new data:", data)
list_A.add(data)
print("After adding new data\nSize:", list_A.size(), "\n")
print(list_A)

#search() demo
target = int(input("Find target: "))
print("Target found!" if list_A.search(target) else "Target not found!")

#insert() demo
print("\nInserting 100 to index 1")
list_A.insert(1, 100)
print(list_A)

print("\nInserting 200 to index 5 <-- This won't work since the max index should be 4")
list_A.insert(5, 200)
print(list_A)

#removeData() demo
print("\nRemoving", list_A.removeData(20))
print(list_A)