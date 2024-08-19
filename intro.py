sum = 645630 // 322

var_bool = False # or False
var_float = 25.7 - 0.1
var_string = "a" # "wasd"
var_list = [1,2,4] # [True, var_float, False]
var_tuple = (1, 4)
var_dictionary = { "paul": 5}

if (var_bool == True):
    print("var_bool is True")
else:
    print("var_bool is False")

for element in var_list:
    print("This is the element: ", element)

# Explicit casting helps us to transform the datatype of a variable

print("Hello World!" + str(sum))