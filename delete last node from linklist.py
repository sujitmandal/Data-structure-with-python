    
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
            return(newnode)

    def deleteLastNode(self):
        if self.head == None:
            print('\nList is Empty!')
        else:
            last_node = self.head
            while(last_node.next != None):
                peve_node = last_node
                last_node = last_node.next
            peve_node.next = None
            

            print('\nlist after deleted.')
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
    print('3: delete last node.')
    print('4: exit.')

    choice = int(input('\nEnter the choice: '))

    if choice == 1:
        list.create()

    elif choice == 2:
        list.display()
    
    elif choice == 3:
        list.deleteLastNode()

    elif choice == 4:
        break
    else:
        print('\nInvalid choice!')