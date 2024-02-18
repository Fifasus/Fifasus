def emogy_conventer(msg):
    words = msg.split(" ")
    emogy = {
    ":)": "😁",
    ":(": "😫"
    }
    output = ""
    for thing in words:
        output += emogy.get(thing, thing) + " "
    return output
 
 
msg = input("> ")
print(emogy_conventer(msg))