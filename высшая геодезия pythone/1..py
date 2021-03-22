from random import randint as rd, sample 

n = int(input('Введите количество строк '))
m = int(input('Введите количество столбцов '))
a = [[rd(1,9) for i in range(m)] for j in range(n)]
tmp = []
s = 0
k = min(n, m)
for i in range(n) :
    if m > i :
        s += a[i][i] + (a[i][m - i - 1] if i != m - i - 1 else 0)
    print(*a[i])
    tmp.extend(a[i])
print()
 
print(s)