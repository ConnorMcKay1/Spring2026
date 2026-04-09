'''
SIMPLE RELATIONSHIPS:
    Which variables are related to the output?
    Are relationships linear or monotonic?
        
PREDICTIVE MODELING:
    How well can I predict the output from the inputs?
    ****Which variables matter most?****  use this to find out which variable affects strenght the most?

EFFECTS OF INTERACTION:
    Do variables combine in not obvious ways?


'''



print("test test turnip \n")


dataFile = "C:/Users/cmcka/OneDrive/Desktop/Spring2026/AppliedProbability&Statistics/AppliedProb&StatsConcrete/concrete_compressive_strength.csv"

def DataReadIn(csvFile):
    with open(csvFile, 'r') as file:
        for line in file:
            print(line.strip())



DataReadIn(dataFile)
