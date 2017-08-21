from html.parser import HTMLParser
import codecs
import numpy



# Here I am creating a subclass and overriding the handler methods

class crosswordAHTMLParser(HTMLParser):
    words = ''
    ans = False
    grid = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

### Functions ###
    def is_crossword_ans(self, data):
        letters = data.split()
        for i in range(0,len(letters)):
            if(len(letters[i]) != 1 or not letters[i].isupper() or not letters[i].isalpha()):
                return False
        return True

    def handle_data(self, data):
        if(data != '\n'):
            data = str(data).strip()
            if (self.ans and self.is_crossword_ans(data)):
                letters = data.split()
                for i in range(0,len(letters)):
                    self.grid[int((self.currTop-126)/37.0)][int((self.currLeft-30)/37.0)+i] = letters[i]
                self.ans = False

    def handle_starttag(self, tag, attrs):
        if(tag == 'div'):
            top = attrs[0][1][attrs[0][1].find('top:')+4:attrs[0][1].find('top:')+7]
            left = attrs[0][1][attrs[0][1].find('left:')+5:attrs[0][1].find('left:')+8]
            if(not left.isnumeric()):
                left = attrs[0][1][attrs[0][1].find('left:')+5:attrs[0][1].find('left:')+7]
            if(top.isnumeric() and left.isnumeric()):
                itop = int(top)
                ileft = int(left)
                if(itop >= 120 and itop <= 660 and ileft >= 25 and ileft <= 570):
                    self.ans = True
                    self.currTop = itop
                    self.currLeft = ileft
