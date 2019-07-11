    
#This programe is create by Sujit Mandal
class Node:
    def __init__(self):
        self.info = None
        self.next = None

class linkList:
    def __init__(self):
        self.head = None
    
    def create(self):
        temp = Node()
        temp.info = input('Enter node data: ')
        print('\n')
        print(temp.info + ' inserted into Linked List')
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
    
    def reverseList(self):
        if self.head == Node:
            print('\nList is Empty!')
                
        else:
            prve_node = None
            cur_node = self.head
            
            while cur_node != None:
                temp = cur_node.next
                cur_node.next = prve_node
                prve_node = cur_node
                cur_node = temp
            self.head = prve_node

            print('\nlist after reversing.')
            self.display()
        
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
                temp = temp.next

list = linkList()

while True:
    print('\n1: ceate.')
    print('2: displaying.')
    print('3: reverse.')
    print('4: exit.')

    choice = int(input('\nEnter the choice: '))

    if choice == 1:
        list.create()

    elif choice == 2:
        list.display()

    elif choice == 3:
        list.reverseList()

    elif choice == 4:
        break
    else:
        print('\nInvalid choice!')