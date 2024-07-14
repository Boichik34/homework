from abc import ABC, abstractmethod


class Node:
    def __init__(self, data):
        self.__data = data
        self.next = None
        self.prev = None

    def get_data(self):
        return self.__data


class LinkedList:
    def __init__(self, type_iterator):
        self._type_iterator = type_iterator
        self.head = None
        self.tail = None
        self._size = 0
        self.iterators = {1: LeftRightIteratorStrategy,
                          2: RightLeftIteratorStrategy,
                          3: CenterIteratorStrategy}

    def get_size(self):
        return self._size

    def add(self, data):
        node = Node(data)

        if self._size == 0:
            self.head = node

        elif self._size > 0:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node
        self._size += 1

    def __iter__(self):
        return self.iterators[self._type_iterator](self)


class IIteratorStrategy(ABC):
    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __next__(self):
        pass


class LeftRightIteratorStrategy(IIteratorStrategy):
    def __init__(self, collection):
        self._collection = collection
        self._index = 0
        self._link = self._collection.head

    def __iter__(self):
        return self

    def __next__(self):

        if self._collection.get_size() > 0:

            while self._index < self._collection.get_size():
                result = self._link.get_data()

                self._link = self._link.next
                self._index += 1

                return result

            raise StopIteration


class RightLeftIteratorStrategy(IIteratorStrategy):
    def __init__(self, collection):
        self._collection = collection
        self._index = 0
        self._link = self._collection.tail

    def __iter__(self):
        return self

    def __next__(self):

        if self._collection.get_size() > 0:

            while self._index < self._collection.get_size():
                result = self._link.get_data()
                self._link = self._link.prev
                self._index += 1
                return result
            raise StopIteration


class CenterIteratorStrategy(IIteratorStrategy):
    def __init__(self, collection):
        self._collection = collection
        self._index = 0
        self._link = self._collection.head
        self._center_right_link = self.get_link()
        self._center_left_link = self.get_link().next

    def __iter__(self):
        return self

    def get_link(self):
        link = self._collection.head

        if self._collection.get_size() % 2 == 0:
            for i in range(self._collection.get_size() // 2 - 1):
                link = link.next
        elif self._collection.get_size() % 2 != 0:
            for i in range(self._collection.get_size() // 2):
                link = link.next
        return link

    def __next__(self):

        if self._collection.get_size() > 0:
            while self._index < self._collection.get_size():
                if self._collection.get_size() == 1:
                    self._index += 1
                    return self._collection.head.get_data()

                if self._collection.get_size() == 2:

                    result = self._link.get_data()
                    self._link = self._link.next
                    self._index += 1
                    return result
                else:
                    if self._collection.get_size() % 2 != 0:
                        center = self._collection.get_size() // 2
                    else:
                        center = self._collection.get_size() // 2 - 1

                    while self._index <= center:
                        result = self._center_right_link.get_data()
                        self._center_right_link = self._center_right_link.prev
                        self._index += 1
                        return result

                    result = self._center_left_link.get_data()
                    self._center_left_link = self._center_left_link.next
                    self._index += 1
                    return result

            raise StopIteration


lst = LinkedList(3)
lst.add(1)
lst.add(2)
lst.add(3)
lst.add(4)
lst.add(5)
lst.add(6)
lst.add(7)
lst.add(8)
lst.add(9)


for i in lst:
    print(i)