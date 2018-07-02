#program to find the number of time the word "Rama" comes in the Ramayana (2).txt file.

#open the ramayana txt file
fh=open("C:/Users/Sara/Desktop/Ramayana (2).txt","r",encoding='utf8')
#read the file
s=fh.read()
#create a list of word in the file
words=s.split()

#condition for search the word "rama"
countrama=0
y="Rama"
for x in words:
    if y in x:
        countrama=countrama+1
print("%s times Rama present in the document" %(countrama))
    


