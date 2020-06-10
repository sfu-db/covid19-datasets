# Dataset containing Yahoo's COVID - 19 Radiography dataset. 
This [dataset](https://github.com/yahoo/covid-19-data) consists of country, state, and county level information updated on a rolling basis, with updates occuring approximately hourly. The COVID-19 datasets are constructed entirely from primary (government and public agency) sources with a clear attribution of the primary sources used for each geographical region.


**Update Frequency:** Hourly

**Dataset stats:** The data is logically organized by region and time. Time is further organized into a snapshot of the latest updates received for all regions and the updates reported by regions for a given date. There are 17 variables for 176 countries.




### [Codebook](https://raw.githubusercontent.com/yahoo/covid-19-data/master/data/by-region-2020-06-09.json: Column level details for the metadata file.
| Field                   | Type        | Description |
|-------------------------|-------------|-------------|
| regionId                | string  | a unique identifier for the region |
| label                   | string  | the English name of the region |
| totalConfirmed          | integer | the total amount of confirmed cases of COVID-19 in the region until the given date (aggregate) |
| totalDeaths             | integer | the total amount of fatalities from COVID-19 in the region |
| totalRecoveredCases     | integer | the total amount of people recovered from COVID-19 in the region (aggregate) |
| totalTestedCases        | integer | the total amount of people tested for COVID-19 in the region (aggregate) |
| numPositiveTests        | integer | the daily count of people tested positive for COVID-19 |
| numDeaths               | integer | the daily count of fatalities as a result of COVID-19 |
| numRecoveredCases       | integer | the daily count of people recovered from COVID-19 |
| diffNumPositiveTests    | integer | the difference in number of positive cases found between 2 consecutive days |
| diffNumDeaths           | integer | the difference in number of deaths between 2 consecutive days |
| avgWeeklyConfirmedCases | float   | 7-day moving average of daily new confirmed cases |
| avgWeeklyDeaths         | float   | 7-day moving average of daily new deaths |
| referenceDate           | date    | the date associated with the COVID-19 data according to the **local** timezone of the region |
| lastUpdatedDate         | datetime| last update time of the entry |
| dataSource              | anyURI  | the source attribution for the COVID-19 data in the current entry |



### Projects:
-------------
N/A

### License:
-------------
The Yahoo Knowledge Graph COVID-19 Dataset is made available under a [Creative Commons CC-BY-NC 4.0 license](https://creativecommons.org/licenses/by-nc/4.0/legalcode).  No express permission from Verizon Media is required for noncommercial uses.  Only compliance with the CC-BY-NC 4.0 license is required for [noncommercial uses](https://wiki.creativecommons.org/wiki/NonCommercial_interpretation) including attribution.

Verizon Media may consider granting royalty-free commercial licenses upon request.  If you are interested in making commercial use of the Yahoo COVID-19 Dataset, [please submit a request](https://docs.google.com/forms/d/e/1FAIpQLSdINfXR6S0ZmOGSvdvg4WUKzhqvDxltLoa4q4btQ4gkJokTPw/viewform).

### Authors:
-------------
* [Amit Nagpal](https://www.linkedin.com/in/amitnagpal09/)
* [Asaf Ary](https://www.linkedin.com/in/asafary/)
* [Cindy Wang](https://www.linkedin.com/in/cindy-wang-365233/)

Please contact yk-covid-19-os@verizonmedia.com with any questions.
