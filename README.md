# Data-Analysis-Project-From-Scratch

The aim of this project is to scrape the job postings related to Data Science and Machine Learning domain and analyze them. The project covers following aspects of any DS / ML project,

1. Data Collection.
2. Data Cleaning.
3. Data Analysis.
4. Data Visualization. 

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

Following are some of the insights from EDA,

1. An experience of 4-6 Yrs seems to be most preferred followed by 6-8 years of experience.
2. Data Scientist and Data Analyst are the top 2 job titles, Data Engineer and Senior Data Scientist also feature in top 15 job titles. It was also observed that most of the other titles did not directly refer to DS / ML, but the skillset suggested otherwise. 
3. Bengaluru tops the list of most preferred locations followed by Hyderabad and Pune. 
4. Java, SQL and Python were the top 3 programming languages that were preferred.
5. Accenture tops the list of companies with most number of Job openings with 78.2% of total job openings, followed by IBM and Bajaj FinServ. Surprisingly, none of the companies focused on Data Science / Machine Learning fall in the top 10.
6. Tableau, PowerBI and IBM Cognos were the most preferred Visualization tools. 
7. SAP, Microsoft Azure, AWS were the top cloud platforms. 

![Experience](https://user-images.githubusercontent.com/25604111/129079385-b33a2918-ff8f-4472-ab92-710fa13297b2.png)
![Titles](https://user-images.githubusercontent.com/25604111/129080321-9b32b76a-e3c8-422a-b763-c94dd9ff53b8.png)
![Locations](https://user-images.githubusercontent.com/25604111/129079664-a3af7398-39ff-4667-a0ff-29d6165b4b83.png)
![Languages](https://user-images.githubusercontent.com/25604111/129080503-19135a16-dbba-4581-b7a4-23f5b711d64f.png)
![Companies](https://user-images.githubusercontent.com/25604111/129079948-2121b874-6cab-451d-b7fa-422a6d90466d.png)

**Note:** For some more insights related to Salary and others, please explore the Data Analysis notebook from [here](https://nbviewer.jupyter.org/github/kulkarni-vishwanath/Data-Analysis-Project-From-Scratch/blob/main/Data_Analysis.ipynb). 

I've linked the Jupyter Notebook Viewer version of the Data Analysis file as some of the Plotly Visualizations do not appear in the plain version. 
