import sys
import timeit

#Invariants: If there are n knights and n ladies in the file, the file is 2n+1 lines in length
#Intialization: The first line of the file specifies the number of knights and number of ladies
#Maintenance: Every subsequent iteration of the loop after the first one adds the preferences of that knight/lady to a dictionary
#Termination: This function will end with every knight having a defined set of preferences listed out
def AssemblePreferences(fileName):
    KnightPrefs = {} # Dictionary with knights as keys and list of ladies as values
    LadyPrefs = {} # Dictionary with ladies as keys and list of knights as values
    lineCount = 0
    n = 0
    #Open the file and put the preferences in dictionaries
    with open(fileName) as f:
        for line in f:
            ####### INITIALIZE IMPORTANT VAR's  #######
            lineCount+=1 # tracks line number.
            line = line.strip() #removes newline char from each line
            choices = line.split(" ") #Makes an array with elements being each name on the line

            if(lineCount == 1 and len(choices)==1): n = int(line)   #base case. finds the number of knights and ladies
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

    return KnightPrefs, LadyPrefs, n # returns dictionaries

#Invariant: This function will always result in a dictionary of n pairs with nobody left unpaired
def propose(kPrefs, lPrefs, n):
    married = {}
    while (len(married) < n):
        #Intialization: Nobody is paired
        #Maintenance: During every iteration, a knight proposes to one of his preferences and a pair is either created or modified
        #Termination: the end of this loop will result in all knights being paired
        for knight in kPrefs: 
            if(knight not in married.values()):
                lady = kPrefs[knight][0]
                kPrefs[knight].remove(lady)

                if (lady not in married.keys()):
                    married[lady] = knight # (knight, lady) added to married
                elif (lady in married.keys()):  # some pair (knight2, lady) already exists
                    currSpouse = married[lady] # get the key (knight) from the pair that the lady is in
                    # traverse her preferences and keep track of the indicies of the two knights
                    knightIndex = lPrefs[lady].index(currSpouse)
                    newKnightIndex = lPrefs[lady].index(knight)

                    # compare the indices
                    if(newKnightIndex < knightIndex):
                        del married[lady]
                        married[lady] = knight


    return married

def main():
    if(len(sys.argv) != 2): exit(1)
    kPrefs, lPrefs, n = AssemblePreferences(sys.argv[1])
    married = propose(kPrefs, lPrefs, n)
    for key in married:
        print(married[key] + " " + key)
main()

#print >> sys.stderr, (timeit.timeit(setup=main, stmt=main, number=1))
