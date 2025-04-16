#To print reverse String
txt= str(input("Enter the string value: "))
print(txt[::-1])
r=''
for i in txt:
    r=i+r
print(r)
