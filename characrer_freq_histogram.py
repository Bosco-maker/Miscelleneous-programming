from os import strerror

try:
    src = open("sampleText.txt","rt")
    content = src.read()

    stat = {'a':0,
            'b':0,
            'c':0,
            'd':0,
            'e':0,
            'f':0,
            'g':0,
            'h':0,
            'i':0,
            'j':0,
            'k':0,
            'l':0,
            'm':0,
            'n':0,
            'o':0,
            'p':0,
            'q':0,
            'r':0,
            's':0,
            't':0,
            'u':0,
            'v':0,
            'w':0,
            'x':0,
            'y':0,
            'z':0,}
    for char in content:
        char = char.lower()
        stat[char] += 1
    
    ori = list(stat.values())[0]
    print(ori)
    for char,no in stat.items():
        print(char + " -> " + str(no))
    
except IOError as e:
    print("error found"   + strerror(e.errno))

