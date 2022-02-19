# Write your solution here
import difflib

wordlist = []
with open("wordlist.txt") as new_file:
    for line in new_file:
        line = line.strip()
        wordlist.append(line)

sentence = input("Write text: ")
words_in_sentence = sentence.split(" ")
wrongly_spelt_words = []

for i in range(len(words_in_sentence)):
    word = words_in_sentence[i]
    word = word.lower()
    if not word in wordlist:
        wrongly_spelt_words.append(word)
        highlight_word = f"*{words_in_sentence[i]}*"
        words_in_sentence[i] = highlight_word

print(" ".join(words_in_sentence))

if len(wrongly_spelt_words) > 0:
    print("suggestions:")
    for wrong_word in wrongly_spelt_words:
        possible_words = difflib.get_close_matches(wrong_word, wordlist)
        possible_words_together = ", ".join(possible_words)
        print(f"{wrong_word}: {possible_words_together}")
    
