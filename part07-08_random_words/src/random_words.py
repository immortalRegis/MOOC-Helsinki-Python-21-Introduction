# Write your solution here
from random import choice, sample

def words(n: int, beginning: str):
    found_list = []
    with open("words.txt") as stored_words:
        for word in stored_words:
            word = word.strip()
            if word.startswith(beginning) and word not in found_list:
                found_list.append(word)
    

        if len(found_list) < n:
            raise ValueError
        
        return sample(found_list,n)

if __name__ == "__main__":
    print(words(5, "ca"))
    
        

