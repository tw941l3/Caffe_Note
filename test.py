from datetime import datetime


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        # 建立 class Node 的instance(實體)
        new_node = Node(data)

        # 如果head == None 代表為第一個Node
        if self.head == None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = self.tail.next

    def delete(self):
        if self.head == None:
            return print("This list is empty")
        else:
            if self.head.next == None:
                self.head = None
            else:
                current_node = self.head
                while current_node != None:
                    self.tail = current_node
                    current_node = current_node.next
                self.tail.next = None


if __name__ == "__main__":

    start = datetime.now()

    s = SingleLinkedList()

    s.append(1)
    s.delete()
    s.delete()

    print(datetime.now()-start)
