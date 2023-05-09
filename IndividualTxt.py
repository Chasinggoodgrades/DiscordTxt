"""
The purpose of this program is to read through discord chat logs produced by
DISCORDCHATEXPORTER and then output/format a text file
of everything the user has said in the chat. Each user will have their own text file.
IE: Aches.txt
"""

## Editable Variables
## name = "##########"
chat = "##########.txt"

file = open(chat, "r", encoding="utf-8")
file2 = open(chat, "r", encoding="utf-8")

def listNames():
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

def main(listOfNames):
    for j in listOfNames:
        ##specific_word_count = 0 ## Uncomment if you want to see individual counts
        text = ""
        me = False
        file2 = open(chat, "r", encoding="utf-8")
        for i in file2.readlines():
            if me == True:
                text += i
            if i.__contains__(j):
                me = True
            else:
                me = False

        print(text)

        """ Export to txt file """
        file3 = open(j+".txt", "a", encoding="utf-8")
        file3.write(j + "\n")
        file3.write(text)
        file3.write("\n")
        file3.close()

main(listNames())
