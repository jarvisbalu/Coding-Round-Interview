#Prime number
start=int(input("Enter the starting number: "))
end=int(input("Enter the end number: "))
prime=[]
nonprime=[]
for i in range(start, end):
    if i<2:
        nonprime.append(i)
        continue
    for j in range(2, int(i**0.5)+1):
        if i%j==0:
            nonprime.append(i)
            break
    else:
        prime.append(i)
print("The prime numbers are: ", prime)
print("The Non-prime numbers are: ", nonprime)
# print("Prime length", len(prime))
# print("Non-Prime length", len(nonprime))