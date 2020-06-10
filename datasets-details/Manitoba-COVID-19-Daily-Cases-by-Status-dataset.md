# Manitoba COVID-19 – Daily Cases by Status dataset

This [dataset](https://resources-covid19canada.hub.arcgis.com/datasets/6680d7f8277e4f1ab24099f24b93622d_0) contains the most up-to-date daily case status information for confirmed cases of COVID-19 in Manitoba (Canada).

**Update Frequency:** Daily.

**Dataset stats:** Comma-separated values file. It includes current and historical information starting from 03-12-2020.
* Format: .csv (comma-separated values) 
* Number of columns: 7
* Language: English

**Dataset Profile:** [Pandas-profile for the dataset](https://sfu-db.github.io/covid19-datasets/webpages/Manitoba-COVID-19-Daily-Cases-by-Status.html). Soon to be replaced with **Dataprep EDA profile**.

### Data Sources:
--------
[Esri Canada GIS COVID-19 Hub](https://resources-covid19canada.hub.arcgis.com/datasets/6680d7f8277e4f1ab24099f24b93622d_0) 
[Province of Manitoba - COVID-19 site](https://www.gov.mb.ca/covid19/index.html) 

### Codebook
--------------
The data columns for the file are as follows:

| ID | Column | Column additional information | Non-Null Count | Dtype |     
| --- | --- | --- | --- | --- |
| 0   |`Date`| Date for which confirmed and probable COVID-19 cases were reported in the Public Health Information Management System (PHIMS) of Manitoba. | 89 non-null | object  |
| 1   |`Daily_Cases`| Daily case numbers of COVID-19 as reported in PHIMS. | 89 non-null | int64 |     
| 2   |`Cumulative_Cases`| Cumulative daily case numbers of COVID-19 as reported in PHIMS. | 89 non-null | int64 |    
| 3   |`Active_Cases`| Number of active cases of COVID-19, derived by the difference between cumulative daily case numbers and recoveries and deaths. | 87 non-null | float64 |    
| 4   |`Recoveries`| Number of cumulative recoveries by day as reported in PHIMS. | 87 non-null | float64 |  
| 5   |`Deaths`| Cumulative number of fatalities in individuals who were reported as confirmed or probable COVID-19 cases. This field is derived from the Admissions, Discharges, Transfers (ADT) database for in-hospital fatalities, and PHIMS for in-community fatalities. | 87 non-null | float64  |  
| 6   |`ObjectId`| Sequential unique whole numbers that are automatically generated. | 89 non-null | int64 |  

### Projects:
-------------
[COVID-19 Canada GIS Hub - Esri Canada](https://resources-covid19canada.hub.arcgis.com/)

### License:
-------------
[Custom License - Geospatial Open Data - Manitoba](https://gov.mb.ca/sd/pubs/geomb/geospatialopendatalicence.pdf)

### Authors:
-------------
[Esri Canada](https://www.esri.ca/en-ca) 
[Government of Manitoba](https://www.gov.mb.ca/) 
  