# Summary of Brazil COVID-19 Case Data with Basemap (STC):
This [dataset](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/YB2S7D) contains case data from 02-26-2020 to 05-31-2020, this data repository stores COVID-19 virus case data for Brazil, including daily case data, summary data, and base map. Each zip file contains weekly case data from Monday to Sunday.

**Update Frequency:** No specified freqency (most probably weekly).

**Dataset stats:** :
*14 .rar files for weekly data, each has size around 4KB
*3 .csv fils for summary data, each has size 5-10KB
*2 files for basemap with size 17.3MB and 2.4MB

**Dataset Profile:** [Pandas-profile for the dataset](https://sfu-db.github.io/covid19-datasets/webpages/Brazil_Covid_19.html). Soon to be replaced with **Dataprep EDA profile**.


### Data Sources:
--------
NSF Spatiotemporal Innovation Center (NSF Spatiotemporal Innovation Center)

### Codebook
--------------
The data columns for the weekly data are as follows:

| #  | Column           |    Column Description             | Dtype    |
|---  |------           |    --------------                 | -----    |
| 0   |State            |    The name for the state         | string   |
| 1   |hasc             |     This will represent the Hierarchical administrative subdivision codes(HASC) for admin 1 level | string   |
| 2   |confirmed        |    The number of confirmed cases  |integer   |
| 3   |death            |   The number of death cases       |integer   |
| 4   |recovered        | The number of recovered cases     |integer   |

The data columns for the summary data are as follows:

| #  | Column           |    Column Description             | Dtype    |
|---  |------           |    --------------                 | -----    |
| 0   |hasc             |     This will represent the Hierarchical administrative subdivision codes(HASC) for admin 1 level | string   |
| 1   |State            |    The name of the state          |string   |
| 2   |date             |   The date representing the current day in which the data represents UTC time is used for this dataset|object    |


### Projects:
-------------
There are two related publications:
Yang, C., Sha, D., Liu, Q., Li, Y., Lan, H., Guan, W.W., Hu, T., Li, Z., Zhang, Z., Thompson, J.H. and Wang, Z., 2020. Taking the pulse of COVID-19: A spatiotemporal perspective. arXiv preprint arXiv:2005.04224. arXiv: 2005.04224.
Liu, Q., Sha, D., Liu, W., Houser, P., Zhang, L., Hou, R., Lan, H., Flynn, C., Lu, M., Hu, T. and Yang, C., 2020. Spatiotemporal Patterns of COVID-19 Impact on Human Activities and Environment in China Using Nighttime Light and Air Quality Data. arXiv preprint arXiv:2005.02808. 2005.02808.
### License:
-------------
Please refer to the [page](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/YB2S7D&version=3.0)

### Authors:
-------------
NSF Spatiotemporal Innovation Center (NSF Spatiotemporal Innovation Center)