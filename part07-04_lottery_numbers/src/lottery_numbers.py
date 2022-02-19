# Write your solution here
import random
def  lottery_numbers(amount: int, lower: int, upper: int):
    numbers_list = list(range(lower, upper + 1))
    lot_nums = random.sample(numbers_list, amount) 
    return sorted(lot_nums)