N = int(input())
x = float(input())
s = input()

GC = 1
for i in s:
    if i == 'G' or i == 'C':
        GC *= (x / 2)
    else:
        GC *= ((1 - x) / 2)
print(1 - ((1 - GC) ** N))
"""
вероятность P того, что строка не такая как начальная 1 - GC
веротяность того, что таких строк N -> P ^ N
вероятность того, что хотя бы одна строка такая же - это 1 - веротяность того, что таких строк нет
1 - p ^ N 
"""