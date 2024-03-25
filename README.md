#Restaurant Data Analysis and Visualization Project

This project analyzes and visualizes restaurant data from Swiggy, a popular food delivery platform in India. The data has been cleaned and processed to provide meaningful insights into the restaurant landscape across various cities in India.

##Data Cleaning
The dataset underwent thorough cleaning to handle ambiguous data and empty values. For instance, various ambiguous entries such as "New" and very few ratings were encountered in the ratings column. To address this, all ratings below 10 were grouped as "New". This step ensured consistency and reliability in the dataset.

##Additional Columns
Two new columns were added to enhance the dataset's utility:

###Rate Category: Restaurants were categorized into groups based on their ratings. The categories include "Very Good", "Good", "Above Average", and "Average". This categorization provides a glance at the dataset's overall rating distribution of restaurants.

###Swiggy Certified: This column identifies whether a restaurant is Swiggy certified or not. A restaurant is considered Swiggy certified if it has 30 or more ratings with a rating of 4 or above. This designation offers users assurance regarding the quality of service provided by Swiggy-certified restaurants.

##Data Visualization
The cleaned and enriched dataset was visualized to extract meaningful insights:

Overall Restaurant Data: A comprehensive plot showcasing various attributes of restaurants in the dataset, providing a holistic view of the restaurant landscape.

Bangalore Restaurants: A specific plot focusing on restaurants in Bangalore, highlighting the number of restaurants with a rating of 4 or above. This visualization offers insights into the quality of restaurants in a specific city.

Top Cities with 4+ Rated Restaurants: A plot illustrating the cities with the highest number of restaurants rated 4 or above. This visualization aids in understanding which cities offer a higher concentration of highly-rated dining options.
