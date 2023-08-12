'''
_________________________________________________________________________________________________
===================================Stack Implementation==========================================
=================================================================================================
The stack is a linear data structure
Data stores in LIFO or FIFO manner

=> Stack Operations : 
PUSH -> Insertion
POP  -> Deletion
PEEK -> Display Last Element
DISPLAY -> Display List  
'''

stack = []
while True:
    choice = int(input('''\nStack Operations :
          (1)-> PUSH OPERATION
          (2)-> POP OPERATION 
          (3)-> PEEK OPERATION
          (4)-> DISPLAY STACK
          ---->Enter Your Choice : '''))

    if choice == 1:
        value = input("Enter Your value : ")
        if value.isdigit():
            value = eval(value)
        stack.append(value)
        print(f"{value} Push Done")

    elif choice<1 or choice>4:
        break 

    elif stack:
        if choice == 2:
            print(f"{stack.pop()} Pop done")

        elif choice == 3:
            print(f"Last Element Value : {stack[-1]}")

        elif choice == 4:
            print(f"\nDisplay Stack : {stack}")

    else:
        print("Stack is Empty")
