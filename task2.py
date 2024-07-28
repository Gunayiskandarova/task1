# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# s=0
# for i in a:
#     s=s+i
# print(s)


# b=[]
# def name(a):
#     for i in range(1,a):
#         b.append(i)
#     return b
# a=11
# name(a)
# print(b)

def username(name,pasword):
   

    if name=="Gunay": 
        print("enter your pasword")

    else: 
        print("Incorrect user name")   
    if pasword=="1234":
        print("Welcome")
    else: print("incorrect your pasword") 

    return username

name=input()
pasword=input()
username("Gunay", 1234)
print(username)

