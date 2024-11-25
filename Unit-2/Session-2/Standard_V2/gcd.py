def gcd(num1, num2):
    if num1 <= num2 and num2%num1==0:
        return num1

    if num2 < num1 and num1%num2==0:
        return num2

    if num1 < num2:
        for num in range(int(num1/2)+1, 0, -1):
            if num2%num==0:
                return num
    else:
        for num in range(int(num2/2)+1, 0, -1):
            if num1%num==0:
                return num

    return -1

print(gcd(20, 15))