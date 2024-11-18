import pandas as pd
import RAKE

# replace with data CSV
df = pd.read_csv('DATA.csv')

# Initialize Rake
rake = RAKE.Rake(RAKE.SmartStopList())

# Function to apply RAKE on a row and return keywords
def extract_keywords(row):
  text = ""
  for i in range(len(df.columns)):
    text += str(row[i]) + ''; 
  return rake.run(text)

# Apply the function to each row
df['Keywords'] = df.apply(extract_keywords, axis=1)

#post process-Keywords
