# The Role of Arts in STEAM Astrophysics Education

This repository contains scripts and data used in the article _"The Role of Arts in STEAM Astrophysics Education."_

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

---

### Additional Notes

If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
