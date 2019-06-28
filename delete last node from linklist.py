#This programe is create by Sujit Mandal
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

    def deleteLastNode(self):
        if self.head is None:
            return
        if self.head.link is None:
            self.head = None
            return

        p = self.head
        while p.link.link is not None:
            p = p.link
        p.link = None
        
        print('\nlist after deleted.')
        self.display()
        
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
    print('3: delete last node.')
    print('4: exit.')

    choice = int(input('\nEnter the choice: '))

    if choice == 1:
        list.create(1)

    elif choice == 2:
        list.display()
    
    elif choice == 3:
        list.deleteLastNode()

    elif choice == 4:
        break
    else:
        print('\nInvalid choice!')
