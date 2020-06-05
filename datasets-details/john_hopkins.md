# Johns Hopkins University - COVID-19 Data Repository
This [dataset](https://github.com/CSSEGISandData/COVID-19) contains the daily cases reports received from John Hopkin. It also provides details on geographic locations, incident rates, active cases, case fatality ratio, etc.

**Update Frequency:** Daily

**Dataset stats:** Each report is approximately 500 KB.



### Data Sources:
--------
World Health Organization (WHO): https://www.who.int/

European Centre for Disease Prevention and Control (ECDC): https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases

DXY.cn. Pneumonia. 2020. http://3g.dxy.cn/newh5/view/pneumonia

US CDC: https://www.cdc.gov/coronavirus/2019-ncov/index.html

BNO News: https://bnonews.com/index.php/2020/02/the-latest-coronavirus-cases/

WorldoMeters: https://www.worldometers.info/coronavirus/

1Point3Arces: https://coronavirus.1point3acres.com/en

COVID Tracking Project: https://covidtracking.com/data. 

### Codebook
--------------
This dataset includes:
geographic locations, incident rates, active cases, cate fatality ratio, etc
* **Geographic locations**
* **Incident rates**
* **Active cases**
* **Case fatality ratio**
 
The following tables provides more details on column data.
--------
#|Column|Non-Null Count|Dtype
-|------|--------------|-----
 0 |FIPS|    3027 non-null  | float64
 1 |  Admin2|3031 non-null  | object 
 2|   Province_State|  3471| non-null|   object 
 3|   Country_Region|       3644| non-null|   object 
 4|   Last_Update|          3644| non-null|   object 
 5|   Lat|                 3572| non-null|   float64
 6|   Long_|               3572| non-null|   float64
 7|   Confirmed|            3644| non-null|   int64  
 8|   Deaths|            3644| non-null|   int64  
 9|   Recovered|           3644| non-null|   int64  
 10|  Active|           3644| non-null|   int64  
 11|  Combined_Key|        3644| non-null|   object 
 12|  Incidence_Rate|       3572| non-null|   float64
 13|  Case-Fatality_Ratio|  3588| non-null|   float64

### Projects:
-------------
[Visual Dashboard (desktop)](https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6)

[Visual Dashboard (mobile)](http://www.arcgis.com/apps/opsdashboard/index.html#/85320e2ea5424dfaaa75ae62e5c06e61)

### License:
-------------
The information on this page is summarized from [Johns Hopkins University's COVID-19 github page](https://github.com/CSSEGISandData/COVID-19). 

### Authors:
-------------
Email: jhusystems@gmail.com
  
