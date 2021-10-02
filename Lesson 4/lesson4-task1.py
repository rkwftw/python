import sys
if len(sys.argv) < 4:
    raise ValueError("Введите выработку, ставку, премию")
else:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    res = a * b + c
    print(res)
