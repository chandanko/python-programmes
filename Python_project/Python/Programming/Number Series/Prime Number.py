# The number divisible by 1 and itself

N = int(input("Enter a  number->"))
count = 0
for i in range(1, N + 1):
    if N % i == 0:
        count += 1
if count == 2:
    print("Given Number is prime")
else:
    print("Given  Number is Not a prime")
