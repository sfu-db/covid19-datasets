# Summary of the COVID-19 Open Research Dataset Challenge (CORD-19)
An AI challenge with AI2, CZI, MSR, Georgetown, NIH & The White House. 

_This is Kaggle dataset, hence it is highly recommended to have a Kaggle account._

This freely available [dataset](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) is provided to the global research community to apply recent advances in natural language processing and other AI techniques to generate new insights in support of the ongoing fight against this infectious disease. There is a growing urgency for these approaches because of the rapid acceleration in new coronavirus literature, making it difficult for the medical research community to keep up.

**Update Frequency:** Updated frequently - no set frequency

**Dataset stats:** 63, 000 scholarly articles (including 51,000 with full text about COVID-19, SARS-CoV-2, and related coronaviruses). The download size is about 9 GB.

### Data Sources:
--------
This dataset was created by the Allen Institute for AI in partnership with the Chan Zuckerberg Initiative, Georgetown University’s Center for Security and Emerging Technology, Microsoft Research, and the National Library of Medicine - National Institutes of Health, in coordination with The White House Office of Science and Technology Policy


### Codebook
------------
1) Metadata for papers from these sources are combined: CZI, PMC, BioRxiv/MedRxiv. (total records 29500)
	- CZI 1236 records
	- PMC 27337
	- bioRxiv 566
	- medRxiv 361
2) 17K of the paper records have PDFs and the hash of the PDFs are in 'sha'
3) For PMC sourced papers, one paper's metadata can be associated with one or more PDFs/shas under that paper - a PDF/sha correponding to the main article, and possibly additional PDF/shas corresponding to supporting materials for the article.
4)	13K of the PDFs were processed with fulltext ('has_full_text'=True)
5) Various 'keys' are populated with the metadata:
	- 'pmcid': populated for all PMC paper records (27337 non null)
	- 'doi': populated for all BioRxiv/MedRxiv paper records and most of the other records (26357 non null)
	- 'WHO #Covidence': populated for all CZI records and none of the other records (1236 non null)
	- 'pubmed_id': populated for some of the records
	- 'Microsoft Academic Paper ID': populated for some of the records


### Projects:
-------------
The entire dataset is available on Kaggle 

### License:
-------------
Licenses for each dataset can be found in the file `all_sources_metadata csv` file

### Authors:
-------------
Datset Owner: Allen Institute For AI
Collaborators: Peijen Lin, Paul Mooney, Carissa Schoenick, Sebastian Kohlmeier, devrishi, Timo Bozsolikm,Ben Hamner.
