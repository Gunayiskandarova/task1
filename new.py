
def username():
    name=input()
    if name=="Gunay": 
        print("enter your pasword")
        pasword=input()
        if pasword=="1234":
            print("Welcome")
            return True
        else: 
            print("incorrect your pasword") 
    else: 
        print( "Incorrect user name"  )
        return False
i=0
while i<10:
    username1=username()#true
    print(username1)
    i+=1

