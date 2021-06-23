def search_using_linear_search(iterable, data):
    for index, value in enumerate(iterable):
        if value == data:
            return index

def search_using_binary_search(iterable, data):
    left_limit = 0
    right_limit = len(iterable) - 1
    mid_index = 0


