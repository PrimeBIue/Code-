class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def appendNode(self,value):
        newNode = Node(value)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = newNode

    def length(self):
        curr_idx = 0
        curr = self.head
        while curr.next != None:
            curr = curr.next
            curr_idx += 1
        return curr_idx

    def display(self):
        arr = []
        curr = self.head
        while curr.next != None:
            curr = curr.next
            arr.append(curr.data)
        return arr

    def insertNode(self,value,index):
        length = self.length()
        if index > length:
            print('Out of range')
            return
        elif index == length:
            self.appendNode(value)
            return
        else:
            newNode = Node(value)
            curr_idx = 0
            curr = self.head
            while True:
                temp = curr
                curr = curr.next
                if curr_idx == index:
                    temp.next = newNode
                    newNode.next = curr
                    return
                curr_idx += 1

    def eraseNodeIdx(self,index):
        length = self.length()
        if index > length:
            print('Out of range')
            return
        else:
            curr_idx = 0
            curr = self.head
            while curr.next != None:
                temp = curr
                curr = curr.next
                if curr_idx == index:
                    temp.next = curr.next
                    del(curr)
                    return
                curr_idx += 1

    def eraseList(self):
        #self.head = Node()
        for i in range(self.length()):
            self.eraseNodeIdx(0)
        return

    def removeDups(self):
        setVals = set()
        curr = self.head
        while curr.next != None:
            temp = curr
            curr = curr.next
            if curr.data not in setVals:
                setVals.add(curr.data)
            else:
                temp.next = curr.next
                del(curr)
                curr = temp
        return

    def invert(self):
        arr = self.display()
        curr = self.head
        curr_idx = 0
        while curr.next != None:
            curr = curr.next
            curr.data = arr[-(curr_idx+1)]
            curr_idx += 1
        return

    def countNum(self,value):
        count = 0
        curr = self.head
        while curr.next != None:
            curr = curr.next
            if value == curr.data:
                count += 1
        return count

def main():

    # create linked list
    list_1 = LinkedList()
    print(f'empty list: \n{list_1.display()}\n')

    # add values
    for i in range(5):
        list_1.appendNode(i)
    print(f'list with values: \n{list_1.display()}\n')

    # add value '1' on index 3
    list_1.insertNode(1,3)
    print(f'added \'1\' on index 3: \n{list_1.display()}\n')

    # erase value on index 0
    list_1.eraseNodeIdx(0)
    print(f'erased value on index 0: \n{list_1.display()}\n')

    # remove duplicate values
    list_1.appendNode(2)
    list_1.appendNode(2)
    list_1.appendNode(1)
    list_1.appendNode(1)
    print(f'list with dups: \n{list_1.display()}\n')
    print(f'count how many dups of \'1\': \n{list_1.countNum(1)}\n')
    list_1.removeDups()
    print(f'list without dups: \n{list_1.display()}\n')

    # invert list
    list_1.invert()
    print(f'inverted list: \n{list_1.display()}\n')

    # erase list
    list_1.eraseList()
    print(f'empty list: \n{list_1.display()}\n')

if __name__ == '__main__':
    main()