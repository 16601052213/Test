# 1.Node类
class Node:
    def __init__(self, initdate):
        self.date = initdate
        self.next = None

    def getDate(self):
        return self.date

    def getNext(self):
        return self.next

    def setDate(self, newdate):
        self.date = newdate

    def setNext(self, newdate):
        self.next = newdate


class UnorderedList:
    # 无序列表
    def __init__(self):
        self.head = Node

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def length(self):
        current = self.head
        count = 0
        while current != Node:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while not found and current != Node:
            if current.getDate() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = Node
        found = False
        while not found:
            if current.getDate() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


class OrderedList:
    # 有序列表类
    def __init__(self):
        self.head = Node

    def length(self):
        current = self.head
        count = 0
        while current != Node:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while not found and current != Node:
            if current.getDate() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = Node
        found = False
        while not found:
            if current.getDate() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while not found and current != Node and not stop:
            if current.getDate() == item:
                found = True
            elif current.getDate() > item:
                stop = True
            else:
                current = current.getNext()
        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getNext() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
        temp = Node(item)
        if previous == Node:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)


if __name__ == '__main__':
    # 实例化无序列表
    mylist = UnorderedList()
    # 实例化有序列表
    mylist = OrderedList()
