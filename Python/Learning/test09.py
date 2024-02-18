phone = input("Phone: ")

numbers = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}

output = ""
for character in phone:
   output += numbers.get(character, "!") + " " #kdybi jsem vynechal nake cislo v numbers nasalo by to vikřiník
print(output)