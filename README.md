# Energy Information Administration API functions
--
Code, with examples, of accessing different API's for Economic research, and exploration. Mostly in Python and R.

## Pseudo Code
--

````
```
Pseudo Code: True for most data sets
-------------------------------------------------------------------------------------------------
def data extraction(): 						
	set global variables
	request the zip file direct from link 
	with zip file (defined as f) 
		=> write the contents into working directory
	unzip the file and extract all its contents (1 txt file specifically)
	with text file from zip
			for each json object (multiple)
			deconstruct json objects
			append into a list into dict
		convert from dict to dataframe
	Take data (for multiple years, and obs) and explode into multiple rows
	due to "explode" index series is duplicated => reset to normal indicies
	Drop NAN values from data frame in order to split Data column from ['number', 'year'] to two separate cols. 'Value' and 'Year'


def data preperation(): # 
	[[[ grab the data from elec, intl, nuc, pet, ng, te, ... , ALL and combine into one major data frame ]]]
	print column titles
		=> allow user to select whichever columns from data frame that will be included
		=> display unique series ids, with names 
	set index as series ids
	User input, list of series ids
		=> append these series ids into one comprehensive dataframe
	Year column 
		=> If string > 4 characters, split after midpoint 4 (e.g 2021Q1)
		=> Convert to date.time format (for graphing purposes) 
	Reset Index
	Reformat the data so that series id becomes variable name NOT index
	export to CSV or XLSX if needed  

ADDITIONS: Save file to working directory, if the file is already in the directory (set data frame as saved pickle).
Saves, time and efficiency. Provide an IF statement (Would you like to update the file) (Yes/No)? Combine strings 
from each input and 
```
````
