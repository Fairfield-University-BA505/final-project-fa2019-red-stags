Please use US_Homicide_Full_Report.ipynb, and Presentation_FInal.ipynb for grading

Objectives:
The goal of this report is to learn in detail about the history of US homocides and its trends. Later on the report will focus on 1 district, Hartford County, CT.

Data Source and Content

The Murder Accountability Project is the most complete database of homicides in the United States currently available. This dataset includes murders from the FBI's Supplementary Homicide Report from 1976 to the present and Freedom of Information Act data on more than 22,000 homicides that were not reported to the Justice Department. This dataset includes the age, race, sex, ethnicity of victims and perpetrators, in addition to the relationship between the victim and perpetrator and weapon used.

Source: https://www.kaggle.com/murderaccountability/homicide-reports

Acknowledgements

The data was compiled and made available by the Murder Accountability Project, founded by Thomas Hargrove. 

Dataset Information

The homocide dataset consists of 24 columns and 638,454 rows each. Here are the explanations for each column:
    1. The record ID
        - Sequentially numbers the reports (i.e. 1,2,3...)
    2. Year and Month
        - The year and month of the given report, ranging from year 1980-2014
    3. Incident 
        - How many incidences occured for the specific features (e.i. year, month, perpetrator age...)
    4. Victim Age
        - contains ages of the victims 
    5. Perpetrator Age
        - contains ages of the perpetrators where 0 mean unknown 
    6. Victim Count and Perpertrator Count 
        - start with zero and have a maximum value of 10 
        - tells us about the number of victims and perpetrators involved in a particular incident  
    7. Agency code 
        - is six-digit alphanumeric code used to classify accounts by the federal or non-federal agency. 
        - The alpha part of the code is the parent or major agency. The numeric part of the code identifies the sub-agency.
    8. Agency name
        - Name of the agency handling the case(s)
    9. Agency type 
        - Type of the agency handling the case(s)
    10. City & State 
    11. Victim & Perpetrator sex
        - Male or Female
    12. Victim & Perpetrator ethnicity
        - Unknown, Not Hispanic, Hispanic
    13. Victim & Perpetrator race
        - Native American/Alaska Native, White, Black, Unknown, Asian/Pacific Islander
    14. Relationship
        - Victim of a crime (i.e. Son) 
    15. Crime type
        - Murder or Mansloughter
        - Mansloughter by negligence
    16. Crime solved
        - Whether the crime was solved or not
    17. Weapon
        - The weapon the crime was committed with 
        
Report Steps
This report consists of 4 major parts:
1. Data Exploration
    - Overview and understanding of the data
    - Finding Errors
2. Data Cleaning
    - Clean the data and prepare it for viziulization
    - Expect an extensive cleaning operation
3. Subsetting & viziulization
    - For the US  
4. Decision Trees
    - Encode data
    - Decision tree model
4. Application to a specific scenario
    - Analysis of homicide data for Hartford, Connecticut
    - Hartford Police and education department competing for a fictional $1,000,000 grant to reduce its homicide rate

Python Package Glossary

Pandas- Free software for Python that is used for data manipulation and visualization

Numpy- Is a library for Python that brings high-level mathimatical functions to support arrays and matrices

Matplotlib- Is a 2D plotting library for Python that produces high quailty plots, histograms, power spectra, bar charts, errorcharts, and scatterplots

Seaborn- Is a Python data visualization library based on Matplotlib. We utilized this to make statistical graphs more pleasing to the eye

Missingno- Missingno provides a small toolset of flexible and easy-to-use missing data visualizations and utilities that allows you to get a quick visual summary of the completeness (or lack thereof) of your dataset

sklearn- provides many unsupervised and supervised learning algorithms

IPython- is an interactive command-line terminal for Python. ... In other words, IPython is a powerful interface to the Python language

pydotplus- is an improved version of the old pydot project that provides a Python Interface to Graphviz’s Dot language

What are the different types of firearms used in the data?

Types

Handgun - A weapon designed to fire a small projectile from one or
more barrels when held in one hand with a short stock
designed to be gripped by one hand.

Rifle - A weapon intended to be fired from the shoulder that uses
the energy of the explosive in a fixed metallic cartridge to
fire only a single projectile through a rifled bore for each
single pull of the trigger.

Shotgun - A weapon intended to be fired from the shoulder that uses
the energy of the explosive in a fixed shotgun shell to fire
through a smooth bore either a number of ball shot or a
single projectile for each single pull of the trigger.

Source: https://ucr.fbi.gov/crime-in-the-u.s/2017/crime-in-the-u.s.-2017/topic-pages/offense-definitions