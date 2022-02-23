class Node:
    def __init__(self, elem):
        self.__data = elem  # элемент
        self.__next = None  # ссылка на следующий узел

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
        tmp = Node(item)  # создаем элемент
        tmp.set_next(self.head)  # прикрепляем новый элемент к списку
        self.head = tmp  # адрес нового элемента помещаем в голову

    def append(self, item):
        new_item = Node(item)
        if self.head is None:
            self.head = new_item
            return

        end = self.head
        while end.get_next():  # доходим до последнего элемента
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

    def search(self, item):  # поиск по значению
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def pop(self, position=None):
        ret = None
        current = self.head
        if position is None:
            ret = current.get_data()
            self.head = current.get_next()
        elif position > self.size() - 1:
            raise IndexError("индекс за пределами списка")
        else:
            pos = 0
            previous = None
            while pos < position:
                previous = current
                current = current.get_next()
                pos += 1
                ret = current.get_data()
            previous.set_next(current.get_next())
        print(ret)
        return ret

    def revers(self):
        p = self.head
        self.head = None
        while p is not None:
            p0, p = p, p.get_next()
            p0.set_next(self.head)
            self.head = p0

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while found is not True:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self.head = current.getNext()
        else:
            previous.set_next(current.get_next())

    def index(self, item):
        pos = 0
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
                pos += 1
                if pos > self.size() - 1:
                    return None
        return f"индекс = {pos}"


temp = LinkedList()
temp.add(31)
temp.add(77)
temp.append(26)
temp.append(6)
temp.append(54)
temp.list_print()
print(temp.index(6))
