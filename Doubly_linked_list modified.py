class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete_item(self,data):
        itr_head = self.head
        itr_tail = self.tail

        if itr_head.data == data:
            self.head = itr_head.next

        elif itr_tail.data == data:
            temp = self.tail.prev
            temp.next = None
            self.tail = temp

        else:
            while itr_head:
                temp = itr_head.next
                if temp.data == data:
                    itr_head.next = temp.next
                itr_head = itr_head.next

    def print_list_T_to_H(self):
        itr = self.tail
        print(None)
        while itr:
            print('<-->', itr.data, end='')
            itr = itr.next
            itr = itr.next


    def print_list_H_to_T(self):
        itr = self.head
        while itr:
            print(itr.data, end='<-->')
            itr = itr.next
        print(None)


if __name__ == '__main__':
    dlist = LinkedList()
    dlist.append(34)
    dlist.push(12)
    dlist.delete_item(12)

    dlist.print_list_H_to_T()
