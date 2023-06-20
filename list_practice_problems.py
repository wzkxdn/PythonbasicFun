import random


nums = []
for i in range(20):
    rand_num = random.randint(1, 10)
    nums.append(rand_num)
print(nums)


for num in nums:
    print(num, end=" ")
print()


nums.sort() # inplace sort
print(nums)

print("min:", nums[0], "max:", nums[-1])
print("min:", min(nums), "max:", max(nums))


user_input = int(input("Enter a number to count: "))
print("Count:", nums.count(user_input))

count = 0
for num in nums:
    if num == user_input:
        count += 1
print("Count:", count)

user_input = int(input("Enter a number to remove all occurences of: "))
if user_input in nums:
    while user_input in nums:
        nums.remove(user_input)
else:
    print("Sorry, your number is not here!")
print(nums)



table = []
for i in range(10):
    # build a row
    row = []
    for j in range(5):
        # generate a random number
        rand_num = random.randrange(1, 11)
        row.append(rand_num)
    table.append(row)
print(table)

# Prints the numbers in a nice grid format (like a table)
for row in table:
    # row is a 1D list of numbers
    for num in row:
        print(num, end="\t")
    print()

curr_min = curr_max = table[0][0]
for row in table:
    for value in row:
        if value < curr_min:
            # we have a new min
            curr_min = value
        if value > curr_max:
            # we have a new max
            curr_max = value
print("min:", curr_min, "max:", curr_max)

# Determines the number of times a user-specified number is in the list
user_input = int(input("Enter a number to count: "))
count = 0
for row in table:
    for num in row:
        if num == user_input:
            count += 1
print("Count:", count)

user_input = int(input("Enter a number to remove all occurences of: "))
removed = False
for row in table:
    while user_input in row:
        row.remove(user_input)
        removed = True
if not removed:
    print("Sorry, your number is not here!")
print(table)


list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1, list2)
list1[0] = 100
print(list1, list2)
list3 = list1 # not a copy!!! list3 is an "alias" for list1
print(list1, list2, list3)
list3[0] = 200
print(list1, list2, list3)

def add_one_to_each_element(some_list):
    # some_list is an alias to the same list list3 refers to
    for i in range(len(some_list)):
        some_list[i] += 1

add_one_to_each_element(list3)
print(list1, list2, list3)
