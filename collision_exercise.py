class Hash_Table:
    def __init__(self):
        self.max = 10
        self.arr = [[] for i in range(self.max)]

    def get_hash(self, key):
        hash = 0
        for i in key:
            hash += ord(i)
        index = hash % self.max
        return index

    def __setitem__(self, key, value):
        found = False
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, item):
        arr_index = self.get_hash(item)
        for idx, element in enumerate(self.arr[arr_index]):
            if element[0] == item:
                return element[1]


if __name__ == "__main__":
    t = Hash_Table()
    with open("nyc_weather.csv", "r") as wt:
        count = 0
        for line in wt:
            if count == 0:
                pass
            else:
                token = line.split(',')
                key = str(token[0])
                value = float(token[1])
                t[key] = value
            count += 1

    print(t.arr)
    print(t["Jan 9"])
    avg = 0
    for i in range(7):
        values = t[f"Jan {i}"]
        print(values)

