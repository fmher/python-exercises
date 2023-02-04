# Write a function called `multiply_by` that takes a list and
# a number, and returns the list of numbers multiplied by that number.
#
# You'll want to apply your fundamental programming knowledge here.
# What are the pieces to this problem? You'll need to define a function,
# need a return statement, need a for loop to iterate over the array.
#
# Example function call:
#
# multiply_by([1, 2, 3], 5)
#
# > [5, 10, 15]

def multiply_by(li, num): return ([current_number * num for current_number in li])        # one liner

    # new_list = []
    # for i, nums in enumerate(li):
    #     print(i)
    #     num *= nums
    #     new_list.append(num)
    #     # print(num)
    # print(new_list)

    # for i, nums in enumerate(li):
    #     li[i] = li[i] * num
    # print(li)

    # for i in range(len(li)):
    #     li[i] *= num
    # print(li)

    # list comprehension rturns a new list
    # [return expression for variable in iterable (if expression)]


    

multiply_by([1,2,3], 5)
print(multiply_by([1,2,3], 5))
