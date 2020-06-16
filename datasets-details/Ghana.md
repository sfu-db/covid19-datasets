# Dataset containing Ghana's COVID-19 dataset. 
The [dataset](https://github.com/sammyhawkrad/ghana-covid-19-dataset) covers the COVID-19 datset in Ghana. The data available in the dataset comes from updates given by the Ghana Health Service, the Ministry of Information and the Ghana Statistical Service.

**Update Frequency:** Daily

**Dataset stats:** oOne .csv file with size up to 167KB. Contains 8 columns and currently 73 rows (June 15, 2020)

## Data Sources / Disclaimer:
--------
Although the data were found using the Ghana Health Service and Ghana Statistical Service web sites and have been produced and processed from sources believed to be reliable, no warranty, expressed or implied, is made regarding accuracy, adequacy, completeness, legality, reliability or usefulness of any information. This disclaimer applies to both isolated and aggregate uses of the information. The information is provided on an "as is" basis. All warranties of any kind, express or implied, including but not limited to the implied warranties of merchantability, fitness for a particular purpose, freedom from contamination by computer viruses and non-infringement of proprietary rights are disclaimed.

## Column level details for the Ghana_Covid19_DailyActive.csv file.
---------

| #  | Column  | Non-Null Count | Dtype |
--- | ------   |-------------- | ----- |
 0  | Confirmed        |60  non-null | object|
 1   |Recovered|40  non-null | object|
 2   |Death  |6  non-null | object|
 3   |Date|73  non-null | object|
 4  | Cumulative_Confirmed| 73 non-null  | object|
 5  | Cumulative_Recovered| 46  non-null  | object|
 6  | Cumulative_Death| 29  non-null  | object|
 7 | Active Cases| 72  non-null  | object|


More info on the columns of the dataset are given below:

Number of columns = 8

  &nbsp;&nbsp;&nbsp;&nbsp; `confirmed` - total number of confirmed positve cases in a given day

  &nbsp;&nbsp;&nbsp;&nbsp; `recovered` - total number of people who recovered from the virus in a given day

  &nbsp;&nbsp;&nbsp;&nbsp; `death`     - total number of people who died from the virus in a given day

  &nbsp;&nbsp;&nbsp;&nbsp; `date`      - day on which confirmed, recovered and death were reported

  &nbsp;&nbsp;&nbsp;&nbsp; `cumulative_confirmed`  - cumulative count of confirmed positive cases 

  &nbsp;&nbsp;&nbsp;&nbsp; `cumulative_recovered`  - cumulative count of people who have recovered from the virus
 
  &nbsp;&nbsp;&nbsp;&nbsp; `cumulative_death`      - cumulative count of people who have died from the virus

  &nbsp;&nbsp;&nbsp;&nbsp; `active_cases`          - total number of existing positive cases on a given day
                           (active_cases = cumulative_confirmed - cumulative_recovered - cumulative_death)

### Projects:
-------------
N/A

### License:
-------------
The Ghana Knowledge Graph COVID-19 Dataset is made available under a [Creative Commons CC-BY-NC 4.0 license](https://creativecommons.org/licenses/by/4.0/). 
### Authors:
-------------
* [Samuel Darkwah Manu](https://github.com/sammyhawkrad)
