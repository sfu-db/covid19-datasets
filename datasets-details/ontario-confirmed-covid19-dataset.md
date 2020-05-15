# Summary for dataset of confirmed positive cases of COVID-19 in Ontario
This [dataset](https://data.ontario.ca/dataset/confirmed-positive-cases-of-covid-19-in-ontario) compiles daily snapshots of publicly reported data on 2019 Novel Coronavirus (COVID-19) testing in Ontario.


**Update Frequency:** Daily

**Dataset stats:** 21494 rows (as of May 14, 2020). Column details is given in Codebook section.

### Data Sources:
--------
1) The data for this report were based on information extracted from the Ontario Ministry of Health (MOH) integrated Public Health Information System (iPHIS) database at 4 p.m.
2) iPHIS is a dynamic disease reporting system, which allows ongoing updates to data previously entered. As a result, data extracted from iPHIS represent a snapshot at the time of extraction and may differ from previous or subsequent reports.


### Codebook
------------
This dataset includes:
* **Patient ages and gender**
* **Transmission type**
* **Patient status**
* **Date reported**
* **Public Health Unit Locations (address, Postal Code, Latitude, Longitude)**
 
The following tables provides more details on column data.

|#  | Column                     | Non-Null Count  | Dtype   |
 |---  | ------                   |   --------------  | -----   |
 | 0   |Row_ID                    | 21494 non-null  |int64  |
 |1   |Accurate_Episode_Date      |21494 non-null  |object |
 |2   |Age_Group                  |21494 non-null  |object |
 |3   |Client_Gender              |21494 non-null  |object |
 |4   |Case_AcquisitionInfo       |21494 non-null  |object |
 |5   |Outcome1                   |21494 non-null  |object |
 |6   |Reporting_PHU              |21494 non-null  |object |
 |7   |Reporting_PHU_Address      |21494 non-null  |object |
 |8   |Reporting_PHU_City         |21494 non-null  |object |
 |9   |Reporting_PHU_Postal_Code  |21494 non-null  |object |
 |10  |Reporting_PHU_Website      |21494 non-null  |object |
 |11  |Reporting_PHU_Latitude     |21494 non-null  |float64|
 |12  |Reporting_PHU_Longitude    |21494 non-null  |float64|


### Projects:
-------------
No projects (as of May 14, 2020). Please free to add projects related to this dataset

### License:
-------------
[Open Government Licence – Ontario](https://www.ontario.ca/page/open-government-licence-ontario)

### Authors:
-------------
Ontario's Open Data Team ([opengov@ontario.ca](mailto:opengov@ontario.ca))
