import csv
import random

file="movfile.csv"

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

        unseen = random.choice(list(newdict.items()))

        oldies = dict((key,value) for key,value in newdict.items() if value[0]<=1970)
        newMov = dict((key,value) for key,value in newdict.items() if value[0]>=2000)
        foreignLang = dict((key,value) for key,value in newdict.items() if 'english' not in value)
        englishLang = dict((key,value) for key,value in newdict.items() if value[4]=='english')
        stream = dict((key,value) for key,value in newdict.items() if 'amazon' not in value)
        

        streamFreeOld = dict((key,value) for key,value in stream.items() if value[0]<=1970)
        streamFreeNew = dict((key,value) for key,value in stream.items() if value[0]>=2000)
        streamFreeForeignLang = dict((key,value) for key,value in stream.items() if 'english' not in value)
        streamFreeEnglish = dict((key,value) for key,value in stream.items() if value[4]=='english')

        overZero = dict((key,value) for key,value in newdict.items() if value[5]>1)
        veryLongMovie = dict((key,value) for key,value in overZero.items() if value[5]>180)
        longMovie = dict((key,value) for key,value in overZero.items() if value[5]>150)
        mediumMovie = dict((key,value) for key,value in overZero.items() if value[5]>120)
        midShort = dict((key,value) for key,value in overZero.items() if value[5]>100)
        shortMovie = dict((key,value) for key,value in overZero.items() if value[5]<=100)

        watchTime=0
        for key,value in overZero.items():
             watchTime+=value[5]
             watchTimeHours=watchTime/60
        print("Watch Time Remaining: {:.2f} hours".format(watchTimeHours))
    

        oldMovie = random.choice(list(oldies.items()))
        newMovie = random.choice(list(newMov.items()))
        forLang = random.choice(list(streamFreeForeignLang.items()))
        english = random.choice(list(streamFreeEnglish.items()))
        streamF = random.choice(list(stream.items()))
        streamFOld= random.choice(list(streamFreeOld.items()))
        streamFNew = random.choice(list(streamFreeNew.items()))



        seenPercentage = 100-((len(newdict)/250)*100)
        longMovies= len(longMovie) - len(veryLongMovie)
        midMov= len(mediumMovie) - longMovies -len(veryLongMovie)
        shortMidMov= len(midShort) - midMov - longMovies - len(veryLongMovie)
        print("Seen Percentage:{:.2f}%".format(seenPercentage))
        print("Total: {:d}".format(len(newdict)))
        print("Old (Pre 1970): {:d}".format(len(oldies)))
        print("Mid (1970-2000):{:d}".format(midMov))
        print("New (Post 2000):{:d}".format(len(newMov)))
        print("Foreign Language:{:d}".format(len(foreignLang)))
        print("English:{:d}".format(len(englishLang)))
        print("Stream Free: {:d}".format(len(stream)))
        print("Very Long (>180 min):{:d}".format(len(veryLongMovie)))
        print("Long Movie (150:180):{:d}".format(longMovies))
        print("Medium (120:150):{:d}".format(midMov))
        print("Mid Short(100:120):{:d}".format(shortMidMov))
        print("Short(<100 min): {:d}".format(len(shortMovie)))

    







        