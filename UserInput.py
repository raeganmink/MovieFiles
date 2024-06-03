import csv
import random

file="C:\\Users\\rmink\\Documents\\C#\\MovieFiles\\movfile.csv"

with open(file,'r') as f: 
        reader = csv.reader(f)

        mydict = {(row[2]):(int(row[3]),row[0], row[1],row[4],row[5],int(row[6])) for row in reader}

        values=mydict.values()
        items=mydict.items()
        newdict = mydict.copy()

        any= random.choice(list(newdict.items()))

        for key,value in list(newdict.items()):
            if 'y' in value:
                del newdict[key]

        PrefYesNo=input("Do you have any preferences? (Enter y for yes, n for no)")

        if PrefYesNo == 'n':
            print(random.choice(list(newdict.items())))
            print(random.choice(list(newdict.items())))
            print(random.choice(list(newdict.items())))
        else:
             streamFreeYN = input("Do you want to watch a free movie? (Enter y for yes)")
             if streamFreeYN == 'y': 
                for key, value in list(newdict.items()):
                     if 'amazon' in value:
                          del newdict[key]
                streamService = input("Would you like to watch something from a particular streaming service? if so enter the name: ")
                ##if streamService!='hbo max' or 'tubi' or 'showtime' or 'prime' or 'netflix' or 'paramount plus':
                     ##print("That is not a valid streaming service")
                if streamService!= '':
                    for key,value in list(newdict.items()):
                         if streamService not in value:
                              del newdict[key]              
             timeLimit = input("What is your time limit? (Enter limit in minutes)")
             if timeLimit == '':
                timeLimit = 500
             for key, value in list(newdict.items()):
                   if value[5]>int(timeLimit):
                       del newdict[key]
             yearLimit = input("Do you have a release date limit?")
             if yearLimit == 'y':
               yearLimitLow = input("What is your release date limit(low)?")
               if yearLimitLow=='':
                    yearLimitLow = 1900
               for key, value in list(newdict.items()):
                   if value[0]<int(yearLimitLow):
                       del newdict[key]
               yearLimitHigh = input("What is your release date limit(high)?")
               if yearLimitHigh=='':
                    yearLimitHigh=2024
               for key,value in list(newdict.items()):
                    if value[0]>int(yearLimitHigh):
                         del newdict[key]
             langPref = input("Would you like to watch a movie in English? (Enter y for yes, n for no)")
             if langPref== 'y': 
                  englishLang = dict((key,value) for key,value in newdict.items() if value[4]=='english')
                  print(random.choice(list(englishLang.items())))
                  print(random.choice(list(englishLang.items())))
                  print(random.choice(list(englishLang.items())))
             elif langPref=='n':
                  foreignLang = dict((key,value) for key,value in newdict.items() if value[4]!='english')
                  print(random.choice(list(foreignLang.items())))
                  print(random.choice(list(foreignLang.items())))
                  print(random.choice(list(foreignLang.items())))
             else:
                  print(random.choice(list(newdict.items())))
                  print(random.choice(list(newdict.items())))
                  print(random.choice(list(newdict.items())))
                  
                  
                
    