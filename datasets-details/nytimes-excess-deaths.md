# Summary of New York Times dataset of excess deaths during the Coronavirus pandemic
The [excess deaths dataset](https://github.com/nytimes/covid-19-data/tree/master/excess-deaths) documents the number of deaths from all causes that have occurred during the Coronavirus pandemic for 24 countries. The totals in this data include deaths from Covid-19 as well as those from other causes, likely including people who could not be treated or did not seek treatment for other conditions.

**Update Frequency:** weekly.
**Dataset stats:** One CSV file of 271 KB.

**Dataset Profile:** [Pandas-profile for the dataset](https://sfu-db.github.io/covid19-datasets/webpages/nytimes-excess-deaths.html)

### Data Sources:
--------
National and municipal health departments, Vital statistics offices and other official sources

### Codebook
--------------

The data columns for the file are as follows:

| #  | Column           		| Description    |
| ---| ------				| ------------	 |
| 0   |deaths               	|    The total number of confirmed deaths recorded from any cause.  |
| 1   |expected_deaths          |     The baseline number of expected deaths, calculated from a historical average. See expected deaths.   |
| 2   |excess_deaths            |    The number of deaths minus the expected deaths.    |
| 3   |frequency 				| Weekly or monthly, depending on how the data is recorded.    |
| 4   |start_date               | The first date included in the period.     |
| 5   |end_date                 | The last date included in the period.      |
| 6   |month           			| Numerical month.      |
| 7   |week           			| Epidemiological week, which is a standardized way of counting weeks to allow for year-over-year comparisons. Most countries start epi weeks on Mondays, but others vary.      |
| 8   |baseline            		| The years used to calculate expected_deaths.      |


### Projects:
-------------
New York Times has used this data to create [graphics tracking the outbreak’s toll](https://www.nytimes.com/interactive/2020/04/21/world/coronavirus-missing-deaths.html) with the dataset.

### License:
-------------
The data is publicly available for broad, noncommercial public use including by medical and public health researchers, policymakers, analysts and local news media. 
* If you use this data, you must attribute it to “The New York Times” in any publication. If you would like a more expanded description of the data, you could say “Data from The New York Times, based on reports from national and municipal health agencies.”
* If you use it in an online presentation, we would appreciate it if you would link to our graphic tracking these deaths https://www.nytimes.com/interactive/2020/04/21/world/coronavirus-missing-deaths.html.
* If you use this data, please let us know at covid-data@nytimes.com.

More information about usage of content can be found at [nytimes github page](https://github.com/nytimes/covid-19-data/tree/master/excess-deaths)

### Authors:
-------------
Data Collection Leads: Allison McCann and Jin Wu.
