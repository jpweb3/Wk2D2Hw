
# 1) Using the given list, print out a filtered version of the list with only the numbers that are less than ten

alist = [1,11,14,5,8,9]

for i in alist:
    if i < 10:
        print(i)


# 2) Merge and sort the two lists below
#Hint: You can use the .sort() method

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

#for i in l_1:
#    l_2.append().sort()
#   print(l_2)

l_3 = l_1 + l_2

(l_3.sort())
print(l_3)


# 3) Square every number from 1 to 15

for i in range(15):
    i= i**2
    print(i)

# 4) Using List Comprehension and the given list, print out a filtered list with only the names that start with the letter 'a'. The names in the outputted list should be title cased and have no whitespace.

#Hint: There is an empty string at the end of the list you will need to account for.

filtered_names = [
    name.strip().title()  # Strip whitespace and title case each name
    for name in names_list  # Iterate through each name in the list
    if name.strip().title().startswith('A')  # Filter names that start with 'A'
]
print(filtered_names)

