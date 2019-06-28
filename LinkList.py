class Node:
    def __init__(self):
        self.info = None
        self.link = None

class linkList:
    def __init__(self):
        self.head = None
    
    def create(self,info):
        info = input('Enter node data: ')
        node = Node()
        node.info = info
        node.link = self.head
        self.head = node
        print('\n')
        print(info + ' inserted into Linked List')

    def display(self):
        if self.head is None:
            print('\nList is empty!')
            return
        else:
            print('List is: ')
            p = self.head
            while p is not None:
                print('info = ' + p.info)
                p = p.link
            print()

list = linkList()

while True:
    print('\n1: ceate.')
    print('2: displaying.')
    print('3: exit.')

    choice = int(input('\nEnter the choice: '))

    if choice == 1:
        list.create(1)

    elif choice == 2:
        list.display()

    elif choice == 3:
        break
    else:
        print('\nInvalid choice!')