'''Problem 1:
A pangram is a sentence using every letter of the alphabet at least once. It is case insensitive, 
so it doesn't matter if a letter is lower-case (e.g. k) or upper-case (e.g. K).
For this exercise, a sentence is a pangram if it contains each of the 26 letters in the English alphabet.
Example: The quick brown fox jumps over the lazy dog.
Your task is to figure out if a sentence is a pangram.'''

sentence = "The quick brown fox jumps over the lazy dog"

sentence_split = list(sentence.split())

print(sentence_split)