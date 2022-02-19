# Write your solution here
def store_personal_data(person: tuple):
    personal_data = f"{person[0]};{person[1]};{person[2]}"
    with open("people.csv", "a") as entries:
        entries.write(personal_data)
