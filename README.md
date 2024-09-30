# The Role of Arts in STEAM Astrophysics Education

This repository contains scripts and data used in the article _"The Role of Arts in STEAM Astrophysics Education."_  
The article is currently being written and is expected to be published soon.

## Dependencies

To use the scripts provided in this repository, please ensure the following Python packages are installed:

- [RAKE (Rapid Automatic Keyword Extraction)](https://github.com/fabianvf/python-rake)
- `pandas`

You can install these dependencies using `pip`:

```bash
pip install python-rake pandas
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/PieterMariaSteyaert/The-Role-of-Arts-in-STEAM-Astrophysics-Education
cd The-Role-of-Arts-in-STEAM-Astrophysics-Education
```

2. Install the required dependencies (if not already installed):

```bash
pip install -r requirements.txt
```

## Query Generator

The scripts in this repository generate search queries for academic databases such as ProQuest and Web of Science. These queries are built by looping over a collection of keywords. Below are the query generation structures for each database.

### ProQuest

The following script generates a search query for ProQuest by iterating over a list of keywords:

```python
for keyword in collection:
    results += "noft(" + keyword + ") OR "
```

### Web of Science

For Web of Science, the script constructs a query by searching in the title (`TI`), abstract (`AB`), and topic (`TS`) fields:

```python
for keyword in collection:
    results += "(TS=(" + keyword + ") OR TI=(" + keyword + ") OR AB=(" + keyword + ")) OR "
```

## Data Overview

The key data file included in this repository is:

- **`Article Selection Procedure - All data.csv`**  
  This file contains the search results from the Web of Science and ProQuest databases used in the article's research.

---

# RAKE Script Results for Query Generation

This repository contains CSV files that are the output of a RAKE (Rapid Automatic Keyword Extraction) script. These files are used to assist in the query generation for academic database searches.

## File Descriptions

1. **Parameters.csv**  
   Contains the parameters used during the RAKE script run.

2. **Cycle1.csv**  
   Keywords and data generated during the first cycle of RAKE extraction.

3. **Cycle 1 - data.csv**  
   Raw data collected for Cycle 1, used as input for the RAKE keyword extraction.

4. **Cycle1 - filtered.csv**  
   Filtered results from Cycle 1 using the inclusion criteria.

5. **Cycle1 - keywords.csv**  
   Keywords extracted from the raw data during Cycle 1.

6. **Cycle1 - filtered keywords.csv**  
   Filtered set of keywords that passed the inlcusion criteria in Cycle 1.

7. **cycle 1 - resulting Query.csv**  
   The resulting search query generated from Cycle 1 keywords, designed for use the databases.

8. **Cycle2.csv**  
   Keywords and data generated during the second cycle of RAKE extraction.

9. **Cycle 2 - data.csv**
10. **Cycle2 - filtered.csv**
11. **Cycle 2 - keywords.csv**
12. **Queries.csv**  
    The set of queries generated across all cycles for both ProQuest and Web of Science databases.

---

### Additional Notes

If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
