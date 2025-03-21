# Counter of The String
from collections import Counter
cont= input("Enter the value: ")
print(dict(Counter(cont)))

# Without Counter
num={}
for i in cont:
    num[i]= num.get(i, 0)+1
print(num)