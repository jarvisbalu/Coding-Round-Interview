start= int(input("Enter the starting number: "))
end= int(input("Enter the end number: "))
odd=[]
even=[]
for i in range(start, end):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("The odd number:", odd)
print("The even number:", even)