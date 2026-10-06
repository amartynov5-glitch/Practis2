a = int(input())
d = []
while a > 0:
    d.append(a%10)
    a //= 10
d.reverse()
if d[0] == d[-1] and d[1]==d[-2]:
    print('Настоящее')
else:
    print('Кривое')