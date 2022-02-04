import re


def read(regex, idkAr):
    with open("words.txt",) as f:
        lines = f.readlines()

        fivers = []
        for line in lines:
            if len(line) == len(regex)+1:  # this is 5
                fivers.append(line.lower())

        str = ""
        newlines = str.join(fivers)
        x = re.findall(regex, newlines)
        final = []
        for word in x:
            found = 0
            for letter in idkAr:
                if letter in word:
                    found += 1
            if found == len(idkAr):
                final.append(word)

        print("Pattern '" + regex + "' and must also contain the letters'" + ",".join(idkAr) + "' found these words: ")
        print(final)


if __name__ == '__main__':
    regex = input("Enter letters you know  i.e. .o..t\n")
    dontknows = input("Enter letters that can be anywhere i.e. a,s\n")
    read(regex, dontknows.split(","))
