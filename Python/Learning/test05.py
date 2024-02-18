name = input("Choose your name: ")

if len(name) < 3:
    print("Your name must be at least 3 chracters long.")

elif len(name) > 10:
    print("Your name can't be more than 10 characers long.")

else:
    print(f'name "{name}" is great.')
