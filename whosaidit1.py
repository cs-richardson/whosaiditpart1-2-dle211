"""
This program prints every word and the amount of times they appear in a short
version of Hamlet and Pride and Prejudice.
Foundation provided by Ms. Richardson
Edits done by Justin
Help provided by W3Schools
"""

# normalize
# -----
# This function takes a word and returns the same word
# with:
#   - All non-letters removed
#   - All letters converted to lowercase
def normalize(word):
    return "".join(letter for letter in word if letter.isalpha()).lower()

# getCounts
# -----
# This function takes a filename and generates a dictionary
# whose keys are the unique words in the file and whose
# values are the counts for those words.
def getCounts(filename):
    text = open(filename, "r")
    text = text.read()
    text = text.split()
    for i in range(len(text) - 1):
        text[i] = normalize(text[i])

    result_dict = {"_total": 0}
    for currentElement in text:
        if currentElement not in result_dict:
            result_dict[currentElement] = 1
        elif currentElement in result_dict:
            result_dict[currentElement] += 1
        result_dict["_total"] += 1
    return result_dict

# Get the counts for the two shortened versions
# of the texts
shakespeareCounts = getCounts("hamlet-short.txt")
austenCounts = getCounts("pride-and-prejudice-short.txt")
del austenCounts[""]
austenCounts["_total"] -= 1

# Check the contents of the dictionaries
for key in shakespeareCounts:
    print(key + ": " + str(shakespeareCounts[key]))
print("-----")
for key in austenCounts:
    print(key + ": " + str(austenCounts[key]))
