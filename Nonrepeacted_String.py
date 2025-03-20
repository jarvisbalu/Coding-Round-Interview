#To Print The Non-Repeacted String
txt= str(input("Enter the string value: "))
print(sum(1 for i in txt.lower() if txt.lower().count(i)==1))

#To Print The Non-Repeacted Letter
nrep=''
for i in txt.lower():
    if txt.lower().count(i)==1:
        nrep+=i
print("The Non-repeacted Letter is:", nrep)