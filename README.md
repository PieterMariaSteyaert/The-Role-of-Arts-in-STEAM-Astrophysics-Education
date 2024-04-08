# The-Role-of-Arts-in-STEAM-Astrophysics-Education-
Scripts used for article "The Role of Arts in STEAM astrophysics education"

This article is currently being written.

## Dependencies
 - rake https://github.com/fabianvf/python-rake
 - pandas

## Installation
- Make sure the dependencies are installed

## Query generator
The queries generated for both ProQuest and WebOfScience are the result of looping over the included keywords

### ProQuest
```
for keyword in collection:
	results += "noft("+keyword+") OR "
```

### WebOfScience
```
for keyword in collection:
	results += "(TS=("+keyword+") OR TI=("+keyword+") OR AB=("+keyword+")) OR "
```

## Overview of data
- "Article Selection Procedure - All data.csv" - Results from Web of Science and ProQuest databases 
