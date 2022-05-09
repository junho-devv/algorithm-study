from collections import Counter


def find_max(word):
    counter = Counter(word)
    print(counter)
    max_count = -1
    for letter in counter:
        if counter[letter] > max_count:
            max_count = counter[letter]
            max_letter = letter
    return max_letter, max_count


print(find_max('hello world'))
