
subj = {}
with open('text6.txt') as file:
    lines = file.readlines()
    for line in lines:
        x = line.split()
        hours = 0
        for el in x[1:]:
            if el != "-":
                num = "0"
                for i in el:
                    if i.isdigit():
                        num += i
                    else:
                        break
                hours += int(num)
        subj.update({x[0].strip(":"): hours})
print(subj)