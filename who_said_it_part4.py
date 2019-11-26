'''
Who said it? Part 4: This program gets the input from the user and returns
if the word or phrase is written by William Shakespeare or Jane Austen in the
whole text.

Miki Ando
'''

import math

# Takes a word and returns the same word with all non-letters removed 
# and converted to lowercase
def normalize(word):
    word =  "".join(letter for letter in word if letter.isalpha()).lower()
    return (word)

# Takes a filename and generates a dictionary. Keys: words. Values: counts for
# each word(key).
def getcounts(filename):
    
    #make an empty dictionary and open the file
    result_dict = {}
    file = open(filename)
    counts = 0

    # for every line in the file, removes the /n and splits each word
    for line in file:
        line = line.strip()
        words = line.split()

        # for every split word, it normalizes by the function
        for word in words:
            word = normalize(word)

            # if the word is already in the dictionary, adds onto the count
            if word in result_dict:
                result_dict[word] += 1 
                
            # if the word is not in the dictionary yet, adds the word as a key
            else:
                result_dict[word] = 1

            counts += 1

    result_dict["_total"] = counts
    return (result_dict)

# Takes a word and a dictionary of word counts, then generates a score that
# approximates the relevance of the word in the document (function was given)
def get_score(word,counts):
    denominator = float(1 + counts["_total"])
    if word in counts:
        return math.log((1 + counts[word]) / denominator)
    else:
        return math.log(1 / denominator)

# Using the get_score function, it compares the score for each word that the
# user input and outputs which text the word or phrase comes from. 
def predict():
    shakespeare_counts = getcounts("hamlet-1.txt")
    austen_counts = getcounts("pride-and-prejudice-1.txt")
    shakespeare_total_score = 0
    austen_total_score = 0

    uword = user_input.strip()
    nword = uword.split()

    #calculate the scores for each word that the user input
    for word in nword:
        word = normalize(word)

        shakespeare_score = get_score(word, shakespeare_counts)
        shakespeare_total_score += shakespeare_score
        
        austen_score = get_score(word, austen_counts)
        austen_total_score += austen_score

    # checks which text the word has more relevance 
    if shakespeare_total_score > austen_total_score:
        print("I think that was written by William Shakespeare.")
    if shakespeare_total_score < austen_total_score:
        print("I think that was written by Jane Austen.")

# gets the input from the user    
user_input = input("Enter Word/Phrase: ")

#runs the function 
predict()
