# Write your solution here
def who_won(game_board: list):
    one_count = 0
    two_count = 0

    for row in game_board:
        for cell in row:
            if cell == 1:
                one_count += 1
            elif cell == 2:
                two_count += 1
            else:
                continue
    
    if one_count > two_count:
        return 1
    elif two_count > one_count:
        return 2
    else:
        return 0