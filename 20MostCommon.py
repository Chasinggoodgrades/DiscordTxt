
"""
The purpose of this program is to read through discord chat logs produced by
DISCORDCHATEXPORTER and then output/format a csv file or text file of users
20 most commonly used words.
"""

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import csv

## Editable Variables
## userdataname = "#####"            ## Edit These
## specific_word = "###"             ## Edit These
the_chat = "#####.txt"               ## Edit These


file = open(the_chat, "r", encoding="utf-8")
file2 = open(the_chat, "r", encoding="utf-8")

def theListofNames():
    listOfNames = []
    for i in file.readlines():
        if i.__contains__("#"):
            listOfNames.append(i[21:i.index("#")].strip())
    for i in listOfNames:
        if i.startswith(" ") or i.__contains__(" "):
            listOfNames.remove(i)
    for i in listOfNames:
        if len(i) > 15:
            listOfNames.remove(i)
    for i in listOfNames:
        if i.__contains__("1") or i.__contains__("2"):
            listOfNames.remove(i)
    for i in listOfNames:
        if not i.isalpha():
            listOfNames.remove(i)
    for i in listOfNames:
        if listOfNames.count(i) > 1:
            listOfNames.remove(i)
    for i in listOfNames:
        if not i.isascii():
            listOfNames.remove(i)
    listOfNames = list(dict.fromkeys(listOfNames))
    return listOfNames

def theMain(listOfNames):
    for j in listOfNames:
        ##specific_word_count = 0 ## Uncomment if you want to see individual counts
        text = ""
        me = False
        file2 = open(the_chat, "r", encoding="utf-8")
        for i in file2.readlines():
            #if i.__contains__(specific_word):
                 #specific_word_count += 1
            if me == True:
                text += i
            if i.__contains__(j):
                me = True
            else:
                me = False

        lowercasetext = text.lower()
        tokenizedlist = word_tokenize(lowercasetext)
        freqDist = nltk.FreqDist(tokenizedlist)
        ##print("Total " + specific_word + " count: " + str(specific_word_count))

        ## If person has less than 20 characters/words.. They're not included ##
        if len(tokenizedlist) > 20:

            """ Debugging """
            # print(j)
            # print(freqDist.most_common(20))
            # print("\n")
            # print(listOfNames)

            """ Export to csv file """
            # try:
            #     with open('output.csv', 'a', newline='') as file:
            #         writer = csv.writer(file)
            #         writer.writerow([j, freqDist.most_common(20)[0], freqDist.most_common(20)[1], freqDist.most_common(20)[2], freqDist.most_common(20)[3], freqDist.most_common(20)[4], freqDist.most_common(20)[5], freqDist.most_common(20)[6], freqDist.most_common(20)[7], freqDist.most_common(20)[8], freqDist.most_common(20)[9], freqDist.most_common(20)[10], freqDist.most_common(20)[11], freqDist.most_common(20)[12], freqDist.most_common(20)[13], freqDist.most_common(20)[14], freqDist.most_common(20)[15], freqDist.most_common(20)[16], freqDist.most_common(20)[17], freqDist.most_common(20)[18], freqDist.most_common(20)[19]])
            #         file.close()
            # except Exception as e:
            #     print(e)
            #     print("Error writing to csv file")

            """ Export to txt file """
            file3 = open("output.txt", "a", encoding="utf-8")
            file3.write(j + "\n")
            file3.write(str(freqDist.most_common(20)) + "\n")
            file3.write("\n")
            file3.close()

theMain(theListofNames())
