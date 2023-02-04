# Write a function to compute the `factorial` of a number.
# Given a whole number n, a factorial is the product of all
# whole numbers from 1 to n.
# 5! = 5 * 4 * 3 * 2 * 1
#
# Example function call
#
# factorial(5)
#
# > 120

def factorial(num):
    holder = num
    # print(holder)
    for n in range(1, num):
        # print(n)
        holder *= n
        # print(holder)
    print(holder)
        
        
        
    

factorial(5)
#
