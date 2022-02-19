# Write your solution here
def recipe_search(filename:str):
    recipe_list = []
    
    with open(filename) as new_file:
        single_recipe = []
        for line in new_file:
            line = line.strip()
            if len(line) == 0:
                recipe_list.append(single_recipe)
                single_recipe = []
                continue
            single_recipe.append(line)
        recipe_list.append(single_recipe)
    return recipe_list

def search_by_name(filename: str, word: str): 
    recipe_list = recipe_search(filename)
    found_list = []
    for recipe in recipe_list:
        name = recipe[0]
        if word.lower() in name.lower():
            found_list.append(name)
    return found_list

def search_by_time(filename: str, prep_time: int):
    recipe_list = recipe_search(filename)
    found_list = []
    for recipe in recipe_list:
        time = int(recipe[1])
        if time < prep_time:
            value = f"{recipe[0]}, preparation time {recipe[1]} min"
            found_list.append(value)
    return found_list

def search_by_ingredient(filename: str, ingredient: str):
    recipe_list = recipe_search(filename)
    found_list = []
    for recipe in recipe_list:
        if ingredient in recipe[2:]:
            value = f"{recipe[0]}, preparation time {recipe[1]} min"
            found_list.append(value)
    return found_list
    

if __name__ == "__main__":
    print(search_by_time("recipes1.txt", 20))
