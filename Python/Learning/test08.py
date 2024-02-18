numbers = [5, 4, 0, 5, 9, 7, 9]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
    else:
        uniques.remove(number)
print(uniques)
