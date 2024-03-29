class Form:
    def __init__(self,d):
        self.d=d
    
    def register(self):
        l=[]
        rno=input("Enter the roll number: ")
        l.append(rno)
        name=input("Enter the name: ")
        l.append(name)
        psw=input("enter password : ")
        l.append(psw)
        email=input("Enter the emailid: ")
        l.append(email)
        d[rno]=l

    def login(self):
        rno=input("Enter the roll number: ")
        psw=input("Enter the password : ")
        if rno in d:
            if d[rno][2]==psw:
                print("succesful Login")
                while(True):
                    print("\n 1. Display \n 2. Logout \n")
                    x=int(input("Enter 1 or 2 : "))
                    if x==1:
                        self.display()
                    else:
                        self.logout()
                        break
            else:
                print("Invalid password")
        else:
            print("User does not Exist")
        

    def display(self):
        for i in d:
            c=0
            for j in d[i]:
                if c==2:
                    c+=1
                    continue
                else:
                    print(j, end="     ")
                    c+=1
        if len(d)==0:
            print("No data inserted")

    def logout(self):
        print("loged out")


d={}
f=Form(d)
while(True):
    print("*****************************")
    print("\n\n 1.Register \n 2. Login \n 3.Display  \nPress other to break\n")
    ch=int(input("Enter the choice : "))
    if ch==1:
        f.register()
    elif ch==2:
        f.login()
    elif ch==3:
        f.display()
    else:
        break

