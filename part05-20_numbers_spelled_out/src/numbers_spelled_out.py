# Write your solution here
def dict_of_numbers():
    unit_dict = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six",7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen",14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen",18:"eighteen", 19:"nineteen"}
    tens_dict = {20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty",70:"seventy", 80:"eighty", 90:"ninety"}
    
    main_dict = {}

    for i in range(20):
        main_dict[i] = unit_dict[i]

    for i in range(20, 100):
        rem = i % 10
        if rem == 0:
            main_dict[i] = tens_dict[i]
        else:
            point = i - rem
            value = tens_dict[point] + "-" + unit_dict[rem]
            main_dict[i] = value
        
    return main_dict