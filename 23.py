n = int(input())
if n == 1:
    print(0)
else:
    n = n - 1
    if n <= 9:
        print(n)
    else:
        n = n - 9
        if n <= 180:
            num = 10 + (n - 1) // 2
            if n % 2 == 1:
                print(num // 10)
            else:
                print(num % 10)
        else:
            n = n - 180
            num = 100 + (n - 1) // 3
            pos = (n - 1) % 3
            if pos == 0:
                print(num // 100)
            elif pos == 1:
                print((num // 10) % 10)
            else:
                print(num % 10)