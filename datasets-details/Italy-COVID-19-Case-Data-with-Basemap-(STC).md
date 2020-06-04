# Summary of Italy COVID-19 Case Data with Basemap (STC):
This [dataset](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/4Z8ZKI) contains case data from 02-24-2020 to 05-31-2020, this data repository stores COVID-19 virus case data for Italy, including daily case data, summary data, and base map. Each zip file contains weekly case data from Monday to Sunday.

**Update Frequency:** No specified freqency (most probably weekly).

**Dataset stats:** :
*14 .rar files for weekly data, each has size around 4KB
*3 .csv fils for summary data, each has size 5-10KB
*2 files for basemap with size 8.5MB and 4.6MB




### Data Sources:
--------
NSF Spatiotemporal Innovation Center (NSF Spatiotemporal Innovation Center)

### Codebook
--------------
The data columns for the weekly data are as follows:

| #  | Column           |    Column Description             | Dtype    |
|---  |------           |    --------------                 | -----    |
| 0   |Region           |    The name for the region         | string   |
| 1   |hasc             |    This will represent the Hierarchical administrative subdivision codes(HASC) for admin 1 level | string   |
| 2   |confirmed        |    The number of confirmed cases  |integer   |
| 3   |death            |    The number of death cases       |integer   |
| 4   |recovered        |    The number of recovered cases     |integer   |

The data columns for the summary data are as follows:

| #  | Column           |    Column Description             | Dtype    |
|---  |------           |    --------------                 | -----    |
| 0   |hasc             |     This will represent the Hierarchical administrative subdivision codes(HASC) for admin 1 level | string   |
| 1   |Region            |    The name of the region          |string   |
| 2   |date             |   The date representing the current day in which the data represents UTC time is used for this dataset|object    |


### Projects:
-------------
The related publications to this dataset:
Yang, C., Sha, D., Liu, Q., Li, Y., Lan, H., Guan, W.W., Hu, T., Li, Z., Zhang, Z., Thompson, J.H. and Wang, Z., 2020. Taking the pulse of COVID-19: A spatiotemporal perspective. arXiv preprint arXiv:2005.04224. arXiv: 2005.04224.
### License:
-------------
Please refer to the [page](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/4Z8ZKI&version=3.0)

### Authors:
-------------
NSF Spatiotemporal Innovation Center (NSF Spatiotemporal Innovation Center)
