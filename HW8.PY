n=int(input("Enter the number:"))
reverse = 0

temp = n
while temp>0:
    remen = temp%10
    reverse = remen + (reverse*10)
    temp = int(temp/10)

    if reverse==n:
        print("Palindorme number")
else:
        print("Not palindrome number")        