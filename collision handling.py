from doubly_linkedList import *

class HashTable:
    def __init__(self):
        #self.main_bus = LinkedList()
        self.main_bus_head = None

    def get_hash(self, key):
        hash = 0
        for element in key:
            hash += ord(element)
        return hash

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        main_node = Node(key, value)
        head = None
        new_node = Node(h)

        if self.main_bus_head == None:

            self.main_bus_head = new_node
            head = main_node
            self.main_bus_head.data = head

        itr = self.main_bus_head
        found_hash = False
        found_key = False
        while itr.data:
            if itr.prev == h:
                temp = itr.data
                found_hash = True
                if temp == None:
                    temp = main_node

                while temp.data:
                    if temp.prev == key:
                        temp.data = value
                        found_key = True
                    temp = temp.next
                if not found_key:
                    temp = main_node

            itr = itr.next

        if not found_hash:
            new_node.next = self.main_bus_head
            self.main_bus_head = new_node
            head = main_node
            self.main_bus_head.data = head

    def __getitem__(self, item):
        h = self.get_hash(item)
        itr = self.main_bus_head
        found_hash = False
        found_key = False
        while itr:
            if itr.prev == h:
                found_hash = True
                temp = itr.data
                while temp:
                    if temp.prev == item:
                        found_key = True
                        return temp.data
                    temp = temp.next
            itr = itr.next
        if not found_hash or not found_key:
            return "such item is isn't there:"


if __name__ == "__main__":
    t = HashTable()
    t['march 9'] = 130
    print(t.__getitem__('march 9'))












