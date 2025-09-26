import guess 
def login():
    while True:
        pwsd=int(input("enter the password= "))
        if pwsd==2004:
            print("in process!!please wait")
            guess.game()
        else:
            print("invalid !try again")

if __name__=="__main__":
    print("welcome")
    login()
    #count+=1


# len
#.upper()
#.lower()
#strip-removes whitespaces between characters
#replace

#text="hello world"
#print(text.replace("hello","world"))
#print(text.split(","))

#.find()
#.index()
#.startswith() return type t/f
#.endswith()   "       "   ""
#name=input("enter your name")
'''
while True:
    
    user=input("you:")
    if user.lower() in ["quit"]:
        print("ok good bye")
        break
    elif user.lower() in ["hello","hi"]:
        print(f"hello! How can i help you")
    elif user.lower() in ["i need some datas about ml","ml","ml algorithm"]:
        print(f"well!Machine learning is a subsset of AI that is useful in decision making.there are various algorithms used to train the machine")
    elif user.lower() in ["ok","thank you","good bye"]:
        print(f"your welcome ")
    else:
        print("i dont aware of it")    
        
        
    '''
    


        
  
        
