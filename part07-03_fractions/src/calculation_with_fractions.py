# Write your solution here
import fractions
def fractionate(num:int):
    fraction_list = []
    for i in range(num):
        fraction_list.append(fractions.Fraction(1, num))
    return fraction_list