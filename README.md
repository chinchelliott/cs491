# cs491
Semester Project for CS course
  - Raychel Delaney, Justin Lukas, Elliott Miller

---Using Sentiment Analysis to evaluate "Social Sensitivity" towards wildfires--- 

Project outline: 

1. Retrieve tweets on wildfires using the twitter stream 

2. Assign sentiment to tweets 

3. Use those tweets to train a classifier using a support vector machine algorithm

4. Now gather tweets on two or more different wildfire incidents to be evaluated using a stream 

5. Perform sentiment analysis on seperate data sets 

6. Using the results, compare the overall reaction/attention to the individual wildfires

7. Using geotagging, consider location with other attributes in comparison
   - location to evaluate regional factors 
   - severity
   - duration
   - population of affected area
  
8. Track/present the results using data visualization tools to display findings 
   - tablo vs d3.js
  
  
  
 STRETCH GOAL: Compare the results of sentiment analysis using different SVM algorithms 


Description of files contained in this repo:

  - wildfire_tweets.py : Code that pulls tweets containing wildfire keywords.  
  
  - training_data.txt : The tweets collected and tagged in order to train our algorithm.
  
  - california_tweets.py/portual_tweets.py : Code that pulls tweets containing our target locations.
  
  - cali_tweets.txt/port_tweets.txt : The tweets about "california" and "portugal" that were pulled.
  
  - training_tweets.py : Code that uses training_data.txt to train our SVM algorithm, which is then used to determine the relevance of tweets from our cali and port txt files.  
  
  - location_comparison.txt : The results from evaluating the unclassified tweets. 
