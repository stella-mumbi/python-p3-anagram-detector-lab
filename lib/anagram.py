# This is a **test-driven lab**. Run `pipenv install` to create your virtual
# environment and `pipenv shell` to enter the virtual environment. Then run
# `pytest -x` to run your tests. Use these instructions and `pytest`'s error
# messages to complete your work in the `lib/` folder.

# You will write a program that, given a word and a list of possible
# [anagrams][anagrams], selects the correct one(s).

# Your class, `Anagram` should take a word on initialization; instances should
# respond to a `match()` instance method that takes a list of possible anagrams.
# It should return all matches in a list. If no matches exist, it should return
# an empty list.

# In other words, given: `'listen'` and `['enlists', 'google', 'inlets',
# 'banana']` the program should return `['inlets']`.

# ```py
# listen = Anagram("listen")
# listen.match(['enlists', 'google', 'inlets', 'banana'])
# # => ['inlets']
# ```
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, possible_anagrams):
        return [anagram for anagram in possible_anagrams if self.is_anagram(anagram)]

    def is_anagram(self, candidate):
        candidate_lower = candidate.lower()
        return sorted(candidate_lower) == sorted(self.word) and candidate_lower != self.word

# Example Usage:
word_to_check = "listen"
possible_anagrams = ["enlist", "silent", "bother", "banana", "inlets"]

anagram_checker = Anagram(word_to_check)
matches = anagram_checker.match(possible_anagrams)

print(f"Anagrams of '{word_to_check}': {matches}")

     
 