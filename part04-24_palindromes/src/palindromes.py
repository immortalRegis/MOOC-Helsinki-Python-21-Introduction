# Write your solution here
def main_method():
    while True:
        word = input("Please type in a palindrome: ")
   
        is_palindrome = palindromes(word)
        if is_palindrome:
            break

def palindromes(word: str):
    front_index  = 0
    back_index = -1

    palindrome = True

    while front_index < len(word):
        if word[front_index] != word[back_index]:
            palindrome = False
            break
        front_index += 1
        back_index -= 1

    if palindrome:
        print(f"{word} is a palindrome!")
    else:
        print("that wasn't a palindrome")
    return palindrome



main_method()



    
