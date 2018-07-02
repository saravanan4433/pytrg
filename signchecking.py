#program to enter the numbers till the user  wants and last it should display the positive,negative and zero entered

#get the amount number user wants
s=int(input("enter amount of number :"))
#user input 
a=[]
for p in range(s):
    q=int(input())
    a.append(q)
print(a)
#counting positive,negative and zero present in user input
positive=0
negative=0
zero=0
for x in a:
    if x > 0:
        positive+=1
    elif x<0:
        negative+=1
    elif x==0:
        zero+=1
    else:
        print("enter valid number")

print("%s positive numbers is present" %(positive))
print("%s negative numbers is present" %(negative))
print("%s zero numbers is present" %(zero))

      
