#even or odd
n = int(input("Enter the number; "))
if n % 2 == 0:
    print("Even number")
else:
    print("Odd Number")

#largest of 3num
arr = [10, 20, 30]
largest=arr[0]
for i in arr:
    if largest > i:
        i = largest
print(i)

#pos neg zer
n = 10
if n < 0:
    print("Negative numbner")
elif n == 0:
    print("zero")
else:
    print("Positive number")