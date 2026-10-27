'''
for this exercise, we want to count the items in a list without using len()
we will start the count at 0 and increment the count by 1 for each item in the list.
we will return the final count after iterating through the entire list.
then, we make use of newline
'''

def count_items(list):
    count = 0

    for item in list:
        count += 1
        return "Item: " + str(item) + " Count: " + str(count) + "\n"
    
    return "\n Total Count: " + str(count)
    
print(count_items(["Ade", "Bolu", "Chidi", "Fatima", "Emeka"]))