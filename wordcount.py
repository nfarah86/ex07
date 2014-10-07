import string
import sys

def wordCount(fileName):
    #initialize dictionary
    wordCountDictionary = {}


    for line in fileName:
        justtext = line.strip()
        lowertext = justtext.lower() #makes lowercase
        #removes all punctuation by joining all chars that aren't punctuation
        nopunct = ''.join(char for char in lowertext if char not in string.punctuation)
        words = nopunct.split()
        #checks if word is in dictionary. If it isn't, adds to dictionary.
        for word in words:
            if word in wordCountDictionary:
                wordCountDictionary[word] += 1
            else:
                wordCountDictionary[word] = 1

    #checks which keys have the maximum wordcount, sorts those keys, prints, and decreases the max by 1
    maxvalue = max(wordCountDictionary.values())
    minvalue = min(wordCountDictionary.values())
    while maxvalue >= minvalue:
        keys = [x for x,y in wordCountDictionary.items() if y == maxvalue]
        keys.sort()
        for word in keys:
            print word, wordCountDictionary[word]
        maxvalue -= 1
    
def main():
    fileName = open(sys.argv[1])
    wordCount(fileName)



if __name__ == "__main__":
    main()













    #sortedValues= wordCountDictionary.items()
    #sortedValues = sorted(sortedValues, key=lambda x:x[1])
    #sortedValues.reverse()

    #print sortedValues


    #print wordCountDictionary














