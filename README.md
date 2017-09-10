# Crossword
Scraping questions and answers from New York Times crossword puzzles

If using python 2.7.X or lower, change 'html.parser' to HTMLParser in HTMLParserA.py and HTMLParserQ.py. Also line 88 in crosswordPuzzle.py may need to be refactored.

### Test by running tester.py

This will print out the dictionary of questions and answers of the puzzle defined in tester.py file. When running on FEB0409, this is given output.

{'Rubberneck': 'GAWK', 'Digital signal receiver': 'HDTV', 'Bailout button': 'EJECT', ' Down from the deck': 'ALOW', ' 16-Across\'s "La donna è mobile," e.g.': 'ARIA', ' See 15-Across': 'VERDI', ' 16th-century Florentine food?': 'RENAISSANCEFARE', ' Show compassion': 'BEKIND', ' Nereid sister of Galatea': 'IONE', ' Stopper of things': 'KIBOSH', ' Supermarket chain': 'IGA', ' Support staffer: Abbr.': 'ASST', ' Reason the tortoise won the race?': 'BADHAREDAY', ' A ring bearer may go down it': 'THEAISLE', ' Commonwealth country in Central America': 'BELIZE', ' Pennies': 'CENTS', " Clairvoyant's claim": 'ESP', ' Half of a 45 with more airplay': 'SIDEA', ' Turn toward the east': 'ORIENT', ' "Alas"': 'SADTOSAY', ' Baseballs, footballs and basketballs?': 'SPORTSWARE', ' Shopping bag': 'TOTE', ' Blacken': 'TAR', ' Like some sausages and Web sites': 'LINKED', ' Air condition': 'SMOG', ' Entree from the frozen food department': 'POTPIE', ' Freedom from the requirement of having long sleeves?': 'RIGHTTOBAREARMS', ' Thai or Chinese': 'ASIAN', ' Craving': 'URGE', ' Spree': 'TOOT', ' Ice bucket accessory': 'TONGS', ' Disgusting one': 'TOAD', ' Queries': 'ASKS', 'Shirts and skirts': 'GARB', "Salt's direction": 'ALEE', 'Policy ___': 'WONK', 'River in a Best Picture title': 'KWAI', 'Lays a claim (on)': 'HASDIBS', 'Patient observers: Abbr.': 'DRS', "Padre's sister": 'TIA', 'Dematerialize': 'VANISH', 'Drawn': 'EVEN', ' Baja boss': 'JEFE', ' Time to remember': 'ERA', ' Mil. leader': 'CDR', ' Draw': 'TIE', ' Press coverage': 'INK', ' Housemate, informally': 'COHAB', ' Bundle in a barn': 'BALE', ' Comedian Yakov Smirnoff, by birth': 'ODESSAN', ' Emphatic confirmation of action': 'IDIDSO', ' Eye intently': 'GAZEAT', ' Naval affirmative': 'AYEAYE', ' Without profit': 'ATCOST', ' Guide for Hillary': 'SHERPA', ' ___ moment': 'SENIOR', ' Spud': 'TATER', " Put one's feet up": 'REST', ' Poet who wrote "Old Possum\'s Book of Practical Cats"': 'ELIOT', " Ain't as it should be?": 'ISNT', ' Part of PRNDL': 'PARK', ' Groove for a letter-shaped bolt': 'TSLOT', ' Ruby': 'DEEPRED', ' Freak': 'WIGOUT', ' Anonymous John': 'DOE', " Farrah Fawcett's signature do": 'SHAG', ' Rockies, e.g.: Abbr.': 'MTNS', ' "Ciao!"': 'TATA', ' Old hands': 'PROS', ' "Don\'t worry about me"': 'IMOK', ' Figs. like "a million or so"': 'ESTS', ' Fink': 'RAT', ' Equal: Prefix': 'ISO', ' ___ and tonic': 'GIN', ' "Yo" man?': 'BRO', ' Ottoman V.I.P.': 'AGA'}

crosswordPuzzle.py can be altered to also print the answer grid.

[  
['G', 'A', 'W', 'K', ' ', 'H', 'D', 'T', 'V', ' ', 'E', 'J', 'E', 'C', 'T'],   
['A', 'L', 'O', 'W', ' ', 'A', 'R', 'I', 'A', ' ', 'V', 'E', 'R', 'D', 'I'],   
['R', 'E', 'N', 'A', 'I', 'S', 'S', 'A', 'N', 'C', 'E', 'F', 'A', 'R', 'E'],   
['B', 'E', 'K', 'I', 'N', 'D', ' ', ' ', 'I', 'O', 'N', 'E', ' ', ' ', ' '],   
[' ', ' ', ' ', ' ', 'K', 'I', 'B', 'O', 'S', 'H', ' ', ' ', 'I', 'G', 'A'],   
['A', 'S', 'S', 'T', ' ', 'B', 'A', 'D', 'H', 'A', 'R', 'E', 'D', 'A', 'Y'],   
['T', 'H', 'E', 'A', 'I', 'S', 'L', 'E', ' ', 'B', 'E', 'L', 'I', 'Z', 'E'],   
['C', 'E', 'N', 'T', 'S', ' ', 'E', 'S', 'P', ' ', 'S', 'I', 'D', 'E', 'A'],   
['O', 'R', 'I', 'E', 'N', 'T', ' ', 'S', 'A', 'D', 'T', 'O', 'S', 'A', 'Y'],   
['S', 'P', 'O', 'R', 'T', 'S', 'W', 'A', 'R', 'E', ' ', 'T', 'O', 'T', 'E'],   
['T', 'A', 'R', ' ', ' ', 'L', 'I', 'N', 'K', 'E', 'D', ' ', ' ', ' ', ' '],   
[' ', ' ', ' ', 'S', 'M', 'O', 'G', ' ', ' ', 'P', 'O', 'T', 'P', 'I', 'E'],   
['R', 'I', 'G', 'H', 'T', 'T', 'O', 'B', 'A', 'R', 'E', 'A', 'R', 'M', 'S'],   
['A', 'S', 'I', 'A', 'N', ' ', 'U', 'R', 'G', 'E', ' ', 'T', 'O', 'O', 'T'],   
['T', 'O', 'N', 'G', 'S', ' ', 'T', 'O', 'A', 'D', ' ', 'A', 'S', 'K', 'S']  
]

## To be done
- Scrape puzzles from https://www.nytimes.com/crosswords
- Convert ezch pdf to html
- automate this process
- store results in CSV
