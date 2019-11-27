"""
This program prints specific words and the amount of times they appear in the
full version of Hamlet and Pride and Prejudice.
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

# get_counts
# -----
# This function takes a filename and generates a dictionary
# whose keys are the unique words in the file and whose
# values are the counts for those words.
def get_counts(filename):
    text = open(filename, "r")
    text = text.read()
    text = text.split()
    for i in range(len(text)-1):
        text[i] = normalize(text[i])

    result_dict = {
        "heart": 0,
        "thou": 0,
        "king": 0,
        "happiness": 0,
        "dance": 0
        }
    for currentElement in text:
        if currentElement in result_dict:
            result_dict[currentElement] += 1
    if filename == "hamlet.txt":
        result_dict.pop("happiness")
        result_dict.pop("dance")
    elif filename == "pride-and-prejudice.txt":
        result_dict.pop("thou")
        result_dict.pop("king")
    return result_dict

# Get the counts for the two shortened versions
# of the texts
shakespeare_counts = get_counts("hamlet.txt")
austen_counts = get_counts("pride-and-prejudice.txt")
del austenCounts[""]
austenCounts["_total"] -= 1

# Check the contents of the dictionaries
for key in shakespeare_counts:
    print(key + ": " + str(shakespeare_counts[key]))
print("-----")
for key in austen_counts:
    print(key + ": " + str(austen_counts[key]))