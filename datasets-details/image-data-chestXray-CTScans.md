# Dataset containing COVID - 19 image data based upon chest X-ray and CT Scans of patients. 
The following summary is based upon Joseph Paul Cohen's [github repo](https://github.com/ieee8023/covid-chestxray-dataset) to build a public open dataset that contains open dataset of chest X-ray and CT images of patients which are positive or suspected of COVID-19 or other viral and bacterial pneunomias (MERS, SARS and ARDS).


**Update Frequency:** No set frequency (it is an open dataset where people contribute)

**Dataset stats:** Images related to 373 patients. Contains a metadata file with patient details.




### [Codebook](https://github.com/ieee8023/covid-chestxray-dataset/blob/master/metadata.csv): Column level details for the metadata file.
|# | Column |  Non-Null Count |  Dtype | 
| ------  |-------------- | ----- | -------|
|0|patientid   |               372 non-null   | int64 |
|1 |  offset   |               276 non-null   | float64 |
| 2 |  sex      |               329 non-null   | object |
|3  | age       |              318 non-null    |float64 |
| 4 |  finding  |               372 non-null   | object | 
| 5 |  survival |               116 non-null   | object |
| 6 |  intubated|               72 non-null    | object |
| 7 |  intubation_present |     77 non-null    | object |
| 8 |  went_icu           |     35 non-null    | object |
| 9 |  in_icu             |    7 non-null      |object  |
| 10|  needed_supplemental_O2 | 12 non-null    | object |
| 11|  extubated              | 23 non-null    | object |
| 12|  temperature            | 35 non-null    | float64|
| 13|  pO2_saturation         | 44 non-null    | float64|
| 14|  leukocyte_count       |  11 non-null    | float64|
 |15 | neutrophil_count      |  2 non-null     | float64|
| 16  |lymphocyte_count      |  10 non-null  |   float64|
| 17|  view                    |372 non-null   | object |
| 18|  modality               | 372 non-null  |  object |
| 19|  date                   | 291 non-null  |  object |
| 20|  location               | 254 non-null  |  object |
 |21 | folder                 | 372 non-null  |  object |
 |22 | filename              |  372 non-null   | object |
| 23 | doi                    |104 non-null   | object |
 |24 | url                   |  372 non-null  |  object |
| 25 | license                | 206 non-null   | object |
| 26 | clinical_notes         | 362 non-null   | object |
| 27 | other_notes            | 234 non-null   | object |
| 28 | Unnamed: 28            | 4 non-null     | object |


### Metadata column [description](https://github.com/ieee8023/covid-chestxray-dataset/blob/master/SCHEMA.md) : 

Following is a list of each metadata field with explanations:

| Column Name | Description |
|------|-----|
| patientid | Internal identifier |
| offset | Number of days since the start of symptoms or hospitalization for each image. If a report indicates "after a few days", then 5 days is assumed. This is very important to have when there are multiple images for the same patient to track progression. |
| sex | Male (M), Female (F), or blank |
| age | Age of the patient in years |
| finding | Type of pneumonia |
| survival | Yes (Y) or no (N) or blank if unknown|
| intubated | Yes (Y) if the patient was intubated (or ventilated) at any point during this illness or No (N) or blank if unknown. |
| went_icu | Yes (Y) if the patient was in the ICU (intensive care unit) or CCU (critical care unit) at any point during this illness or No (N) or blank if unknown.|
| needed_supplemental_O2 | Yes (Y) if the patient required supplemental oxygen at any point during this illness or No (N) or blank if unknown |
| extubated | Yes (Y) if the patient was successfully extubated or No (N) or blank if unknown |
| temperature | Temperature of the patient in Celsius at the time of the image|
| pO2 saturation | partial pressure of oxygen saturation in % at the time of the image |
| wbc count | white blood cell count in units of 10^3/uL at the time of the image |
| neutrophil count | neutrophil cell count in units of 10^3/uL at the time of the image |
| lymphocyte count | lymphocyte cell count in units of 10^3/uL at the time of the image |
| view | Posteroanterior (PA), Anteroposterior (AP), AP Supine (APS), or Lateral (L) for X-rays; Axial or Coronal for CT scans |
| modality | CT, X-ray, or something else |
| date | Date on which the image was acquired |
| location | Hospital name, city, state, country |
| filename | Name with extension |
| doi | Digital object identifier ([DOI](https://en.wikipedia.org/wiki/Digital_object_identifier)) of the research article |
| url | URL of the paper or website where the image came from |
| license | License of the image such as CC BY-NC-SA. Blank if unknown |
| clinical notes | Clinical notes about the image and/or the patient |
| other notes | e.g. credit |



### Projects:
-------------
Please feel free to add any projects you find that build using on the [github repo](https://github.com/ieee8023/covid-chestxray-dataset) .

### License:
-------------
Contact : [Joseph Paul Cohen. Postdoctoral Fellow, Mila, University of Montreal](https://josephpcohen.com/w/)

### Authors:
-------------
[Joseph Paul Cohen. Postdoctoral Fellow, Mila, University of Montreal](https://josephpcohen.com/w/)
