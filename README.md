# Project Name: Instahyre Job Analytics

<p align="center">
  <img src="https://github.com/divyechopra/Instahyre-Job-Analytics/assets/122443219/4d12f489-95e8-48a9-a6fc-4fabdc60c6cd" alt="WhatsApp Video 2023-07-24 at 10 15 43 AM">
</p>

## Introduction

The project's objective is to gather job-related information from Instahyre using Python's Selenium library and organize it in a specified format. The collected data will then be converted into three separate tables: jobs, company, and details, utilizing the Pandas library. To enable user-friendly searches, a search bar will be implemented using the Flask web framework, allowing users to look up skills. The search results will display essential details, such as the most common experience level, industry, and company class where the skill is in demand, along with the number of available job opportunities. To enhance user experience, the FuzzyBuzzy library will be employed to correct any input errors made by users in the search bar.


## Problem Aimed to Solve:

1. Automate the job search process - Save time and effort.
2. Provide comprehensive job details - Rich information for users.
3. Enhance search query accuracy - Improve search results precision.
4. Analyze job market trends - Identify employment patterns and demands.
5. Increase job matching efficiency - Connect candidates with suitable positions.

##  <img src="https://user-images.githubusercontent.com/106439762/181935629-b3c47bd3-77fb-4431-a11c-ff8ba0942b63.gif" width="48" height="48"> **User's Manual**

| Files/Folder        | Description                                                                                   |
|---------------------|-----------------------------------------------------------------------------------------------|
| **Phase - 1**       | Includes the following folders:                                                               |
|                     | **Table creation:** (Creating database tables)                                                  |
|                     | **Data Analysis:** (Analyzing data sets)                                                        |
|                     | **Web Scraping:** (Extracting data from websites).                                              |
| **Phase - 2**       | Includes the following folders:                                                               |
|                     | **App Logics:** (Implementation of application logic.)                                         |
|                     | **Data Preprocessing and Model Creation:** (Data preparation and development of machine learning models.)|
|                     | **App:** (Final application code.)                                                              |


## Data Description

- *Jobs Table*:

Column Name    | Description
---------------|-----------------------------------------------------------
JobID          | Primary key for Jobs table
Designation    | The designation of the job
Industry       | Industry of the company from which the job is
Location       | Location of the job
Skills         | Skills required for the job
DetailID       | A key to map with details table, as every job has some description
CompanyID      | A key to map with company table, as one company can have multiple jobs

- *Company Table:*

Column Name         | Description
--------------------|-------------------------------------------------
CompanyID           | Primary key for Company table
Name                | Name of the company posting the job listings
Founded             | Founded year of the company
Employees           | Total number of employees in the company


- *Details Table:*

Column Name           | Description
----------------------|--------------------------------------------------
DetailID              | Unique identifier for each set of additional details
Skills                | Skills or qualifications required for the job
Involvement           | The nature of involvement in the job
Exp                   | Year of experience needed for the job
HR                    | Name of HR who posted the job
 

## Methodology

The following methodology was used to accomplish the project objectives:

1. _Data Scraping:_ Job data was obtained from Instahyre using Python's Selenium library, considering specific criteria like job titles, locations, and company names.

2. _Data Conversion:_ Utilizing Pandas, the scraped data underwent transformation into three tables: jobs, company, and details.

3. _Data Cleaning and Preparation:_ The data cleaning phase involved eliminating irrelevant data, handling missing values, standardizing formats, removing duplicates, cleaning text, managing outliers, type conversion, consistency checks, categorical data normalization, and ensuring data integrity.

4. _Company Classification:_ Companies were classified into five classes (Class0 to Class4) based on employee count and company age using K-Means clustering. The optimal number of clusters was determined using the Elbow Method.

<p align="center">
  <img src="https://github.com/divyechopra/Instahyre-Job-Analytics/assets/122443219/963ab2b2-0efe-462d-84ce-a27c856594aa" width="500">
</p>

<h5 align=center>
  Elbow Method
</h5>
   
<p align="center">
  <img src="https://github.com/divyechopra/Instahyre-Job-Analytics/assets/122443219/a0208a2f-8b59-4e7c-9d4b-44156d544d79" width="500" length="500">


</p>
 <h5 align=center>
 Scatter Plot of Clusters
 </h5>
   
5. _User-Friendly Interface:_ A Flask web framework introduced a search bar for users to look up skills. FuzzyBuzzy library corrected any input errors. Search results displayed the most common experience level, industry, company class related to the skill, and the number of available job opportunities.

## Results

### 1. This webpage is designed to accept user input.
<p align="center">
  <img width="800" alt="image" src="https://github.com/divyechopra/Instahyre-Job-Analytics/assets/122443219/f71fe8fe-8c48-42cc-a6fe-9116c9e78eb6">
</p>



### 2. The webpage generates output based on the skills searched by the users.

<p align = "center">
<img width="800" alt="image" src="https://github.com/divyechopra/Instahyre-Job-Analytics/assets/122443219/fef38b12-0871-473e-9e3a-fb0b6357eedc">
</p>


### 3. This webpage showcases a comprehensive list of jobs related to specific skills entered by users, along with supplementary information.

<p align = "center" >
  <img width="800" alt="image" src="https://github.com/divyechopra/Instahyre-Job-Analytics/assets/122443219/bf5d54d1-3cff-4a37-abce-5ef8dcc43d83">
</p>

## A short demo video of our app (Deployed on the local host server)


https://github.com/divyechopra/Instahyre-Job-Analytics/assets/122443219/128a105f-8b21-4664-b706-2106456a0a21


## Challenges:

- Creating Webpage with the help of HTML and CSS.
- User Input Text Processing and learning Fuzzy wuzzy.
- Creating a backend with Flask and returning output to a webpage.
- Understanding the different ways to deploy the model.

## References

- Python Software Foundation. (2022). Python Language Reference, version 3.10. Retrieved from https://docs.python.org/3/reference/index.html
  
- Selenium with Python: https://selenium-python.readthedocs.io/
  
- Wikipedia contributors. (2023, April 13). Flask (web framework). In Wikipedia, The Free Encyclopedia. Retrieved 15:48, April 22, 2023, from "https://en.wikipedia.org/wiki/Flask_(web_framework)"

- Scikit-learn developers. (n.d.). Clustering. Retrieved April 22, 2023, from "https://scikit-learn.org/stable/modules/clustering.html"

- FuzzyBuzzy. (n.d.). FuzzyBuzzy Documentation. Retrieved April 22, 2023, from "https://pypi.org/project/fuzzybuzzy/"


