# COMMENTS
# this is a one line comment

# GETTING INPUT FROM THE USER
print("Enter a number: ")
num = input() # num is a variable
# what type is num?
print(type(num))
print("The number doubled is: ",2 * num)

# we need to convert num from a string
# to a integer
num_int = int (num)
print("The number doubled is: ",2 * num_int)

# CONDITONALS
# if some condition is true
# then excute some code
x = 7
if x == 5:
    print("x is 5")
elif x == 7:
    print("x is 7")
else:
    print("x is not 5 and x is not 7")

# LOOPS
for i in range(2, 42, 2):
    print(i, end="")
print()

i = 2
while i < 40 :
    print(i,end="")
    i +=2 # progress

# FUNCTIONS
def say_hello():
    print("hello")
say_hello()
    

for i in range(10):
    say_hello()


#LIST

list_ints = [10, 4, -2, 9]
print(list_ints)
print(list_ints[1],list_ints[-3])

list_ints[0] = 4000
print(list_ints)

list_ints[-1] = "hello"
print(list_ints)

print(len(list_ints))

list_ints.append(42)
print(len(list_ints))

empty_list = []
print(len(empty_list))

nested_list = [[0,1],[2,3],[],[8]]
print(nested_list)
print(nested_list[1])
print(nested_list[1] [1])

cities = ["hangzhou","beijing","shanghai"]
for city in cities:
    print(city)


i = 0
while i < len(cities):
    print("i:",i,"cities[i]",cities[i])
    i += 1


repeated_list = 3*["guangdong","chongqing"]
print(repeated_list)


print(cities[:2])
print(cities[2:])

cities_copy = cities[:]
print("copy:",cities_copy)
cities_copy[0] = "HANGZHOU"

cities.append("new york city")
print(cities)

cities.remove("shanghai")
print(cities)

cities.pop(-1)
print(cities)

string_list = ["new","york","city"]
one_string = "".join(string_list)
print(one_string)

comma_separated_values_string = "new,york,city"
s12 = comma_separated_values_string.split(",")
print(s12)


#FILES
import math
filename = "data.csv"
infile = open(filename,"r")
reader = csv.reader(infile)
table = []
for row in reader:
    print(row)
    table.append(row)
infile.close()
print("after closing file table:")
print(table)































