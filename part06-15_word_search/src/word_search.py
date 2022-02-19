# Write your solution here
def find_words(search_term: str):
    word_list = []
    search_term = search_term.lower()
    with open("words.txt") as dictionary:
        for word in dictionary:
            word = word.strip()
            if "." not in search_term and "*" not in search_term:
                if search_term == word.lower():
                    word_list.append(word)
            elif "*" in search_term:
                if search_term[0] == "*":
                    if word.endswith(search_term[1:]):
                        word_list.append(word)
                else:
                    if word.startswith(search_term[0:(len(search_term)-1)]):
                        word_list.append(word)
            elif "." in search_term:
                same = True
                if len(search_term) == len(word):
                    for i in range(len(search_term)):
                        if search_term[i] != "." and (search_term[i] != word[i]):
                            same = False
                            break
                    if same:
                        word_list.append(word)
    return word_list
