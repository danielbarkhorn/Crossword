import HTMLParserQ
import HTMLParserA
from collections import OrderedDict
import codecs

def toDate(abbr):
    # month = abb[0:4]
    day = abbr[3:5] if (abbr[3] != '0') else abbr[4]
    year = int(abbr[5:7])
    year += 2000 if (year<18) else 1900
    return (day + ", " + str(year))

class crosswordPuzzle(object):
    """Class Representing a Crossword puzzle"""

    # Variables
    fullText = ''
    across = OrderedDict()
    down = OrderedDict()
    QA = {}

    # Constructors
    def __init__(self, HTMLFilePathA, HTMLFilePathQ):
        self.pathA = HTMLFilePathA
        self.pathQ = HTMLFilePathQ

    # Methods
    def initiate(self):
        fileA = codecs.open(self.pathA)
        fileQ = codecs.open(self.pathQ)
        parserA = HTMLParserA.crosswordAHTMLParser()
        parserQ = HTMLParserQ.crosswordQHTMLParser()
        parserA.feed(fileA.read())
        parserQ.feed(fileQ.read())
        self.fullText = parserQ.words
        self.getQuestions()
        self.answerGrid = parserA.grid
        self.match()
        print(self.QA)

    def getQuestions(self):
        acrossIndex = self.fullText.rfind('ACROSS')+len('ACROSS')+1
        downIndex = self.fullText.rfind('DOWN')
        lastKey = ''

        acrossTemp = self.fullText[acrossIndex:downIndex].splitlines()
        for line in acrossTemp:
            if(line[0:2].strip().isdigit()):
                lastKey = line[0:2].strip()
                self.across[lastKey] = line[2:len(line)]
            else:
                self.across[lastKey] = self.across[lastKey] + " " + line

        # -8 is to get rid of 'Page: 1" that is at end of all these html files'
        downDict = OrderedDict()
        downTemp = self.fullText[downIndex + len('DOWN') + 1: -8].splitlines()
        for line in downTemp:
            if(line.strip().isdigit()):
                continue
            elif(line[0:2].strip().isdigit()):
                lastKey = line[0:2].strip()
                downDict[lastKey] = line[2:len(line)]
            else:
                downDict[lastKey] = downDict[lastKey] + " " + line
        for q in sorted(map(int, downDict.keys())):
            self.down[str(q)] = downDict[str(q)]

    def match(self):
        acrossTotal = downTotal = ''
        for row in self.answerGrid:
            acrossTotal += ' ' + ''.join(row)
        self.QA = dict(zip(self.across.values(), acrossTotal.split()))

        def findDown(self, row, ind, downTotal):
            row = list(row)
            if (ind == 0 or row[ind-1] == ' ') and row[ind].isalpha():
                while ind < 15 and row[ind].isalpha():
                    downTotal += row[ind]
                    row[ind] = ' '
                    ind+=1
                downTotal += ' '
            return downTotal

        answerGridT = list(zip(*self.answerGrid))
        for i in range(15):
            for j in range(15):
                downTotal = findDown(self, answerGridT[j], i, downTotal)
        self.QA = {**self.QA, **(dict(zip(self.down.values(), downTotal.split())))}
