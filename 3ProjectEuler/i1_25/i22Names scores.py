# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

def getData(path):
    with open(path) as text_file:
        contents = text_file.read()
        mylist = [line for line in contents.split(',')]
        mylist.sort()
        thesum = 0
        for idex, val in enumerate(mylist):
            print(val)
            val = val.replace('"','')
            print(idex,'#',ciculatevalue(val))
            thesum += (idex + 1) * ciculatevalue(val)
        print('sum = ',thesum)



def ciculatevalue(i):
    isum = 0
    for ch in i:
        code = ord(ch) - ord('A') + 1
        isum += code
    return isum
if __name__ == "__main__":
    getData("i22names.txt")