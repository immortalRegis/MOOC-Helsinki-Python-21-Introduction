# Write your solution here
# I intend to use a for loop with a counter variable to solve this problem
from string import ascii_uppercase

def run(instructions: list):
    initial_state = {}
    results = []
    
    for letter in ascii_uppercase: #initialize all the letters to 0
        initial_state[letter] = 0

    i = 0
    #use a while loop to execute every command passed in as an argument.
    # I used a lot of casting because the MOV, ADD, SUB and MUL commands accept
    # both integer and string values e.g "MOV A B", "MUL B 5" etc
    while True:
        if i == len(instructions):
            break
        row = instructions[i]
        contents_of_row = row.split()
        command = contents_of_row[0]
        if command == "END":
            break
        elif command == "IF":
            if not contents_of_row[1].isdigit():
                var1 = initial_state[contents_of_row[1]]
            else:
                var1 = int(contents_of_row[1])
            
            if not contents_of_row[3].isdigit():
                var2 = initial_state[contents_of_row[3]]
            else:
                var2 = int(contents_of_row[3])
            
            con = contents_of_row[2]
        
            if con == ">":
                condition = var1 > var2
            elif con == ">=":
                condition = var1 >= var2
            elif con == "==":
                condition = var1 == var2
            elif con == "<":
                condition = var1 < var2
            elif con == "<=":
                condition = var1 <= var2
            else:
                condition = var1 != var2

            if condition: # This conditional acts as a loop
                jump_location = contents_of_row[5]
                jump_location = f"{jump_location}:"
                i = instructions.index(jump_location) 
                continue
        elif command == "PRINT":
            if contents_of_row[1] in initial_state:
                results.append(int(initial_state[(contents_of_row[1])]))
            else:
                results.append(int(contents_of_row[1]))
        elif command == "JUMP":
            location = f"{contents_of_row[1]}:"
            new_location = instructions.index(location)
            i = new_location
        elif command == "MOV":
            if contents_of_row[2].isdigit():
                initial_state[contents_of_row[1]] = int(contents_of_row[2])
            else:
                initial_state[contents_of_row[1]] = int(initial_state[contents_of_row[2]])
            
        elif command == "ADD":
            value = int(initial_state[contents_of_row[1]])
            if contents_of_row[2].isdigit():
                value += int(contents_of_row[2])
            else:
                value += int(initial_state[contents_of_row[2]])
            initial_state[contents_of_row[1]] = value
        elif command == "SUB":
            value = int(initial_state[contents_of_row[1]])
            if contents_of_row[2].isdigit():
                value -= int(contents_of_row[2])
            else:
                value -= int(initial_state[contents_of_row[2]])
            initial_state[contents_of_row[1]] = value
        elif command == "MUL":
            value = int(initial_state[contents_of_row[1]])
            if contents_of_row[2].isdigit():
                value *= int(contents_of_row[2])
            else:
                value *= int(initial_state[contents_of_row[2]])
            initial_state[contents_of_row[1]] = value
        i += 1

        
        
    return results
            
if __name__ == "__main__":
    program1 = ['MOV N 100', 'PRINT 2', 'MOV A 3', 'start:', 'MOV B 2', 'MOV Z 0', 'test:', 'MOV C B', 'new:', 'IF C == A JUMP virhe', 'IF C > A JUMP pass_by', 'ADD C B', 'JUMP new', 'virhe:', 'MOV Z 1', 'JUMP pass_by2', 'pass_by:', 'ADD B 1', 'IF B < A JUMP test', 'pass_by2:', 'IF Z == 1 JUMP pass_by3', 'PRINT A', 'pass_by3:', 'ADD A 1', 'IF A <= N JUMP start']
    result = run(program1)
    print(result)
