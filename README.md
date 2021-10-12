# Graph Auto-generation: CSV -> Diagram 

This serves as the documentation to explain how to utilize the csv2Draw.py script to 
sanitize and structure a csv output from a spreadsheet application into input that Draw.io/Diagrams.net
will understand and use to create a bare-bones implementation of all specified nodes and 
connections in a pre-arranged fashion.

## Framing:

The main goal for the csv2Draw.py script is to take initial steps in generation of graphs
from various sources of data. A csv file is seen as a mediary format to take data from one
application and translate it into something that is understandable to another application.
This is initially being tested by transferring a .csv output file from structured Google
Sheets and Excel Spreasheets into a diagram that can then be tweaked and styled much easier.

## Usage:

Draw.io allows for input through CSV in the 'Arranged'->'Insert'->'Advanced'->'CSV' menu
option. Here you will see an example of a CSV and can then 'Import' to see the resulting
diagram that has been created. This CSV input uses ## to denote comments and # to denote
configurations. The csv2Draw.py has taken care of configurations to best enable a sensible
graph generation. The script will then take a csv file and use the first line to structure
the rest of the decisions made both in the script and from the configuration lines.

### Representation:

A semi-structured excel spreadsheet can be found in this folder. The first line specifies 
the names of the fields. The first 7 fields must remain in the order they are, or you will
have to change their position in the program constants portion of the script at the top 
of the file. Here are pertinent details to the first 7 fields:

- name
	- Case sensitive, spaces will remain in tact, nodes will use this as their label
- id
	- This is usually an abbreviated version of the name and is to be used in other fields
- shape
	- default: rectangle
	- cloud
	- square
	- rectangle
	- diamond
	- triangle
	- person: accepts user, human, developer
	- cylinder: accepts cylinder, database
- connectedTo
	- One-way arrow starting at this node and ending at the node id(s) specified in this field
	  separated by commas with or without spaces in between them.
- twoWayConnectedWith
	- Two-way arrow starting at this node and ending at the node id(s) specified in this field
	  separated by commas with or without spaces in between them.
- fill
	- Specifies the color of this node. Accepts english (green, red, etc.) or the hex value
	  (#123456, #abcdef, etc.)
- stroke
	- Specifies the color of this node outline. Accepts english (green, red, etc.) or the hex value
	  (#123456, #abcdef, etc.).
- All additional fields
	- any other field you may want to use when generating the graph can be written to the right of
	  the existing ones, but you will have to edit the code to both use these fields in the configuration
	  portion of the file as well as structure the inputs given.

### Script calling convention:

python */csv2Draw.py [.csv input file]
