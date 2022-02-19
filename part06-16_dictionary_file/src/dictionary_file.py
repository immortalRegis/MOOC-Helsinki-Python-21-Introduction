# Write your solution here
word_list = []

while True:
    with open("dictionary.txt") as new_file:
        for row in new_file:
            row = row.strip()
            word_list.append(row)

    print("1 - Add word, 2 - Search, 3 - Quit")
    response = int(input("Function:"))

    if response == 3:
        break

    if response == 2:
        search_term = input("Search term: ")
        for word_pair in word_list:
            word_pair = word_pair.strip()
            split_pair = word_pair.split("-")
            if search_term in split_pair[0] or search_term in split_pair[1]:
                print(f"{split_pair[0]} - {split_pair[1]}")
    
    elif response == 1:
        finnish = input("The word in Finnish: ")
        english = input("The word in English: ")
        word_pair = f"{finnish}-{english}"
        if word_pair not in word_list:
            with open("dictionary.txt","a") as stored_words:
                stored_words.write(word_pair + "\n")
            print("Dictionary entry added")

   
print("Bye!")
