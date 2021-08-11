# Data-Analysis-Project-From-Scratch

The aim of this project is to scrape the job postings related to Data Science and Machine Learning domain and analyze them. 

# Project Structure

- **Data_Scraping.py**: Scrapes the job portal to get the job details.
- **Data_Cleaning.py**: Cleaning the scraped data for further analysis.
- **Data_Analysis.ipynb**: Python notebook to analyze the scraped data. 

# Python Libraries and Versions 

- **Python Version**: 3.7.6
- **matplotlib**: 3.1.3
- **numpy**: 1.18.1
- **pandas**: 1.0.1
- **plotly**: 4.6.0
- **scipy**: 1.4.1
- **seaborn**: 0.11.1
- **selenium**: 3.141.0
- **spacy**: 2.3.5

# Web Scraping

20000 Job postings were scraped from the job portal and for each job posting following details were obtained, and all the details were converted to a comma separated file (Raw_Data.csv)

- Title
- Company
- Experience
- Location
- Tags
- Ratings
- Reviews
- Salary
- Job_Type
- Posting

**Note:** Selenium was used to scrape the data and as long as the names of the elements in the HTML file do not change, this works just fine. 

# Cleaning the raw data

- Reviews column was split based on the White space to get the count of the number of reviews.
- Experience column was split based on the Hyphen to et the Minimum and Maximum experience needed. 
- The exact number of days since the job posting was obtained by splitting Posted column based on certain text and relevant information was obtained. 
- Salary column was alphanumeric and approproate steps were taken to get the Minimum, Maximum and Average salary.
- Tags column was split based on the Newline character and all the tags were joined by comma.
- Location column had a lot of duplicate values and there were many values replaced with approproate replacements. 
- Duplicate rows were dropped. 

**Note:** Although extensive data cleaning was performed, some of the minute details migt have been left out. 

# Exploratory Data Analysis

Following are the insights from EDA,

1. An experience of 4-6 Yrs seems to be most preferred followed by 6-8 years of experience. Following chart explains the distribution of experience level preferred,
![Experience](https://user-images.githubusercontent.com/25604111/129079385-b33a2918-ff8f-4472-ab92-710fa13297b2.png)
