# Write your solution here
from random import choice

def roll(die: str):
    values = ""
    if die == "A":
        values = "333336"
    if die == "B":
        values = "222555"
    if die == "C":
        values = "144444"
    return int(choice(values))

def play(die1: str, die2: str, times: int):
    d1_wins = 0
    d2_wins = 0
    draws = 0

    for i in range(times):
        d1_value = roll(die1)
        d2_value = roll(die2)
        if d1_value > d2_value:
            d1_wins += 1
        elif d2_value > d1_value:
            d2_wins += 1
        else:
            draws += 1
    
    return (d1_wins, d2_wins, draws)

if __name__ == "__main__":
    
    
    for i in range(20):
        print(roll(A)," ", end="")
    print()
    print(play(A, B, 1000))