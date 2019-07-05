#This programe is create by Sujit Mandal
class Node:
    def __init__(self):
        self.info = None
        self.link = None

class linkList:
    def __init__(self):
        self.head = None
    
    def create(self):  
        temp = Node()
        temp.info = input('Enter node data: ')
        print('\n')
        print(temp.info + ' inserted into Linked List')
        temp.link = None

        if self.head == None:
            self.head = temp
            return
        else:
            newnode = Node()
            newnode = self.head

            while newnode.link != None:
                newnode = newnode.link
            newnode.link = temp

    def display(self):
        temp = Node()
        if self.head == None:
            print('\nList is empty!')
            return
        else:
            temp = self.head
            print('List is: ')
            while temp != None:
                print('info = ' + temp.info)
                temp = temp.link
        

list = linkList()

while True:
    print('\n1: ceate.')
    print('2: displaying.')
    print('3: exit.')

    choice = int(input('\nEnter the choice: '))

    if choice == 1:
        list.create()

    elif choice == 2:
        list.display()

    elif choice == 3:
        break
    else:
        print('\nInvalid choice!')
