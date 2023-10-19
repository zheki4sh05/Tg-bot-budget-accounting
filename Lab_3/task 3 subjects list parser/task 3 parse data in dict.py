subjects = dict()
with open("database.txt", "r") as source:
    for line in source:
        line_items = line.split()
        sum = 0
        i = 1
        while i < len(line_items):
            sum += int(line_items[i].split("(")[0])
            i += 1
        subjects[line_items[0]] = sum
print(subjects)
