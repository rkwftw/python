def fac(x):
    a = 1
    for i in range(1, x + 1):
        a *= i
        yield a

x = 10
for b, c in enumerate(fac(x)):
    print(f'#{b +1} {c}')