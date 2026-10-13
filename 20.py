chess = input()
let = 'abcdefgh'.find(chess[0])+1
if (let + int(chess[1])) % 2 == 0:
    print("черный")
else:
    print("нечерный")