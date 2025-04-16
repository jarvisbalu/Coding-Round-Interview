from collections import Counter
t=input('Enter the string: ')
print(dict(Counter(t.lower())))

d={}
for i in t.lower():
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)