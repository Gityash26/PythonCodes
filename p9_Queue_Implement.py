'''
_________________________________________________________________________________________________
===================================Queue Implementation==========================================
=================================================================================================
The Queue is a linear Data Structure.
Queue stores data in FIFO manner
         __________________________________________________
   <---  |____|____|____|____|____|____|____|____|____|____| <---
       front                                             Rear
      ()
Queue Operations : 
=> ENQUEUE OPERATION (Insertion)
=> DEQUEUE OPERATION (Deletion)
=> FRONT VALUE
=> REAR VALUE
=> DISPLAY OPERATION
'''

queue=[]
while True:
    choice = int(input('''\nQueue Operations :
          (1)-> ENQUEUE OPERATION
          (2)-> DEQUEUE OPERATION 
          (3)-> FRONT DISPLAY
          (4)-> REAR DISPLAY
          (5)-> DISPLAY QUEUE
          ---->Enter Your Choice : '''))

    if choice == 1:
        value = input("Enter Your value : ")
        queue.append(value)
        print(f"{value} enqueue Done")

    elif choice<1 or choice>5:
        break 

    elif queue:
        if choice == 2:
            print(f"{queue.pop(0)} Pop done")

        elif choice == 3:
            print(f"Front Queue Element : {queue[0]}")

        elif choice == 4:
            print(f"\nRear Queue Element : {queue[-1]}")
      
        elif choice == 5:
            print(f"\nDisplay Queue Element : {queue}")

    else:
        print("Queue is Empty")



























