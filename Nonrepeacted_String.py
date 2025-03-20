#To Print Number of Repeacted String
txt= str(input("Enter the string value: "))
print(sum(1 for i in txt.lower() if txt.lower().count(i)==1))