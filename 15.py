n, k, m = map(int, input().split())
vpered = (m - k) % n '''оказывается % работает для минуса иначе 
                        (= -2+n % n)'''
nasad = (k-m) % n
print(min(vpered, nasad)-1)
