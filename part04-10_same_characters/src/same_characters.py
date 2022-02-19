# Write your solution here
def same_chars(word, index1, index2):
    if index1 < 0 or index1 >=len(word):
        return False
    if index2 < 0 or index2 >= len(word):
        return False
    if word[index1] != word[index2]:
        return False
    return True
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))