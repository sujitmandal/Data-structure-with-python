    
#This programe is create by Sujit Mandal
class Node:
    def __init__(self):
        self.info = None
        self.next = None

class stack:
    def __init__(self):
        self.head = None
    
    def push(self):
        temp = Node()
        temp.info = input('Enter node data: ')
        print('\n')
        print(temp.info + ' push/inserted into Queue.')
        temp.next = None

        if self.head == None:
            self.head = temp
            return
        else:
            newnode = Node()
            newnode = self.head

            while newnode.next != None:
                newnode = newnode.next
            newnode.next = temp
            return(newnode)

    def pop(self):
        if self.head == None:
            print('\nQueue Underflow!')
        else:
            self.head = self.head.next

            print('\nQueue after deleted/pop.')
            self.display()

    def display(self):
        temp = Node()
        if self.head == None:
            print('\nQueue is empty!')
            return
        else:
            temp = self.head
            print('List is: ')
            while temp != None:
                print('info = ' + temp.info)
                temp = temp.next

list = stack()

while True:
    print('\n1: insert/push')
    print('2: delete/pop.')
    print('3: displaying.')
    print('4: exit.')
        
    choice = int(input('\nEnter the choice: '))

    if choice == 1:
        list.push()

    elif choice == 2:
        list.pop()

    elif choice == 3:
        list.display()

    elif choice == 4:
        break
    else:
        print('\nInvalid choice!')