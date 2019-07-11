    
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

    def deleteinfo(self,value):
        if self.head == None:
            print('\nList is Empty!')
        
        else:
            value = input('Enete the value for delete: ')
            if self.head is None:
                print('\nList is empty!')
                return

            #delete first node
            if self.head.info == value:
                self.head = self.head.next
                return

            #delete in between or at the end
            temp = self.head
            while temp.next != None:
                if temp.next.info == value:
                    break
                temp = temp.next

            if temp.next == None:
                print('\nvalue ',value + 'is not in list')
            else:
                temp.next = temp.next.next

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
    print('3: delete info.')
    print('4: exit.')

    choice = int(input('\nEnter the choice: '))

    if choice == 1:
        list.create()

    elif choice == 2:
        list.display()
    
    elif choice == 3:
        list.deleteinfo(1)

    elif choice == 4:
        break
    else:
        print('\nInvalid choice!')