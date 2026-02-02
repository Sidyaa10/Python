#A project to build a translator

def translator(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOIaeiou":
            translation = translation + "d"
        else:
            translation = translation + letter
    return translation

print(translator(input("Enter a phrase:")))

#Dumb AHH translator do better