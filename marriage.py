import sys

def AssemblePreferences(fileName):
    #Dictionary with knights as keys and list of Ladies as values
        #for every knight, set them to free (not married)
    KnightPrefs = {}
    LadyPrefs = {}
    lineCount = 0
    n = 0
    #Open the file and put the preferences in dictionaries
    with open(fileName) as f:
        for line in f:
            if(lineCount == 0): n = int(line)
            lineCount+=1
            line = line.strip()
            choices = line.split(" ")
            if(lineCount > 1 and lineCount <= n+1):
                #Make the knight the key
                current_knight = choices.pop(0)
                #Make his preference list of ladies the values
                KnightPrefs[current_knight] = choices
            elif (lineCount > n):
                #Make the knight the key
                current_lady = choices.pop(0)
                #Make his preference list of ladies the values
                LadyPrefs[current_lady] = choices

    print("Knights: ", KnightPrefs)
    print("Ladies: ", LadyPrefs)

    return KnightPrefs, LadyPrefs

def propose(kPrefs, lPrefs):
    for i in range(0, kPrefs[0].length()):
        print(i)


def main():
    kPrefs, lPrefs = AssemblePreferences(sys.argv[1])

main()