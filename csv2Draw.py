# Required imports.
import sys

# Define constants.
SHAPE_POS = 3
CONNECTED_TO_POS = 4
TWO_WAY_CONNECTED_WITH_POS = 5
FILL_POS = 6
STROKE_POS = 7
DEFAULT_SHAPE = 'label'
DEFAULT_FILL = 'white'
DEFAULT_STROKE = 'black'
CONFIG_TEXT = """
## ## = comments 
## #  = configuration 
#
## Double arrow add: endArrow=classic;startArrow=classic;
#
# style: %shape%;image=%image%;whiteSpace=wrap;html=1;rounded=1;fillColor=%fill%;strokeColor=%stroke%;
# connect: {"from": "connectedTo", "to": "id"}
# connect: {"from": "twoWayConnectedWith", "to": "id", "style": "endArrow=classic;startArrow=classic;"}
# nodespacing: 60
# ignore: id,image,fill,stroke,refs,manager
# link: url
# layout: auto
#
## ---- CSV below this line. First line are column names. ----
"""

# Ensures there is a csv file for input.
if(len(sys.argv) != 2):
    print("Usage: \n     python */csv2Draw.py [.csv input file]")
    exit()

# Read in the csv file provided in the command line.
inputCSV = sys.argv[1]
with open(inputCSV, 'r') as f:
    csvContents = f.read()

# Clean csv contents.
if (len(csvContents) > 0 and ' ' in csvContents):
    temp = ""
    commaCount = 0
    withinQuotes = 0
    prev = ''
    for char in csvContents:
        # Decide if we are within quote marks.
        if (char == '"' and not withinQuotes):
            withinQuotes = 1
        elif ((char == ','  or char == '\n') and prev == '"' and withinQuotes):
            withinQuotes = 0

        # If fields are left blank, set their desired defaults.
        # Set default shape.
        if (commaCount == (SHAPE_POS - 1) and char == ',' and prev == ','):
            temp += DEFAULT_SHAPE
        # Set default fill color.
        elif (commaCount == (FILL_POS - 1) and char == ',' and prev == ','):
            temp += DEFAULT_FILL
        # Set default stroke/border color.
        elif (commaCount == (STROKE_POS - 1) and char == ',' and prev == ','):
            temp += DEFAULT_STROKE

        # Remove spaces in the connectedTo field to allow for multiple connections.
        if ((commaCount != (CONNECTED_TO_POS - 1) and commaCount != (TWO_WAY_CONNECTED_WITH_POS - 1)) or char != ' '):
            temp += char

        # At the end of a row, reset the commaCount.
        if (char == '\n'):
            commaCount = 0

        # Increment the comma count if not witin quotes.
        if (char == ',' and not withinQuotes):
            commaCount += 1

        # Store the prev char to give the next one context.
        prev = char

    # Replace acceptable values from the spreadsheet with values that make sense to Draw.io.
    # This looks much less optimal than it really is. It's just a looping if statement. 
    # If there are two instances it will only loop twice. 0 = 0, 1 = 1, etc.
    while ',cylinder,' in temp:
        temp = temp[:temp.index(',cylinder,') + 1] + 'shape=cylinder3' + temp[temp.index(',cylinder,') + (len(',cylinder,') - 1):]
    while ',database,' in temp:
        temp = temp[:temp.index(',database,') + 1] + 'shape=cylinder3' + temp[temp.index(',database,') + (len(',database,') - 1):]
    while ',human,' in temp:
        temp = temp[:temp.index(',human,') + 1] + 'shape=umlActor' + temp[temp.index(',human,') + (len(',human,') - 1):]
    while ',user,' in temp:
        temp = temp[:temp.index(',user,') + 1] + 'shape=umlActor' + temp[temp.index(',user,') + (len(',user,') - 1):]
    while ',developer,' in temp:
        temp = temp[:temp.index(',developer,') + 1] + 'shape=umlActor' + temp[temp.index(',developer,') + (len(',developer,') - 1):]
    while ',cloud,' in temp:
        temp = temp[:temp.index(',cloud,') + 1] + 'ellipse;shape=cloud' + temp[temp.index(',cloud,') + (len(',cloud,') - 1):]
    while ',circle,' in temp:
        temp = temp[:temp.index(',circle,') + 1] + 'ellipse' + temp[temp.index(',circle,') + (len(',circle,') - 1):]
    while ',diamond,' in temp:
        temp = temp[:temp.index(',diamond,') + 1] + 'rhombus' + temp[temp.index(',diamond,') + (len(',diamond,') - 1):]
    while ',square,' in temp:
        temp = temp[:temp.index(',square,') + 1] + 'label' + temp[temp.index(',square,') + (len(',square,') - 1):]

    csvContents = temp

# Slap it all together and print.
out = CONFIG_TEXT + csvContents
print(out)