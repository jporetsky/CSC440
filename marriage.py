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
            ####### INITIALIZE IMPORTANT VAR's  #######
            lineCount+=1 # tracks line number.
            line = line.strip() #removes newline char from each line
            choices = line.split(" ") #Makes an array with elements being each name on the line
            if(lineCount == 1 and len(choices)==1): n = int(line)   #base case. finds value of n

            #######  ERROR CHECKING  #######
            elif(lineCount == 1 and len(choices)!=1): exit(1) # ensures line 1 always has 1 value
            if(lineCount>1 and len(choices) != n+1): exit(1) #Check for file format error (num of names per line)
            

            #######  BUILD DICTIONARY  #######
            if(lineCount > 1 and lineCount <= n+1): # Knights dictionary contstruction
                current_knight = choices.pop(0) #Make the knight the key
                KnightPrefs[current_knight] = choices #Make his preference list of ladies the values
            elif (lineCount > n+1): # Lady dictionary construction
                current_lady = choices.pop(0) #Make the lady the key
                LadyPrefs[current_lady] = choices #Make her preference list of knights the values


    if(lineCount != (2*n)+1): exit(1) #checks for instance of file not having correct num of lines.
    
    print("Knights: ", KnightPrefs) # FOR TESTING
    print("Ladies: ", LadyPrefs) # FOR TESTING

    return KnightPrefs, LadyPrefs # returns dictionaries

def propose(kPrefs, lPrefs):

def main():
    kPrefs, lPrefs = AssemblePreferences(sys.argv[1])
    

main()