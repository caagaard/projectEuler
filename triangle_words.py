# Reads a text file w/ about 2000 words and checcks if they're "triangular" words

# A word is triangular if the sum of its characters is a triangular number after
# converting letters to numbers by: a->1, b->2, ... z->26
import string

def make_triangular_list():
    triangles = []
    for n in range(1,24):
        triangles.append(n*(n+1)/2)
    return(triangles)

def read_text():
    raw_words = string.lower(open('support_files/words.txt', 'r').read())
    word_list = string.split(raw_words, '","')
    word_list[0] = word_list[0][1:]
    word_list[-1] = word_list[-1][0:-2]
    return(word_list)

def wordToNum(word):
    char_sum = 0
    for letter in word:
        char_value = string.lowercase.index(letter) + 1
        char_sum = char_sum + char_value
    return(char_sum)

word_list = read_text()
tri_nums = make_triangular_list()
tri_words = []

for word in word_list:
    char_sum = wordToNum(word)
    if char_sum in tri_nums:
        tri_words.append(word)

print(len(tri_words))
