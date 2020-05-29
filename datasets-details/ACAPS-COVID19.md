# Summary of ACAPS COVID-19: Government Measures Dataset
This [dataset](https://data.humdata.org/dataset/acaps-covid19-government-measures-dataset) puts together all the measures implemented by the governments worldwide in reponse to the Coronavirus pandemic. The researched information falls into the following five categories:
 * Social Distancing
 * Movement Restrictions
 * Public Health Measures
 * Social and economic measures
 * Lockdowns

**Update Frequency:** No specified freqency (most probably everyday).

**Dataset stats:** one .xlsx excel file of about 3.4mb.

**Dataset Profile:** [Pandas-profile for the dataset](https://sfu-db.github.io/covid19-datasets/webpages/acaps-dataset.html). Soon to be replaced with **Dataprep EDA profile**.


### Data Sources:
--------
ACAPS team consulted government, media, United Nations, and other organisations sources.


### Codebook
--------------
The data columns for the file are as follows:

| #  | Column           |    Non-Null Count  | Dtype    |     
|---  |------           |    --------------  | -----    |     
| 0   |ID               |    12011 non-null  | float64  |     
| 1   |COUNTRY          |     12011 non-null | object   |     
| 2   |ISO              |    12011 non-null  |object    |    
| 3   |ADMIN_LEVEL_NAME |   1278 non-null    |object    |    
| 4   |PCODE              | 0 non-null      |float64     |  
| 5   |REGION             | 12011 non-null  |object      |  
| 6   |LOG_TYPE           | 12011 non-null  |object      |  
| 7   |CATEGORY           | 12011 non-null  |object      |  
| 8   |MEASURE            | 12011 non-null  |object      |  
| 9   |TARGETED_POP_GROUP | 12011 non-null  |object      |  
| 10  |COMMENTS           | 11866 non-null  |object      |  
| 11  |NON_COMPLIANCE     | 10751 non-null  |object      |  
| 12  |DATE_IMPLEMENTED   | 11726 non-null  |datetime64[ns]|
| 13  |SOURCE             | 11989 non-null  |object      |  
| 14  |SOURCE_TYPE        | 11995 non-null  |object      |  
| 15  |LINK               | 11979 non-null  |object      |  
| 16  |ENTRY_DATE         | 12011 non-null  |datetime64[ns]|
| 17  |Alternative source | 1064 non-null   |object |

### Projects:
-------------
ACAPS have created a [dashboard](https://data.humdata.org/dataset/acaps-covid19-government-measures-dataset) with the dataset.

### License:
-------------
[Creative Commons Attribution International](https://data.humdata.org/about/license)

### Authors:
-------------
The ACAPS Team - they can be reached at info@acaps.org  
