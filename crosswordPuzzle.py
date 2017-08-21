import HTMLParserQ
import HTMLParserA
from collections import OrderedDict
import codecs
import numpy

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
        downTemp = self.fullText[downIndex + len('DOWN') + 1: -8].splitlines()
        for line in downTemp:
            if(line[0:2].strip().isdigit()):
                lastKey = line[0:2].strip()
                self.down[lastKey] = line[2:len(line)]
            else:
                self.down[lastKey] = self.down[lastKey] + " " + line

    def match(self):
        top = leftB = leftE = 0
        for AQ in self.across:
            while not str(self.answerGrid[top][leftB]).isalnum() and leftB < 14:
                leftB += 1
            leftE = leftB
            while leftE < 14 and str(self.answerGrid[top][leftE]).isalnum():
                leftE += 1
            if(leftE == 14 and str(self.answerGrid[top][leftE]).isalnum()):
                leftE+=1
            self.QA[str(AQ)+str(self.across[AQ])] = "".join(self.answerGrid[top][leftB:leftE])
            print(leftB, leftE)
            if(leftE > 11):
                if(top < 14):
                    top += 1
                    leftB = leftE = 0
                else:
                    break
            while str(self.answerGrid[top][leftE]).isalnum() and leftE < 14:
                leftE += 1
            leftB = leftE

        left = topB = topE = 0
        for DQ in self.down:
            while not str(self.answerGrid[topB][left]).isalnum() and topB < 14:
                topB += 1
            topE = topB
            while topE < 14 and str(self.answerGrid[topE][left]).isalnum():
                topE += 1
            if(topE == 14 and str(self.answerGrid[topE][left]).isalnum()):
                topE+=1
            print(topB, topE, left)
            self.QA[str(DQ)+str(self.down[DQ])] = "".join(self.answerGrid[topB:topE][left])
            print(topB, topE)
            if(topE > 11):
                if(left < 14):
                    left += 1
                    topB = topE = 0
                else:
                    break
            while str(self.answerGrid[topE][left]).isalnum() and topE < 14:
                topE += 1
            topB = topE
