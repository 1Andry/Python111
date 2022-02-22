class Node:
    def __init__(self, elem):
        self.__data = elem
        self.__next = None

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def set_data(self, new_data):
        self.__data = new_data

    def set_next(self, new_next):
        self.__next = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def list_print(self):
        val = self.head
        while val:  # val is not None
            print(val.get_data(), end=" ")
            val = val.get_next()
        print()

    def add(self, item):
        tmp = Node(item)
        tmp.set_next(self.head)
        self.head = tmp

    def append(self, item):
        new_item = Node(item)
        if self.head is None:
            self.head = new_item
            return

        end = self.head
        while end.get_next():
            end = end.get_next()
        end.set_next(new_item)

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.get_next()
        return count

    def insert(self, position, item):
        if position > self.size():
            raise IndexError("Индекс находится за пределами списка.")

        current = self.head
        previous = None
        pos = 0
        if position == 0:
            self.add(item)
            return
        else:
            new_node = Node(item)
            while pos < position:
                pos += 1
                previous = current
                current = current.get_next()
            previous.set_next(new_node)
            new_node.set_next(current)

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

ls = LinkedList()
ls.add(1)
ls.add(2)
ls.add("a")
ls.add("b")
print(ls.search("a"))
print(ls.search(3))