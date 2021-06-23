class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_begining(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return

        temp = self.head
        self.head = new_node
        self.head.next = temp

    def print_list(self):
        itr = self.head
        while itr:
            print(itr.data, end="-->")
            itr = itr.next
        print("None")

    def add_in_the_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def add_after(self, add_after, new_value):
        itr = self.head
        new_node = Node(new_value)
        while itr:
            if itr.data == add_after:
                temp = itr.next
                itr.next = new_node
                new_node.next = temp
                return self.head
            itr = itr.next

    def add_before(self, add_before, new_value):
        new_node = Node(new_value)
        itr = self.head

        if itr.data == add_before:
            new_node.next = itr
            self.head = new_node
            return

        while itr.next:
            if itr.next.data == add_before:
                temp = itr.next
                itr.next = new_node
                new_node.next = temp
                return
            itr = itr.next

    def delete(self, data):
        itr = self.head
        if itr.data == data:
            self.head = itr.next
            return

        while itr:
            check_node = itr.next

            if check_node.data == data:
                temp = check_node.next
                itr.next = temp
                return
            itr = itr.next



if __name__ == "__main__":
    llist = LinkedList()
    llist.add_at_begining(56)
    llist.add_at_begining(57)
    llist.add_at_begining(58)
    llist.add_at_begining(59)
    llist.add_at_begining(50)
    llist.add_in_the_end(67)
    llist.add_after(57, 14)
    llist.add_after(50, 41)
    llist.add_after(67, 32)
    llist.add_before(50, 47)
    llist.add_before(14, "p")
    llist.delete(47)
    llist.print_list()
