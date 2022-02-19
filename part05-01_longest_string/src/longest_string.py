# Write your solution here
def longest(strings: list):
    longest = ""
    for string in strings:
        if len(string) > len(longest):
            longest = string
    return longest