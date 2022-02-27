import re
import os
import sys


def read(regex, idkAr, notIn):
    with open("words.txt",) as f:
        lines = f.readlines()

        fivers = []
        for line in lines:
            if len(line) == len(regex)+1:  # this is 5
                fivers.append(line.lower())

        str = ""
        newlines = str.join(fivers)
        x = re.findall(regex, newlines)
        almost = []
        for word in x:
            found = 0
            for letter in idkAr:
                if letter in word:
                    found += 1
            if found == len(idkAr):
                almost.append(word)

        for word in almost:
            for letter in notIn:
                if letter in word:
                    print("Removing: ", word, "it contains", letter)
                    almost.remove(word)
                    break



        print("Pattern '" + regex + "' and must also contain the letters'" + ",".join(idkAr) + "' found these words: ")
        print(almost)


if __name__ == '__main__':
    regex = input("Enter letters you know  i.e. .o..t\n")
    dontknows = input("Enter letters that can be anywhere i.e. a,s\n")
    notIn = input("Enter letters that aren't in the word\n")
    read(regex, dontknows.split(","), notIn.split(","))
