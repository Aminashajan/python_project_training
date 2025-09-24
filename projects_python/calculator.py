print("==calculator==")



final=""

while(final!='q'):
    a=int(input("enter the value of a"))
    b=int(input("enter the value of b"))
    choice=input("enter your choice[+,-,*,/,%]: ")

    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mult(a,b):
        return a*b
    def div(a,b):
        return a//b
    def  mod(a,b):
        return a%b
    


    if choice=="+":
        print(add(a,b))
    elif choice=="-":
        print(sub(a,b))
    elif choice=="*":
        print(mult(a,b))
    elif choice=="/":
        if b==0:
            print("divide by zero is not allowed")
        else:
            print(div(a,b))
    elif choice=="%":
        print(mod(a,b))

    final=input("do u want to quit[q] or resume[r]")

else:
    print("thank u")



   





