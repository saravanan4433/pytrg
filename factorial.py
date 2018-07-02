#program to add first seven term of the following series using a for loop 1/1!+2/2!+3/3!+.....

number=7
fact=1
value=0
#condition for the series upto seven term
for s in range(1,number+1):
    fact=fact*s
    value+=(s/fact)

print("value for first seven term is=%s" %(value))
