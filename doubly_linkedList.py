class Node:
    def __init__(self,  prev = None,data = None, next = None):
        self.prev = prev
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        new_node = Node(None, data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


    def append(self, data):
        new_node = Node(None, data)
        if self.tail == None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def printlist_head_to_tail(self):
        temp = self.head
        while temp:
            print("<-->", temp.data, end= "")
            temp = temp.next
        print("<-->")

    def printlist_tail_to_head(self):
        temp = ll.tail
        while temp:
            print("<-->", temp.data, end="")
            temp = temp.prev
        print("<-->")




if __name__ == '__main__':
    ll = LinkedList()
    ll.append(32)
    ll.append(45)
    ll.push(12)
    ll.push(43)
    ll.printlist_head_to_tail()

