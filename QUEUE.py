class Stack:
    def queue(self,s,n,x):
        if len(s)==n:
            print("\n<<<<< OverFlow >>>>>>")
            print("\n")
        else:
            s.append(x)
            print(x,"is inserted into the queue \n")
    def dequeue(self,s,n):
        if len(s)==0:
            print("\n<<<<<< UnderFlow >>>>>>")
            print("\n")
        else:
            s.pop(0)
    def peek(self,s):
        if len(s)==0:
            print("No Elements in the queue")
        else:  
            print(s[-1])
    def display(self,s):
        if len(s)==0:
            print("No Elements in the queue")
        else:
            for i in s:
                print(i,end=" ")
            print()
n=int(input("Enter the size of the queue: "))
s=[]
cl=Stack()
while(True):
    print("\n************************5*****\n 1. Enqueue \n 2. Dequeue \n 3. Peek \n 4. Display \nPress other to exit")
    c=int(input("Enter your choice: "))
    print()
    if c==1:
        x=int(input("Enter the number to push : "))
        print()
        cl.queue(s,n,x)
    elif c==2:
        cl.dequeue(s,n)
    elif c==3:
        cl.peek(s)
    elif c==4:
        cl.display(s)
    else:
       break 

    
