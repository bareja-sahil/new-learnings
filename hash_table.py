MAX_SIZE = 4096
def get_index(data_list, key):
    index = 0
    for charc in key:
        index += ord(charc)
    index = index % len(data_list)
    return index


def get_valid_index(data_list, key):
    index = get_index(data_list, key)
    while True:
        if data_list[index] is None:
            return index
        else:
            k, v = data_list[index]
            if k == key:
                return index
            index += 1
        if len(data_list) == index:
            index = 0


class HashTable:
    data_list = [None] * MAX_SIZE

    def __setitem__(self, key, value):
        index = get_valid_index(self.data_list, key)
        self.data_list[index] = (key, value)

    def __getitem__(self, item):
        index = get_valid_index(self.data_list, item)
        if self.data_list:
            return self.data_list[index][1]

    # def __str__(self):
    #     return (', ').join([data[0], data[1] for data in self.data_list if data is not None])

    def list_all(self):
        return [data for data in self.data_list if data is not None]

    # def __init__(self):
    #     self.data_list = [None] * 4096
    #
    # def insert(self, key, value):
    #     index = get_valid_index(self.data_list, key)
    #     self.data_list[index] = (key, value)

    # def find(self, key):
    #     return self.data_list[]

    # def update(self, key, value):
    #     index = get_index(self.data_list, key)
    #     self.data_list[index] = (key, value)
    #



has_table = HashTable()
has_table['silent'] = 5
has_table['listen'] = 5
has_table['wow'] = 23
print(has_table.list_all())
has_table['wow'] = 25
print(has_table.list_all())
# print(get_index(data_list, 'silent'))
# print(get_index(data_list, 'listen'))
#
#
# print(get_valid_index(data_list, 'silent'))
# print(get_valid_index(data_list, 'listen'))