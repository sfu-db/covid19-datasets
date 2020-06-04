# Dataset Title

This government-generated [dataset](https://www.ins.gov.co/Paginas/Boletines-casos-COVID-19-Colombia.aspx) (in Spanish) compiles daily data of COVID-19 confirmed cases in Colombia (South America). It provides details on confirmed cases, recoveries and deaths by city.

**Update Frequency:** Daily.

**Dataset stats:** Microsoft Excel file named according to its date of generation. It includes current and historical information starting from 03-02-2020.
Format: .xlsx 
Number of columns: 17
Language: Spanish

**Dataset Profile:** [Pandas-profile for the dataset](https://sfu-db.github.io/covid19-datasets/webpages/Colombia-COVID-19-official-dataset.html). Soon to be replaced with **Dataprep EDA profile**.

### Data Sources:
--------
Colombia National Institutute of Health (Instituto Nacional de Salud - INS -)

[Website](http://www.ins.gov.co/Noticias/Paginas/Coronavirus.aspx) 
[Dashboard](https://www.datos.gov.co/Salud-y-Protecci-n-Social/Casos-positivos-de-COVID-19-en-Colombia/gt2j-8ykr/data) 

### Codebook
--------------
The data columns for the file are as follows:

| #   | Column (in Spanish)        | Column (in English)                | Column additional information (if applicable)     | Non-Null Count | Dtype  |     
|---  |------                      | -----                              |                                                   | -------------  | -----  |
| 0   |Caso                        | Case number						|                                                   | 30493 non-null | int64  |
| 1   |Fecha Not                   | Notification date to INS   		|                                                   | 30493 non-null | object |     
| 2   |Código ciudad               | City code						    | City code according to the following table: https://www.datos.gov.co/Mapas-Nacionales/DIVIPOLA-Codigos-municipios/gdxc-w37w/data | 30493 non-null | int64 |    
| 3   |Departamento                | Department (Province/State) name	|                                                   | 30493 non-null | object |    
| 4   |Ciudad                      | City name							|                                                   | 30493 non-null | object |  
| 5   |Edad                        | Age								|                                                   | 30493 non-null | int64  |  
| 6   |Sexo                        | Gender								|                                                   | 30493 non-null | object |  
| 7   |Tipo                        | Case origin type					| "Importado" (Imported): Individual with COVID-19 who arrived in Colombia from overseas; "Relacionado" (Related): Individual who got infected with COVID-19 from contact with an infected person; "En estudio" (Under revision). |	30493 non-null | object |  
| 8   |Ubicación                   | Patient location					| "Casa" (Home); "Fallecido" (Deceased); "Hospital"; "Hospital UCI" (ICU - Intensive care unit); "Recuperado" (Recovered); "N/A": Non-applicable | 30448 non-null | object |  
| 9   |Estado                      | Patient health status				| "Asintomático" (Asymptomatic); "Fallecido" (Deceased); "Grave" (Gravely ill); "Leve" (Slightly ill); "Moderado" (Moderately ill). | 30442 non-null | object |  
| 10  |Pais de procedencia         | Country of origin					|                                                   | 30493 non-null | object |  
| 11  |Fecha de inicio de síntomas | Symptoms start date				|                                                   | 30490 non-null | object |  
| 12  |Fecha de muerte             | Date of death						|                                                   | 1005 non-null  | object |
| 13  |Fecha de diagnóstico        | Date of diagnosis					|                                                   | 30493 non-null | object |  
| 14  |Fecha recuperado            | Date of recovery					|                                                   | 9645 non-null  | object |  
| 15  |Fecha cargue web            | System upload date					|                                                   | 30493 non-null | object |  
| 16  |Tipo de recuperación        | Recovery type						| "PCR": Negative results on a second PCR test. ; "Tiempo":  Asymptomatic patient after thirty days of diagnosis. | 28749 non-null | object |

### Projects:
-------------
Colombian government has created a [dashboard](https://www.datos.gov.co/Salud-y-Protecci-n-Social/Casos-positivos-de-COVID-19-en-Colombia/gt2j-8ykr/data) with this dataset.

### License:
-------------
[Creative Commons Attribution-ShareAlike 4.0 International Public License](https://creativecommons.org/licenses/by-sa/4.0/legalcode)

### Authors:
-------------
[National Institute of Health - Government of Colombia](http://www.ins.gov.co)
  