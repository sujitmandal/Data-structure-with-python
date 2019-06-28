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

    def deleteinfo(self,value):
        value = input('Enete the value for delete: ')
        if self.head is None:
            print('\nList is empty!')
            return

        #delete first node
        if self.head.info == value:
            self.head = self.head.link
            return

        #delete in between or at the end
        p = self.head
        while p.link is not None:
            if p.link.info == value:
                break
            p = p.link

        if p.link is None:
            print('\nvalue ',value + 'is not in list')
        else:
            p.link = p.link.link

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
    print('3: delete info.')
    print('4: exit.')

    choice = int(input('\nEnter the choice: '))

    if choice == 1:
        list.create(1)

    elif choice == 2:
        list.display()
    
    elif choice == 3:
        list.deleteinfo(1)

    elif choice == 4:
        break
    else:
        print('\nInvalid choice!')