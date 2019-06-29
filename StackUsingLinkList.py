#This programe is create by Sujit Mandal
class Node:
    def __init__(self):
        self.info = None
        self.link = None

class stack:
    def __init__(self):
        self.head = None
    
    def pus(self,info):
        info = input('Enter node data: ')
        node = Node()
        node.info = info
        node.link = self.head
        self.head = node
        print('\n')
        print(info + ' inserted into Linked List')

    def pop(self):
        if self.head == None:
            print('\nStack Underflow')
        else:
            print('\n')
            print(self.head.info + ' deleted from stack.')
            self.head = self.head.link

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

list = stack()

while True:
    print('\n1: insert/push')
    print('2: delete/pop.')
    print('3: displaying.')
    print('4: exit.')
        
    choice = int(input('\nEnter the choice: '))

    if choice == 1:
        list.pus(1)

    elif choice == 2:
        list.pop()

    elif choice == 3:
        list.display()

    elif choice == 4:
        break
    else:
        print('\nInvalid choice!')