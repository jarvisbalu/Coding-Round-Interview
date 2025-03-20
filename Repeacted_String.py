#To Print Number of Repeacted String
txt= str(input("Enter the String: "))
print(len(txt)-len(set(txt.lower())))