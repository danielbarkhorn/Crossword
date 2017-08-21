from htmlparser import HTMLParser
import codecs
import numpy

# Here I am creating a subclass and overriding the handler methods
class crosswordQHTMLParser(HTMLParser):
    words = ''

### Functions ###
    def handle_data(self, data):
        if(data != '\n'):
            self.words += data
