# write your solution here
def check_spelling():
    wordlist = []
    with open("wordlist.txt") as new_file:
        for line in new_file:
            line = line.strip()
            wordlist.append(line)
    
    sentence = input("Write text: ")
    words_in_sentence = sentence.split(" ")
    for i in range(len(words_in_sentence)):
        word = words_in_sentence[i]
        word = word.lower()
        if not word in wordlist:
            highlight_word = f"*{words_in_sentence[i]}*"
            words_in_sentence[i] = highlight_word

    print(" ".join(words_in_sentence))

def main():
    check_spelling()
main()
