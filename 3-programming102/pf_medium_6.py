# 6. Long-long Vowels
# Given a word as a string, print the result of extending any long vowels to the length of 5.

word = list(input("Give a word with a long vowel sound!\n"))
vowels = ["A", "E", "I", "O", "U"]
count = 0

for i in range(0, len(word)):
    l = word[i]
    for v in vowels:
        if l.upper() == v and l == word[i - 1]:
            word[i] = 4 * l

word_final = "".join(word)
print(word_final)