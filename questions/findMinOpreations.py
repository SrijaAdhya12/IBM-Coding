# You are given a string abb we need to find th number of opreations taken to convert the string into


def findMinOperations(s):
    pattern = "abc"
    i = 0
    pos = 0
    opreations = 0
    while i < len(s):
        alphabet = pattern[pos]
        if s[i] == alphabet:
            i += 1
            pos = (pos+1)%3
        else:
            opreations += 1
            pos = (pos+1)%3
    if pos != 0:
        remaining = 3 - pos
        opreations += remaining
    return opreations






if __name__ == "__main__":
    s = input().strip()
    print(findMinOperations(s))
