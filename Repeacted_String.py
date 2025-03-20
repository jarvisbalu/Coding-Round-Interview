#To Print Number of Repeacted String
txt= str(input("Enter the String: "))
print(len(txt)-len(set(txt.lower())))

#To Print Repeacted String
rep=''
for i in txt.lower():
    if txt.lower().count(i)>1 and i not in rep:
        rep+=i
print("The Repeacted Letters is:", rep)