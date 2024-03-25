# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('dark_background')
from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv('/content/drive/MyDrive/Datasets/swiggy_file.csv') #read data from the csv file
df.head()

# Dropping values in 'RATINGS' column

def hr(value):
    if(value=='NEW' or value=='--'):
        return np.nan
    else:
        return float(value)
df['Rating']=df['Rating'].apply(hr)

# Adding a new column= rate category, groups the restaurants into 4 categories: 'Very good', 'Good', 'Above average' & 'Average'

import pandas as pd 

df = pd.read_csv('/content/drive/MyDrive/Datasets/swiggy_file.csv') # Read the CSV file into a DataFrame

# Convert 'Rating' column to numeric values
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce') # Read the CSV file into a DataFrame

def classify_rating(rating): # Define a function to classify ratings
    if rating >= 4.3:
        return 'Very Good'
    elif 3.8 <= rating < 4.3:
        return 'Good'
    elif 3.2 <= rating < 3.8:
        return 'Above Average'
    else:
        return 'Average'


df['Rating Category'] = df['Rating'].apply(classify_rating) # Apply the classification function to create a new column 'Rating Category'

df.to_csv('your_file_with_categories.csv', index=False)# Save the DataFrame back to the CSV file

# Cleaning the 'Number of Ratings' column

def numberRatingConverter(s): # This function removes the 'Too few ratings' and 'nan' and replaces them with 0, it also replaces 'K+' in the string with 000
  s=str(s)
  if s=='Too Few Ratings' or s=='nan':
    return 0
  s=s.replace('K+','000')
  ans=''
  for i in s:
    if i.isdigit():
      ans+=i
  return int(ans)

df['Number of Ratings'] = df['Number of Ratings'].apply((numberRatingConverter)) 

# Creating a new column called Swiggy certified which relates the ratings and rating category columns

def swiggyCert(row):
    if row['Number of Ratings']>30 and row['Rating Category'] in ['Good', 'Very Good']: # a restaurant is swiggy certified if and only if it has both 30+ ratings and belongs either to good or very good category
        return 'Yes'
    else:
        return 'No'

df['Swiggy Certified'] = df.apply(swiggyCert,axis=1)

df.to_csv('/content/drive/MyDrive/Datasets/swiggy_file.csv', index=False)

df.rename(columns={'Cuisine': 'Cuisines'}, inplace=True)
df.rename(columns={'Price for 2': 'Price for 2 (in ₹)'}, inplace=True)

df.head()

#Cleaned the average price column and renamed it to 'Price for 2', also changed the data from strings to display only the integers
#example: '250 for 2' was changed to 250 in the csv file

def pf2(s):
  s=str(s)
  ans=''
  for i in s:
    if i.isdigit():
      ans+=i
  return int(ans)

df['Price for 2 (in ₹)'] = df['Price for 2 (in ₹)'].apply((pf2))

#Cleaned the 'Offers' column which displayed 2-3 offers right next to each other with \n being written and made them appear one below another

df['Offer Name'] = df['Offer Name'].str.replace('\n', ', ')









