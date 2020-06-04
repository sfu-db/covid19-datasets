# ECDC-COVID-19-dataset
The [dataset](https://data.europa.eu/euodp/en/data/dataset/covid-19-coronavirus-data) contains the latest available public data on COVID-19 including a daily situation update, the epidemiological curve and the global geographical distribution (EU/EEA and the UK, worldwide).

**Update Frequency:** Daily

**Dataset stats:** A csv file which contains 21129 rows and 11 columns (as of June 3, 2020)

**Dataset Profile:** [Link](../webpages/ECDC-COVID-19.html)

### Data Sources:
--------
 ECDC’s Epidemic Intelligence team of epidemiologists screens up to 500 relevant sources to collect the latest figures. The data screening is followed by ECDC’s standard epidemic intelligence process for which every single data entry is validated and documented in an ECDC database.

### Codebook
--------------
| # |  Column                 |  Non-Null Count | Dtype  
|---|------                   |--------------   |-----  
| 0 |  dateRep                |  21338 non-null | object 
| 1 |  day                    |  21338 non-null | int64  
| 2 |  month                  |  21338 non-null | int64  
| 3 |  year                   |  21338 non-null | int64  
| 4 |  cases                  |  21338 non-null | int64  
| 5 | deaths                  | 21338 non-null  | int64  
| 6 |  countriesAndTerritories|  21338 non-null | object 
| 7 |  geoId                  |  21256 non-null | object 
| 8 |  countryterritoryCode   |  21038 non-null | object 
| 9 |  popData2018            |  21027 non-null | float64
| 10 | continentExp           | 21338 non-null  | object 

### Projects:
-------------
N/A

### License:
-------------
N/A

### Authors:
-------------
[European Centre for Disease Prevention and Control](https://data.europa.eu/euodp/en/data/publisher/ecdc)