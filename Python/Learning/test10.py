msg = input("> ")
words = msg.split(" ")
emogy = {
    ":)": "😁",
    ":(": "😫"
}
output = ""
for thing in words:
    output += emogy.get(thing, thing) + " "
    
print(output)

#WORDS = vse oddelene carkou (slova + smajliky)
#THING = jednotlivé "slovo" z WORDS

#   emogy.get(thing, thing) 
#    ^ u každého "slova" zjisti jestli se nachází mezi EMOGY ---jestli ano napiš smajlíka
#                                                            \jestli ne napiš slovo