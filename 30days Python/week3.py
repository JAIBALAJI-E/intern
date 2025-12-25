#print 1 - 100
for i in range(101):
    print(i)

#sum of numbers
n = 2345
total = 0
while n > 0:
    digit = n % 10
    total = total + digit
    n = n // 10
print(total)

#armstrong
n = int(input("Enter number: "))
temp = n
digits = len(str(n))
total = 0
while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10
if total == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")