num = int(input("Enter a number: "))
if num % 7 == 0 and num % 9 == 0:
    print(num, "is divisible by both 7 and 9")
else:
    print(num, "is not divisible by both 7 and 9")