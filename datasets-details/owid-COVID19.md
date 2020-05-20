## Data on COVID-19 (coronavirus) by Our World in Data. 

This [COVID-19 dataset](https://github.com/owid/covid-19-data/tree/master/public/data) is a collection of the COVID-19 data maintained by **_Our World in Data_**. This includes data on confirmed cases, deaths, and testing, as well as other variables of potential interest.

**Update Frequency:** Updated daily.

**Dataset stats:** 16801 rows (as of May 11, 2020). More details regarding the column details are given below in the Codebook section.

**Dataset Profile:** [Pandas-profile for the dataset](https://sfu-db.github.io/covid19-datasets/webpages/owiddataset.html). Soon to be replaced with **Dataprep EDA profile**.



### **Data Sources:**
--------
 1) **Confirmed cases and deaths:** Data comes from the [European Centre for Disease Prevention and Control (ECDC)](https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide)
 2) **Testing for COVID-19:** Data is collected by the Our World in Data team from official reports; you can find the source information for every country and further details in the [post](https://ourworldindata.org/coronavirus-testing) on COVID-19 testing. The testing dataset is updated around twice a week.
 3) **Confirmed cases and deaths:** Data is collected from a variety of sources (United Nations, World Bank, Global Burden of Disease, etc.)


### [Codebook](https://github.com/owid/covid-19-data/edit/master/public/data/owid-covid-data-codebook.md) for the complete Our World in Data COVID-19 dataset
--------
Column|Description|Source
------|-----------|------
`iso_code`|ISO 3166-1 alpha-3 – three-letter country codes|International Organization for Standardization
`location`|Geographical location|Our World in Data
`date`|Date of observation|Our World in Data
`total_cases`|Total confirmed cases of COVID-19|European Centre for Disease Prevention and Control
`new_cases`|New confirmed cases of COVID-19|European Centre for Disease Prevention and Control
`total_deaths`|Total deaths attributed to COVID-19|European Centre for Disease Prevention and Control
`new_deaths`|New deaths attributed to COVID-19|European Centre for Disease Prevention and Control
`total_cases_per_million`|Total confirmed cases of COVID-19 per 1,000,000 people|European Centre for Disease Prevention and Control
`new_cases_per_million`|New confirmed cases of COVID-19 per 1,000,000 people|European Centre for Disease Prevention and Control
`total_deaths_per_million`|Total deaths attributed to COVID-19 per 1,000,000 people|European Centre for Disease Prevention and Control
`new_deaths_per_million`|New deaths attributed to COVID-19 per 1,000,000 people|European Centre for Disease Prevention and Control
`total_tests`|Total tests for COVID-19|European Centre for Disease Prevention and Control
`new_tests`|New tests for COVID-19|European Centre for Disease Prevention and Control
`total_tests_per_thousand`|Total tests for COVID-19 per 1,000 people|National government reports
`new_tests_per_thousand`|New tests for COVID-19 per 1,000 people|National government reports
`tests_units`|Units used by the location to report its testing data|National government reports
`population`|Population in 2020|United Nations, Department of Economic and Social Affairs, Population Division, World Population Prospects: The 2019 Revision
`population_density`|Number of people divided by land area, measured in square kilometers, most recent year available|World Bank – World Development Indicators, sourced from Food and Agriculture Organization and World Bank estimates
`median_age`|Median age of the population, UN projection for 2020|UN Population Division, World Population Prospects, 2017 Revision
`aged_65_older`|Share of the population that is 65 years and older, most recent year available|World Bank – World Development Indicators, based on age/sex distributions of United Nations Population Division's World Population Prospects: 2017 Revision
`aged_70_older`|Share of the population that is 70 years and older in 2015|United Nations, Department of Economic and Social Affairs, Population Division (2017), World Population Prospects: The 2017 Revision
`gdp_per_capita`|Gross domestic product at purchasing power parity (constant 2011 international dollars), most recent year available|World Bank – World Development Indicators, source from World Bank, International Comparison Program database
`extreme_poverty`|Share of the population living in extreme poverty, most recent year available since 2010|World Bank – World Development Indicators, sourced from World Bank Development Research Group
`cvd_death_rate`|Death rate from cardiovascular disease in 2017|Global Burden of Disease Collaborative Network, Global Burden of Disease Study 2017 Results
`diabetes_prevalence`|Diabetes prevalence (% of population aged 20 to 79) in 2017|World Bank – World Development Indicators, sourced from International Diabetes Federation, Diabetes Atlas
`female_smokers`|Share of women who smoke, most recent year available|World Bank – World Development Indicators, sourced from World Health Organization, Global Health Observatory Data Repository
`male_smokers`|Share of men who smoke, most recent year available|World Bank – World Development Indicators, sourced from World Health Organization, Global Health Observatory Data Repository
`handwashing_facilities`|Share of the population with basic handwashing facilities on premises, most recent year available|United Nations Statistics Division
`hospital_beds_per_100k`|Hospital beds per 100,000 people, most recent year available since 2010|OECD, Eurostat, World Bank, national government records and other sources



### License:
-------------
The information on this page is summarized from [OWID's COVID-19 github page](https://github.com/owid/covid-19-data/tree/master/public/data). All of _Our World in Data_ is completely open access and all work is licensed under the Creative Commons BY license. More information about the usage of content can be found [OWID github page](https://github.com/owid/covid-19-data/tree/master/public/data).


### Authors:
-------------
OWID's COVID19 github page the data has been collected, aggregated, and documented by Diana Beltekian, Daniel Gavrilov, Joe Hasell, Bobbie Macdonald, Edouard Mathieu, Esteban Ortiz-Ospina, Hannah Ritchie, Max Roser.
