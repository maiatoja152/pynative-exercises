from collections import Counter 


# Exercise 1
def list_comprehension_mastery(strings: list[str]) -> list[str]:
    return [s.upper() for s in strings if len(s) >= 4]

#words = ["apple", "bat", "cherry", "dog", "elderberry"]
#print(list_comprehension_mastery(words))

# Exercise 2
def dictionary_merge(dict1: dict, dict2: dict) -> dict:
    merged = dict1.copy()
    for key in dict2:
        if key in merged:
            merged[key] += dict2[key]
        else:
            merged[key] = dict2[key]
    return merged

#dict_a = {'a': 10, 'b': 20}
#dict_b = {'b': 5, 'c': 15}
#print(dictionary_merge(dict_a, dict_b))


# Exercise 3
def counter(string: str) -> Counter:
    return Counter([c.lower() for c in string if c.isalpha()])

#text = "Python Programming"
#print(counter(text))


# Exercise 4
def anagram_check(string1: str, string2: str) -> bool:
    return Counter(string1) == Counter(string2)

#word1 = "listen"
#word2 = "silent"
#print(anagram_check(word1, word2))


# Exercise 5
def flatten_list(lis: list) -> list:
    flattened = []
    for item in lis:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened

#nested = [1, [2, 3], [4, [5, 6]], 7]
#print(flatten_list(nested))


# Exercise 6
def reverse_words(string: str) -> str:
    return " ".join([s[::-1] for s in string.split(" ")])

#print(reverse_words("Python is awesome"))


# Exercise 7
def palindrome_sentence(sentence: str) -> bool:
    sentence = "".join(c.lower() for c in sentence if c.isalnum())
    return sentence == sentence[::-1]

#print(palindrome_sentence("A man, a plan, a canal: Panama"))


# Exercise 8
def list_comprehension_filtering(strings: list[str]) -> list[str]:
    return [s for s in strings if len(s) > 5 and s[0].lower() in "aeiou"]


#print(list_comprehension_filtering(
#    ["apple", "education", "ice", "ocean", "python", "umbrella"])
#)


# Exercise 9
def remove_duplicates(lis: list) -> list:
    items_seen = set()
    for i, item in enumerate(lis):
        if item in items_seen:
            del lis[i]
        else:
            items_seen.add(item)
    return lis

#print(remove_duplicates([1, 2, 2, 3, 1, 4, 2]))


# Exercise 10
from enum import Enum, auto

class Direction(Enum):
    RIGHT = auto()
    LEFT = auto()

def circular_shift(lis: list, shift: int, direction: Direction) -> list:
    shift %= len(lis)
    if direction == Direction.RIGHT:
        return lis[-shift:] + lis[:-shift]
    else:
        return lis[shift:] + lis[:shift]

#print(circular_shift([1, 2, 3, 4, 5], 2, Direction.RIGHT))
#print(circular_shift([1, 2, 3, 4, 5], 12, Direction.LEFT))


# Exercise 11
def dictionary_merge(d1: dict, d2: dict) -> dict:
    merged = d1
    for key in d2:
        if key in merged:
            merged[key] = [merged[key], d2[key]]
        else:
            merged[key] = d2[key]
    return merged

#print(dictionary_merge({"a": 1, "b": 2}, {"b": 3, "c": 4}))
