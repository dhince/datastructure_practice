# In this code push method is equivalent to add_at_begining method in previous code
# But in here push method is very short and efficient
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = new_node

    def delete_item(self, data):
        itr = self.head

        if itr.data == data:
            self.head = itr.next
            return
        while itr:
            temp = itr.next
            if temp.next.next == None:
                temp.next = None

            elif temp.data == data:
                itr.next = temp.next
            itr = itr.next

            itr = itr.next

    def print_list(self):
        itr = self.head
        while itr:
            print(itr.data, end='-->')
            itr = itr.next
        print(None)

if __name__ == '__main__':
    llist = LinkedList()
    llist.append(12)
    llist.append(45)
    llist.push(23)
    llist.delete_item(45)
    llist.print_list()


