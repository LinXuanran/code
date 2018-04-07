def decode(x, qq, char1, char2):
    i = 0
    while i < len(x)-1:
        temp = x[i] + x[i + 1]
        if temp in char2:
            qq = qq + str(char2[temp])
            i = i + 2
            continue
        temp = x[i]
        if temp in char1:
            qq = qq + str(char1[temp])
            i = i + 1
            continue
        i = i + 1
    return qq


if __name__=='__main__':
    qq="qq:"
    x = "NeSkoeCA"
    char1={'n': 0, '6': 1, '-': 2, 'o': 3, 'v': 4, '4': 5, 'C': 6, 'S': 7, 'c': 8, 'E': 9, 'z': 0, '5': 1, 'A': 2, 'i': 3, 'P': 4, 'k': 5, 's': 6, 'l': 7, 'F': 8, 'q': 9}
    char2={'oe': 0, 'oK': 1, 'ow': 2, 'oi': 3, '7e': 4, '7K': 5, '7w': 6, '7i': 7, 'Ne': 8, 'NK': 9, 'on': 0, 'oz': 3, '7v': 5, '7z': 7, 'Nn': 8, 'Nv': 9}
    qq=decode(x,qq,char1,char2)
    print(qq)

