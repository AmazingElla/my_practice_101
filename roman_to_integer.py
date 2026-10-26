def roman_to_integer(roman):
    symbols = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    for symbol in roman:
        if symbol not in symbols:
            return "Invalid Roman numeral"
    
    total = 0
    i = 0

    while i < len(roman):
        if i + 1 < len(roman) and symbols[roman[i]] < symbols[roman[i + 1]]:
            total += symbols[roman[i + 1]] - symbols[roman[i]]
            i += 2
        else:
            total += symbols[roman[i]]
            i += 1

    return total

print(roman_to_integer("IIIW"))  
print(roman_to_integer("LVIII"))
print(roman_to_integer("MCMXCIV"))
print(roman_to_integer("IV")) 

