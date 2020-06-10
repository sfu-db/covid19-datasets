# Summary of Austria COVID-19 Case Data with Basemap (STC):
This [dataset](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/NGWFTO) contains case data from 03-04-2020 to 05-31-2020, this data repository stores COVID-19 virus case data for Austria, including daily case data, summary data, and base map. Each zip file contains weekly case data from Monday to Sunday.

**Update Frequency:** No specified freqency (most probably weekly).

**Dataset stats:** :
*13 .rar files for weekly data, each has size around 2-3KB
*3 .csv fils for summary data, each has size 3KB
*2 files for basemap with size around 2MB.

**Dataset Profile:** [Pandas-profile for the dataset](https://sfu-db.github.io/covid19-datasets/webpages/Austria_Covid_19.html). Soon to be replaced with **Dataprep EDA profile**.


### Data Sources:
--------
NSF Spatiotemporal Innovation Center (NSF Spatiotemporal Innovation Center)

### Codebook
--------------
The data columns for the weekly data are as follows:

| #  | Column           |    Column Description             | Dtype    |
|---  |------           |    --------------                 | -----    |
| 0   |State           |    The name for the state         | string   |
| 1   |hasc             |    This will represent the Hierarchical administrative subdivision codes(HASC) for admin 1 level | string   |
| 2   |confirmed        |    The number of confirmed cases  |integer   |
| 3   |death            |    The number of death cases       |integer   |
| 4   |recovered        |    The number of recovered cases     |integer   |

The data columns for the summary data are as follows:

| #  | Column           |    Column Description             | Dtype    |
|---  |------           |    --------------                 | -----    |
| 0   |hasc             |     This will represent the Hierarchical administrative subdivision codes(HASC) for admin 1 level | string   |
| 1   |State            |    The name of the state          |string   |
| 2   |date             |   The date representing the current day in which the data represents UTC time is used for this dataset|Date( YYYY/MM/DD) in UTC    |


### Projects:
-------------
The related publications to this dataset:
Yang, C., Sha, D., Liu, Q., Li, Y., Lan, H., Guan, W.W., Hu, T., Li, Z., Zhang, Z., Thompson, J.H. and Wang, Z., 2020. Taking the pulse of COVID-19: A spatiotemporal perspective. arXiv preprint arXiv:2005.04224. arXiv: 2005.04224.
### License:
-------------
Please refer to the [page](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/NGWFTO&version=3.0)

### Authors:
-------------
NSF Spatiotemporal Innovation Center (NSF Spatiotemporal Innovation Center)