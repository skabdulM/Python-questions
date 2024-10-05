class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegining(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def printAll(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end="->")
            current_node = current_node.next

    def insertAtIndex(self, data, index):
        if index == 0:
            self.insertAtBegining(data)
            return

        position = 0
        current_node = self.head
        while current_node != None and position + 1 != index:
            position += 1
            current_node = current_node.next
        if current_node != None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")

    def remove_first_node(self):
        if self.head == None:
            return

        self.head = self.head.next

    def remove_at_index(self, index):
        if self.head is None:
            return

        current_node = self.head
        position = 0

        if index == 0:
            self.remove_first_node()
        else:
            while current_node != None and position + 1 != index:
                position += 1
                current_node = current_node.next

            if current_node is None or current_node.next is None:
                print("index not present")
            else:
                current_node.next = current_node.next.next


temp = LinkedList()
temp.insertAtEnd(45)
temp.insertAtBegining(26)
temp.insertAtBegining("3")
temp.insertAtBegining("2")
temp.insertAtIndex(90, 1)
temp.remove_at_index(0)
temp.printAll()
