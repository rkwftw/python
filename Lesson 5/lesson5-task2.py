with open("text2.txt") as file:
    line1 = file.readlines()
    for i, line in enumerate(line1):
        w_count = len(line.split())
        print(f'в {i + 1} строке {w_count} слов(а)')