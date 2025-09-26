print("BODY MASS INDEX")
def inputbmi():
    name=input("enter your name :")
    age=int(input("enter your age : "))
    weight=int(input("enter your weight : "))
    height=int(input("enter your height"))
    return weight,height



def bmi():
    weight,height=inputbmi()
    bmindex=weight//(height**2)
    print(bmindex)

    if bmindex<18:
        print("underweight")
    elif bmindex>=19 and bmi<25:
        print("normal weight")
    elif bmindex>=25 and bmi<=30:
        print("overweight")
    else:
        print("obesity")

if __name__=="__main__":
    print("body mass index")
    bmi()

