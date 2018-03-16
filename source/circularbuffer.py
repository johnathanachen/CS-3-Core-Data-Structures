#!python

class CircularBuffer(object):

    def __init__(self, max_size):
        self.array = []
        for items in range(max_size):
            self.array.append("")
        self.read_index = 0
        self.write_index = 0
        self.size = 0

    def __repr__(self):
        return 'Array({!r})'.format(self.array)

    def is_empty(self):
        if len(self.array) == 0:
            return True
        else:
            return False

    def is_full(self):
        if self.size == self.max_size:
            return True
        else:
            return False
        # if self.array.contains(""):
        #     return False
        # else:
        #     return True
        # if len(self.array) == self.max_size:
        #     return True
        # else:
        #     return False

    def enqueue(self, item):
        if self.is_empty and not self.is_full:
            self.array[self.size] = item
        else:
            self.front = item
        self.size += 1

    def front(self):
        if self.size == self.max_size:
            self.size = 0
            return self.array[self.size]
        else:
            print("pass")
            # self.size += 1
            # self.dequeue()

    def dequeue(self):
        pass
        # return self.array[self.size + 1]


if __name__ == '__main__':
    circular_buffer = CircularBuffer(3)
    circular_buffer.enqueue("a")
    circular_buffer.enqueue("b")
    circular_buffer.enqueue("c")
    # circular_buffer.enqueue("d")
    print(circular_buffer)



# class CircularBuffer(object):
#
#     def __init__(self, max_size):
#         self.array = []
#         self.read_index = 0
#         self.write_index = 0
#
#     def __repr__(self):
#         return 'Array({!r})'.format(self.array)
#
#     def _available_reading_space(self):
#         return self.write_index - self.read_index
#
#     def _available_writing_space(self):
#         return len(self.array) - self._available_reading_space
#
#     def is_empty(self):
#         return self._available_reading_space == 0
#
#     def is_full(self):
#         return self._available_writing_space == 0
#
#     def write(self, item):
#         if self.is_full == False:
#             self.array[self.write_index % len(self.array)] = item
#             print(item)
#             self.write_index += 1
#             return True
#         else:
#             return False
#
#     def read(self):
#         if self.is_empty == False:
#             item = self.array[self.read_index % len(self.array)]
#             self.read_index += 1
#             return item
#         else:
#             return None
#
#
#
# if __name__ == '__main__':
#     circular_buffer = CircularBuffer(5)
#     print(circular_buffer.write("a"))
#     print(circular_buffer.is_full())
#     print(circular_buffer.read())
