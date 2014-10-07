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

    #print wordCountDictionary
    return wordCountDictionary

def invertDictionary(wordCountDictionary):  #calling wordCountDictionary so it can be passed in to this func.
    #we can switch the keys and values of the old dictionary (wordCountDictonary) and append those
    #new values to inverseDict (because we can't switch keys and values in place)

    inverseDict = {}  #new dictionary
        

    for old_key in wordCountDictionary:   #old_key just refers to the place holder for key in wordCountDictionary
        new_key = wordCountDictionary[old_key]  # value of wordCountDictionary[key] is being passed as new_key
        if new_key not in inverseDict:   
            inverseDict[new_key] = [old_key]  #if new_key is not in inverseDict, it'll add it with its valu; key:value
                                                #[old_key] is set to a list, otherwise it returns a string
        else:
            inverseDict[new_key].append(old_key)   
    #print inverseDict

    for key in inverseDict:
        inverseDict[key] = sorted(inverseDict[key])
    #print inverseDict
    return inverseDict

def printDict(inverseDict):
    listOfKeys = sorted(inverseDict.keys())  #list of keys in numerical order
    listOfKeys.reverse()
    for key in listOfKeys:
        #print key, inverseDict[key]
        for item in inverseDict[key]:
            print item, key




def main():
    fileName = open(sys.argv[1])
    dictionary = wordCount(fileName)
    invDictionary = invertDictionary(dictionary)
    printDict(invDictionary)


if __name__ == "__main__":
    main()

