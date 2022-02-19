# Write your solution here
def oldest_person(people: list):
    oldest_age = people[0][1]
    oldest_person = people[0][0]
    
    for person in people:
        if person[1] < oldest_age:
            oldest_person = person[0]
            oldest_age = person[1]
        
    
    return oldest_person


