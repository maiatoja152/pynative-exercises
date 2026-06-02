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