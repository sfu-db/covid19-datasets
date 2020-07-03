# COVID-19 in Spain Dataset

COVID-19 in Spain [dataset](https://www.kaggle.com/danigarci1/covid19-in-spain) maintained by [DATADISTA](https://github.com/datadista/datasets/tree/master/COVID%2019) (in Spanish) provides details on COVID-19 confirmed cases by autonomous community (Spain's first-level political and administrative division) as well as information about health infrastructure (hospital beds) and supplies (face masks).

**Update Frequency:** Approximately weekly.

**Dataset stats:** Comma-separated values (CSV) files. 
* **Format:** .csv 
* **Number of files:** 9
* **Language:** Spanish

**Dataset Profile:** [Pandas-profile for the dataset (generated on: 2020-07-02)](https://sfu-db.github.io/covid19-datasets/webpages/COVID-19-in-Spain-Dataset/). Soon to be replaced with **Dataprep EDA profile**.

### Data Sources:
--------
* [Dataset source (Kaggle)](https://www.kaggle.com/danigarci1/covid19-in-spain).
* [DATADISTA GitHub dataset repository (in Spanish)](https://github.com/datadista/datasets/tree/master/COVID%2019).


### Codebook
--------------

* **nacional_covid19.csv**

National COVID-19 confirmed cases information.

| ID | Column (in Spanish)        | Column (in English)                | Column additional information (if applicable)     | Non-Null Count | Dtype  |     
| --- | --- | --- | --- | --- | --- |
| 0   |`fecha`                        | Publication date						| Publication date. | 126 non-null | object  |
| 1   |`casos_total`                   | Total of confirmed cases | Accumulated total of COVID-19 confirmed cases (sum of PCR and Antibody cases columns). | 91 non-null | float64 |     
| 2   |`casos_pcr`               | Number of PCR cases | Number of COVID-19 cases confirmed by PCR testing. PCR: Polymerase chain reaction test. | 126 non-null | int64 |    
| 3   |`casos_test_ac`                | Number of Antibody cases |  Number of COVID-19 cases confirmed by Antibody testing. | 48 non-null | float64 |    
| 4   |`altas`                      | Number of recoveries	| Number of COVID-19 recoveries. | 71 non-null | float64 |  
| 5   |`fallecimientos`                      | Number of deaths	| Number of COVID-19 deaths. | 114 non-null | float64 |  
| 6   |`ingresos_uci`                      | Number of ICU hospitalizations	| Number of COVID-19 cases that required ICU hospitalization.  | 58 non-null | float64 |  
| 7   |`hospitalizados`                      | Number of hospitalizations	| Total number of COVID-19 cases that required hospitalization (including ICU hospitalizations). | 60 non-null | float64 |  


* **nacional_covid19_rango_edad.csv**

National COVID-19 confirmed cases information per age range.

| ID | Column (in Spanish)        | Column (in English)                | Column additional information (if applicable)     | Non-Null Count | Dtype  |     
| --- | --- | --- | --- | --- | --- |
| 0   |`fecha`                        | Publication date						| Publication date. | 1878 non-null | object  |
| 1   |`rango_edad`                   | Age range | Patients' age range: "0-10", "10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79", and "80 y +" (80 and more). | 1878 non-null | object |     
| 2   |`sexo`               | Gender | Gender: "hombres" (males), "mujeres" (females), "ambos" (both genders). | 1878 non-null | object |    
| 3   |`casos_confirmados`                | Accumulated number of confirmed cases |  Accumulated number of COVID-19 confirmed cases. | 1878 non-null | int64 |    
| 4   |`hospitalizados`                      | Accumulated number of hospitalizations | Accumulated number of COVID-19 cases that required hospitalization. | 1878 non-null | int64 |  
| 5   |`ingresos_uci`                      | Accumulated number of ICU hospitalizations	| Number of COVID-19 cases that required ICU hospitalization.  | 1878 non-null | int64 |  
| 6   |`fallecidos`                      | Accumulated number of deaths	| Accumulated number of COVID-19 deaths. | 1878 non-null | int64 |  


* **ccaa_covid19_altas_long.csv**

Number of COVID-19 recovered cases.

| ID | Column (in Spanish)        | Column (in English)                | Column additional information (if applicable)     | Non-Null Count | Dtype  |     
| --- | --- | --- | --- | --- | --- |
| 0   |`fecha`                        | Publication date						| Publication date. | 1368 non-null | object  |
| 1   |`cod_ine`                        | Autonomous Community code						| Autonomous Community Code according to the following official National Statistics Institute (INE) [table]( https://www.ine.es/daco/daco42/codmun/cod_ccaa.htm). | 1368 non-null | int64  |
| 2   |`CCAA`                   | Autonomous Community name | In Spain, an autonomous community (Spanish: *comunidad autónoma*) is a first-level political and administrative division. | 1368 non-null | object |     
| 3   |`Total`                      | Accumulated recovered cases | Total number of COVID-19 recovered cases.  | 1344 non-null | float64 |  


* **ccaa_covid19_casos_long.csv**

Number of COVID-19 confirmed cases.

| ID | Column (in Spanish)        | Column (in English)                | Column additional information (if applicable)     | Non-Null Count | Dtype  |     
| --- | --- | --- | --- | --- | --- |
| 0   |`fecha`                        | Publication date						| Publication date. | 1729 non-null | object  |
| 1   |`cod_ine`                        | Autonomous Community code						| Autonomous Community Code according to the following official National Statistics Institute (INE) [table]( https://www.ine.es/daco/daco42/codmun/cod_ccaa.htm). | 1729 non-null | int64  |
| 2   |`CCAA`                   | Autonomous Community name | In Spain, an autonomous community (Spanish: *comunidad autónoma*) is a first-level political and administrative division. | 1729 non-null | object |     
| 3   |`Total`                      | Number of confirmed cases | Total number of COVID-19 confirmed cases. | 1729 non-null | int64 |  


* **ccaa_covid19_fallecidos_long.csv**

Number of COVID-19 deceased cases.

| ID | Column (in Spanish)        | Column (in English)                | Column additional information (if applicable)     | Non-Null Count | Dtype  |     
| --- | --- | --- | --- | --- | --- |
| 0   |`fecha`                        | Publication date						| Publication date. | 1558 non-null | object  |
| 1   |`cod_ine`                        | Autonomous Community code						| Autonomous Community Code according to the following official National Statistics Institute (INE) [table]( https://www.ine.es/daco/daco42/codmun/cod_ccaa.htm). | 1558 non-null | int64  |
| 2   |`CCAA`                   | Autonomous Community name | In Spain, an autonomous community (Spanish: *comunidad autónoma*) is a first-level political and administrative division. | 1558 non-null | object |     
| 3   |`Total`                      | Number of deceased cases | Total number of COVID-19 deceased cases. | 1558 non-null | int64 |  


* **ccaa_covid19_hospitalizados_long.csv**

Number of COVID-19 cases that required hospitalization (including ICU hospitalizations).

| ID | Column (in Spanish)        | Column (in English)                | Column additional information (if applicable)     | Non-Null Count | Dtype  |     
| --- | --- | --- | --- | --- | --- |
| 0   |`fecha`                        | Publication date						| Publication date. | 1786 non-null | object  |
| 1   |`cod_ine`                        | Autonomous Community code						| Autonomous Community Code according to the following official National Statistics Institute (INE) [table]( https://www.ine.es/daco/daco42/codmun/cod_ccaa.htm). | 1786 non-null | int64  |
| 2   |`CCAA`                   | Autonomous Community name | In Spain, an autonomous community (Spanish: *comunidad autónoma*) is a first-level political and administrative division. | 1786 non-null | object |     
| 3   |`Total`                      | Number of hospitalization cases | Total number of COVID-19 cases that required hospitalization (including ICU hospitalizations). | 1458 non-null | float64 |  


* **ccaa_covid19_uci_long.csv**

Number of COVID-19 cases that required ICU hospitalization.

| ID | Column (in Spanish)        | Column (in English)                | Column additional information (if applicable)     | Non-Null Count | Dtype  |     
| --- | --- | --- | --- | --- | --- |
| 0   |`fecha`                        | Publication date						| Publication date. | 1786 non-null | object  |
| 1   |`cod_ine`                        | Autonomous Community code						| Autonomous Community Code according to the following official National Statistics Institute (INE) [table]( https://www.ine.es/daco/daco42/codmun/cod_ccaa.htm). | 1786 non-null | int64  |
| 2   |`CCAA`                   | Autonomous Community name | In Spain, an autonomous community (Spanish: *comunidad autónoma*) is a first-level political and administrative division. | 1786 non-null | object |     
| 3   |`Total`                      | Number of ICU hospitalization cases | Total number of COVID-19 cases that required ICU hospitalization. | 1488 non-null | float64 |  


* **ccaa_covid19_mascarillas.csv**

Number of face masks available since 2020-03-10.

| ID | Column (in Spanish)        | Column (in English)                | Column additional information (if applicable)     | Non-Null Count | Dtype  |     
| --- | --- | --- | --- | --- | --- |
| 0   |`fecha`                        | Publication date						| Publication Date | 58 non-null | object  |
| 1   |`cod_ine`                        | Autonomous Community code						| Autonomous Community Code according to the following official National Statistics Institute (INE) [table]( https://www.ine.es/daco/daco42/codmun/cod_ccaa.htm). | 57 non-null | float64  |
| 2   |`CCAA`                   | Autonomous Community name | In Spain, an autonomous community (Spanish: *comunidad autónoma*) is a first-level political and administrative division. | 58 non-null | object |     
| 3   |`mascarillas_acumulado_desde_2020-03-10`                      | Number of face masks available since 2020-03-10  | Number of face masks available since 2020-03-10. | 58 non-null | int64 |  


* **ccaa_camas_uci_2017.csv**

As of 2017, number of ICU (Intensive Care Unit) beds per autonomous community (first-level political and administrative division in Spain).

| ID | Column (in Spanish)        | Column (in English)                | Column additional information (if applicable)     | Non-Null Count | Dtype  |     
| --- | --- | --- | --- | --- | --- |
| 0   |`cod_ine`                        | Autonomous Community code						| Autonomous Community Code according to the following official National Statistics Institute (INE) [table]( https://www.ine.es/daco/daco42/codmun/cod_ccaa.htm). | 17 non-null | int64  |
| 1   |`CCAA`                   | Autonomous Community name | In Spain, an autonomous community (Spanish: *comunidad autónoma*) is a first-level political and administrative division. | 17 non-null | object |     
| 2   |`Públicos`               | Number of public ICU beds | Number of ICU beds in public hospitals.  | 17 non-null | int64 |    
| 3   |`Privados`                | Number of private ICU beds	|  Number of ICU beds in private hospitals. | 17 non-null | int64 |    
| 4   |`Total`                      | Total of ICU beds	| Total number of ICU beds in the autonomous community. | 17 non-null | int64 |  

### Projects:
-------------
* [Dataset source (Kaggle)](https://www.kaggle.com/danigarci1/covid19-in-spain).
* [DATADISTA GitHub dataset repository (in Spanish)](https://github.com/datadista/datasets/tree/master/COVID%2019).

### License:
-------------
Please cite: [DATADISTA GitHub dataset repository (in Spanish)](https://github.com/datadista/datasets/tree/master/COVID%2019).

### Authors:
-------------
[DATADISTA (in Spanish)](https://github.com/datadista/datasets/tree/master/COVID%2019).
  