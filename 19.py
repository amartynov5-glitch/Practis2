n, m = map(int, input().split('x'))
k = int(input())
hor = (k % m == 0) and (k // m < n)
vert = (k % n == 0) and (k // n < m)
if hor or vert:
    print("успешно")
else:
    print("неосуществимо")