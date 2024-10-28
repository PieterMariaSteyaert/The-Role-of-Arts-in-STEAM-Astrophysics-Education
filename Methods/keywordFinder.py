import pandas as pd
import RAKE

# Assuming your CSV file is named 'data.csv' and uploaded to Colab
df = pd.read_csv('/content/STEAMLIT_PROQ_19122022_KEYWORDFINDER.csv')

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
