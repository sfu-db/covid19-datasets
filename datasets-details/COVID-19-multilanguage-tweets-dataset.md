# COVID-19 Multilanguage Tweets Dataset

Collection of tweets IDs associated with the COVID-19 disease. 

"The [repository](https://github.com/lopezbec/COVID19_Tweets_Dataset) contains an ongoing collection of tweets IDs associated with the novel coronavirus COVID-19. The dataset contains Tweets’ ids dating back to January 22th, 2020. The Twitter’s search API was used to gather historical Tweets from multiple continents in multiple languages that contained a given keyword (i.e., coronavirus, virus, covid, ncov19, ncov2019). In order to comply with Twitter’s Terms of Service, only the Tweet IDs of the Tweets gathered are released for non-commercial research use only."

**Update Frequency:** Approximately weekly.

**Dataset stats:** 

* Tweets’ ids dating back to January 22th, 2020.
* Tweet-ID files are stored in folders that indicate the keyword used (i.e., coronavirus, virus, covid, ncov19, ncov2019).
* The Tweet-ID file is a .txt containing individual Tweet-IDs stored as a comma-separated-list. The file names follow the naming convention of : [Keyword]_yyyy_mm_dd.txt (e.g., coronavirus_2020_01_22.txt contains the ids of tweets mentioning the keyword ‘coronavirus’ tweeted on January 22th, 2020).
* The Tweets_ID_by_language folder contains a series of .txt files with the tweets ID and their language organized by keyword (see Twitter language codes). The file names follow the naming convention of : [mm_dd_yyyy]_[Keyword].txt (e.g., coronavirus>Apr_03_2020_coronavirus, contains tweets id and their language from all the tweets collected on April 3rd, 2020 using the keyword coronavirus).
* Since the Twitter API returns tweets in UTC, all tweet-ID folder and file names are all in UTC as well.
* Language: Multilanguage

Stats and descriptions obtained from the official site: [here](https://github.com/lopezbec/COVID19_Tweets_Dataset)

### Data Sources:
--------
- [COVID-19 Multilanguage Tweets Dataset](https://github.com/lopezbec/COVID19_Tweets_Dataset) 
  Christian Lopez, Malolan Vasu, and Caleb Gallemore (2020) Understanding the perception of COVID-19 policies by mining a multilanguage Twitter dataset. arXiv:cs.SI/2003.10359,2020 https://arxiv.org/abs/2003.10359
- [Twitter, Inc.](https://twitter.com/) 


### Codebook
--------------
- Tweet's files by keyword contain the Tweet ID.
- Tweet's files by language contain the Tweet ID and its language ([see languages list here](https://developer.twitter.com/en/docs/twitter-for-websites/twitter-for-websites-supported-languages/overview) ).

### Projects:
-------------
- Christian Lopez, Malolan Vasu, and Caleb Gallemore (2020) Understanding the perception of COVID-19 policies by mining a multilanguage Twitter dataset. arXiv:cs.SI/2003.10359,2020 https://arxiv.org/abs/2003.10359
- Kaggle's COVID-19 Multilanguage Tweets [Dataset](https://www.kaggle.com/lopezbec/covid19-tweets-dataset) . 

### License:
-------------
This dataset is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International Public License (CC BY-NC-SA 4.0). By using this dataset, you agree to abide by the stipulations in the license, remain in compliance with Twitter’s Terms of Service, and cite the following manuscript:
Christian Lopez, Malolan Vasu, and Caleb Gallemore (2020) Understanding the perception of COVID-19 policies by mining a multilanguage Twitter dataset. arXiv:cs.SI/2003.10359,2020 https://arxiv.org/abs/2003.10359

### Authors:
-------------
[Christian Lopez, Malolan Vasu, and Caleb Gallemore (2020)](https://github.com/lopezbec/COVID19_Tweets_Dataset)  