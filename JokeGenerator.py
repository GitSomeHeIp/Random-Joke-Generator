import random
import os.path
import sys
import getopt

def help():
    sys.exit('python JokeGenerator.py -d <jokesdatabase>')

def random_line(afile,count):
    rnumber = random.randint(0,count-2)
    #print(rnumber)
    for num,aline in enumerate(afile,0):
        if(num == rnumber and num % 2 == 0):
            nline = next(afile)
            return aline + nline
        elif(num == rnumber):
            aline = next(afile)
            nline = next(afile)
            return aline + nline
        else:
            continue

def line_count(db_name):
    count= -1
    if(os.path.isfile(db_name)):
        count = len(open(db_name, encoding="utf8").readlines())
    else:
        sys.exit("Sorry, your file doesn't exist.")
    return(count)

try:
    options, args = getopt.getopt(sys.argv[1:], "d:")
except getopt.GetoptError as err:
    sys.exit("Sorry, I do not recognize this file.")

default_jokes = "jokesdatabase"
db_name = default_jokes

if(len(options)):
    for opt, arg in options:
        if opt in ['-d']:
            db_name = arg
        else:
            help()
elif len(args) == 1:
    db_name = args[0]
else:
    help()

#print("I will attempt to read this file" + db_name)

fcount = line_count(db_name)

nad = open(db_name, "r", encoding="utf8")
joke = random_line(nad, fcount)
print(joke)
