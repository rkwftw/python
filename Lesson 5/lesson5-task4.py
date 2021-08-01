endict = {
    "One" : "Odin",
    "Two" : "Dva",
    "Three" : "Tri",
    "Four" : "Chetiri"
}

with open("text4.txt") as file, open("text4_1.txt", "w") as file1:
    line1 = file.readlines()
    for line in line1:
        i = line.split()
        rudict = endict.get(i[0])
        print(rudict)
        file1.write(f'{line.replace(i[0], rudict)}')