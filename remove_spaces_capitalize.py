sentence = input("Enter your sentence here: ")

capitalized = ""
removed_spaces = ""
first_word = True

for character in sentence:
    if character == " ":
        capitalized += character
        first_word = True
    else:
        if first_word and "a" <= character <= "z":
            character = chr(ord(character) - 32)
        capitalized += character
        removed_spaces += character
        first_word = False

print("Capitalized: ", capitalized)
print("No spaces: ", removed_spaces)