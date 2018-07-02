#program for find the range of a set of numbers. Rangeis the difference between the smallest and biggest number inthe list.

#user input for the amount of numbers
a=int(input("enter the amount of numbers:"))
#create list of numbers
d=[]
for b in range(a):
    c=int(input("enter the number:"))
    d.append(c)
print(d)
#find the maximum and minimum number in the range
print("%s maximum number in the list"%(max(d)))
print("%s minimum number in the list"%(min(d)))
print("diifference between the range is %s"%(max(d)-min(d)))
