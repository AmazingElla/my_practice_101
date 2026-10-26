def anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    dict1 = {}
    dict2 = {}

    for char in str1.lower():
        if char in dict1:
            dict1[char] += 1
        else:
            dict1[char] = 1


    for char in str2.lower():
        if char in dict2:
            dict2[char] += 1
        else:
            dict2[char] = 1

    return dict1 == dict2

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if anagram(str1, str2):
    print("Anagram")
else:
    print("Not an anagram")
