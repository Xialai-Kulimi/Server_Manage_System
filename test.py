import math
import time

n = input("n= e.g. 12/5:").split("/")  # 輸入所求數值
ti = time.time()  # 初始時間
n[0] = int(n[0])  # 分子
n[1] = int(n[1])  # 分母
x = math.gcd(n[0], n[1])  # 分子,分母的最大公因數
n[0] = n[0] / x
n[1] = n[1] / x  # 化為最簡分數
# print(n)
m = [int(n[0] ** 0.5) + 1, int(n[1] ** 0.5) + 1]  # 迴圈的起始條件
# print(m)
ans = [[1, 1], [1, 1]]  # 根式有理化的結果 ans[0][0]為分子的a sqrt(b) 的a
for i in range(2):
    k = m[i]
    while k > 0:
        y = k * k
        if n[i] % y == 0:
            ans[i][0] = k
            ans[i][1] = n[i] // y
            break
        if i == 1:
            ans[i][1] = n[i]
            break
        k -= 1
print(ans)
if ans[1][1] != 1:
    ans[0][1] *= ans[1][1]
    ans[1][0] *= ans[1][1]
    ans[1][1] = 1
    print('alsdhfklasjdhfkasjdhflaksdjfhaklsdf')

print(ans[0][1])
i = int(math.sqrt(ans[0][1])) + 1
print(i)

while i > 0:
    y = i * i
    if ans[0][1] % y == 0:
        ans[0][0] *= i
        ans[0][1] = ans[0][1] // y
        break
    if i == 1:
        ans[1] = n
        # print("sqrt("+str(n)+"😞"+"sqrt("+str(ans[1])+")")
        break
    i -= 1
# print(ans)
x = math.gcd(int(ans[0][0]), int(ans[1][0]))
ans[0][0] = ans[0][0] / x
ans[1][0] = ans[1][0] / x
for i in range(2):
    for j in range(2):
        ans[i][j] = int(ans[i][j])
tf = time.time()
if ans[0][0] != 1 and ans[0][1] != 1 and ans[1][0] != 1:
    print("ans=" + str(ans[0][0]) + "sqrt(" + str(ans[0][1]) + ")/" + str(ans[1][0]))
elif ans[0][0] == 1:
    print("ans=" + "sqrt(" + str(ans[0][1]) + ")/" + str(ans[1][0]))
elif ans[0][1] == 1:
    print("ans=" + str(ans[0][0]) + "/" + str(ans[1][0]))
elif ans[1][0] == 1:
    print("ans=" + str(ans[0][0]) + "sqrt(" + str(ans[0][1]) + ")")
else:
    print("ans=1")
print("it costs", tf - ti)
time.sleep(10)
