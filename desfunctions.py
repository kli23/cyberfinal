ip = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44,
    36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14,
    6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41,
    33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31,
    23, 15, 7]

# M = "0000000100100011010001010110011110001001101010111100110111101111"


def initialperm(text):
    newtext = ""
    for x in range(len(ip)):
        newtext += text[ip[x] - 1]
    return newtext


#print(len(ip))
#print(initialperm(M))
