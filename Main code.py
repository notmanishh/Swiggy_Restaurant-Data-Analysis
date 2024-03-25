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


# Plot to show the number of restaurants that are pure veg
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 10))
sns.countplot(data=df, x='Pure Veg', palette='inferno')  # Passing data=df
plt.show()

# Plot to show the total number of restaurants in each city in the dataset
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(100,80))
sns.countplot(data=df, x='Location', palette='Set3')  # You can change 'Set3' to any other palette
plt.xticks(rotation=90)
plt.show()

# Plot to show the total number of restaurants in Bangalore and to show the frequency of the rating for  the restaurants
import seaborn as sns
import matplotlib.pyplot as plt

bangalore_df = df[df['Location'] == 'Bangalore'] # Filter DataFrame to include only rows with location 'Bangalore'

plt.figure(figsize=(10, 6))
sns.histplot(bangalore_df['Rating'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of Ratings for Restaurants in Bangalore')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

# Plot to show the top cities with the most number of 4+ ratings

import seaborn as sns
import matplotlib.pyplot as plt

high_rated_restaurants = df[df['Rating'] >= 4] # Filter the DataFrame for restaurants with ratings 4 or higher

city_restaurant_counts = high_rated_restaurants.groupby('Location').size().reset_index(name='restaurant_count') # Group by location (assuming 'Location' column represents cities) and count the number of restaurants in each city

sorted_cities = city_restaurant_counts.sort_values(by='restaurant_count', ascending=False) # Sort the cities by the number of highly rated restaurants

plt.figure(figsize=(12, 8))
sns.barplot(data=sorted_cities.head(10), x='restaurant_count', y='Location', palette='viridis')
plt.xlabel('Number of Highly Rated Restaurants')
plt.ylabel('City')
plt.title('Top Cities with the Most Number of Restaurants with 4+ Ratings')
plt.show()

# Plot to show the top cuisines among the highly-rated restaurants

import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter

high_rated_restaurants = df[df['Rating'] >= 4] # Filter the DataFrame for restaurants with ratings 4 or higher

cuisine_list = high_rated_restaurants['Cuisines'].str.split(',').sum() # Extract the 'Cuisines' column and split into individual cuisine entries

cuisine_counts = Counter(cuisine_list) # Count the occurrences of each cuisine

cuisine_df = pd.DataFrame.from_dict(cuisine_counts, orient='index').reset_index() # Convert the Counter to a DataFrame
cuisine_df.columns = ['Cuisine', 'Frequency']

sorted_cuisines = cuisine_df.sort_values(by='Frequency', ascending=False) # Sort the cuisines by frequency

plt.figure(figsize=(12, 8))
sns.barplot(data=sorted_cuisines.head(10), x='Frequency', y='Cuisine', palette='muted')
plt.xlabel('Frequency')
plt.ylabel('Cuisine')
plt.title('Top Cuisines Among Highly Rated Restaurants')
plt.show()








