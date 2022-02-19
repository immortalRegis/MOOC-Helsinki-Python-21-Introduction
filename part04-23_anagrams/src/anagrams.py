# Write your solution here
def anagrams(word1, word2):
    word1_as_list = []
    word2_as_list = []

    for letters in word1:
        word1_as_list.append(letters)

    for letters in word2:
        word2_as_list.append(letters)

    return sorted(word1_as_list) == sorted(word2_as_list)

    

if __name__ == "__main__":
    print(anagrams("fish", "shif"))
