# University of Oxford's Dataset on Coronavirus Government Response Tracker
This [dataset](https://www.bsg.ox.ac.uk/research/research-projects/coronavirus-government-response-tracker) is provided by University of Oxford's Blavatik School of Government, it provides systematic information on which governments have taken which measures, and when, can help decision-makers and citizens understand the robustness of governmental responses in a consistent way, aiding efforts to fight the pandemic. The Oxford COVID-19 Government Response Tracker (OxCGRT) systematically collects information on several different common policy responses governments have taken, scores the stringency of such measures, and aggregates these scores into a common Stringency Index.

**Update Frequency:** Usually updated daily.

**Dataset stats:** Mutiple .csv files, column level details are provided in the codebook section.

**Dataset Profile:** Add the link to webpage containing the profile.

### Data Sources:
--------
Data is collected from public sources by a team of over one hundred Oxford University students and staff from every part of the world. Please find more info on the dataset [webpage](https://www.bsg.ox.ac.uk/research/research-projects/coronavirus-government-response-tracker).
### Codebook
--------------
The following codebook is **taken from OxCRT's codebook github page** which can be found [here](https://github.com/OxCGRT/covid-policy-tracker/blob/master/documentation/codebook.md).


***Codebook version 2.2 <br/>22 May 2020***

This document is the authoritative codebook for the Oxford Covid-19 Government Response Tracker ([GitHub repo](https://github.com/OxCGRT/covid-policy-tracker), [university website](https://www.bsg.ox.ac.uk/covidtracker)). The dataset contains 17 indicators and a miscellaneous notes field organised into four groups:
- [C - containment and closure policies](#containment-and-closure-policies)
- [E - economic policies](#economic-policies)
- [H - health system policies](#health-system-policies)
- [M - miscellaneous policies](#miscellaneous-policies)

Updates to this codebook are recorded in the [changelog](#codebook-changelog) below.

Most indicators are recorded on an ordinal scale that represents the level of strictness of the policy. Four of the indicators (E3, E4, H4 and H5) are recorded as a US dollar value of fiscal spending.

Eight of the indicators (C1-C7 and H1) also have a flag for whether they are targeted to a specific geographical region (flag=0) or whether they are a "general" policy that is applied across the whole country (flag=1). One indicator (E1) has a flag to describe whether income support is for just formal sector workers (flag=0) or whether it includes informal workers as well (flag=1).

### Containment and closure policies

| ID | Name | Description | Measurement | Coding |
| --- | --- | --- | --- | --- |
| C1 | `C1_School closing` | Record closings of schools and universities | Ordinal scale | 0 - no measures <br/>1 - recommend closing <br/>2 - require closing (only some levels or categories, eg just high school, or just public schools) <br/>3 - require closing all levels <br/>Blank - no data |
| | `C1_Flag` | | Binary flag for geographic scope | 0 - targeted <br/>1- general <br/>Blank - no data |
| C2 | `C2_Workplace closing` | Record closings of workplaces | Ordinal scale | 0 - no measures <br/>1 - recommend closing (or recommend work from home) <br/>2 - require closing (or work from home) for some sectors or categories of workers <br/>3 - require closing (or work from home) for all-but-essential workplaces (eg grocery stores, doctors) <br/>Blank - no data |
| | `C2_Flag` | | Binary flag for geographic scope | 0 - targeted <br/>1- general <br/>Blank - no data |
| C3 | `C3_Cancel public events` | Record cancelling public events | Ordinal scale | 0 - no measures <br/>1 - recommend cancelling <br/>2 - require cancelling <br/>Blank - no data |
| | `C3_Flag` | | Binary flag for geographic scope | 0 - targeted <br/>1- general <br/>Blank - no data |
| C4 | `C4_Restrictions on gatherings` | Record limits on private gatherings | Ordinal scale | 0 - no restrictions <br/>1 - restrictions on very large gatherings (the limit is above 1000 people) <br/>2 - restrictions on gatherings between 101-1000 people <br/>3 - restrictions on gatherings between 11-100 people <br/>4 - restrictions on gatherings of 10 people or less <br/>Blank - no data |
| | `C4_Flag` | | Binary flag for geographic scope | 0 - targeted <br/>1- general <br/>Blank - no data |
| C5 | `C5_Close public transport` | Record closing of public transport | Ordinal scale | 0 - no measures <br/>1 - recommend closing (or significantly reduce volume/route/means of transport available) <br/>2 - require closing (or prohibit most citizens from using it) <br/>Blank - no data |
| | `C5_Flag` | | Binary flag for geographic scope | 0 - targeted <br/>1- general <br/>Blank - no data |
| C6 | `C6_Stay at home requirements` | Record orders to "shelter-in-place" and otherwise confine to the home | Ordinal scale | 0 - no measures <br/>1 - recommend not leaving house <br/>2 - require not leaving house with exceptions for daily exercise, grocery shopping, and 'essential' trips <br/>3 - require not leaving house with minimal exceptions (eg allowed to leave once a week, or only one person can leave at a time, etc) <br/>Blank - no data |
| | `C6_Flag` | | Binary flag for geographic scope | 0 - targeted <br/>1- general <br/>Blank - no data |
| C7 | `C7_Restrictions on internal movement` | Record restrictions on internal movement between cities/regions | Ordinal scale | 0 - no measures <br/>1 - recommend not to travel between regions/cities <br/>2 - internal movement restrictions in place <br/>Blank - no data |
| | `C7_Flag` | | Binary flag for geographic scope | 0 - targeted <br/>1- general <br/>Blank - no data |
| C8 | `C8_International travel controls` | Record restrictions on international travel <br/><br/>Note: this records policy for foreign travellers, not citizens | Ordinal scale | 0 - no restrictions <br/>1 - screening arrivals <br/>2 - quarantine arrivals from some or all regions <br/>3 - ban arrivals from some regions <br/>4 - ban on all regions or total border closure <br/>Blank - no data |

### Economic policies

| ID | Name | Description | Measurement | Coding |
| --- | --- | --- | --- | --- |
| E1 | `E1_Income support` <br/>(for households) | Record if the government is providing direct cash payments to people who lose their jobs or cannot work. <br/><br/>Note: only includes payments to firms if explicitly linked to payroll/salaries | Ordinal scale | 0 - no income support <br/>1 - government is replacing less than 50% of lost salary (or if a flat sum, it is less than 50% median salary) <br/>2 - government is replacing 50% or more of lost salary (or if a flat sum, it is greater than 50% median salary) <br/>Blank - no data |
| | `E1_Flag` | | Binary flag for sectoral scope | 0 - formal sector workers only <br/>1 - transfers to informal sector workers too <br/>Blank - no data |
| E2 | `E2_Debt/contract relief` <br/>(for households) | Record if the government is freezing financial obligations for households (eg stopping loan repayments, preventing services like water from stopping, or banning evictions) | Ordinal scale | 0 - no debt/contract relief <br/>1 - narrow relief, specific to one kind of contract <br/>2 - broad debt/contract relief |
| E3 | `E3_Fiscal measures` | Announced economic stimulus spending <br/><br/>Note: only record amount additional to previously announced spending | USD | Record monetary value in USD of fiscal stimuli, includes any spending or tax cuts NOT included in E4, H4 or H5 <br/>0 - no new spending that day <br/>Blank - no data |
| E4 | `E4_International support` | Announced offers of Covid-19 related aid spending to other countries <br/><br/>Note: only record amount additional to previously announced spending | USD | Record monetary value in USD <br/>0 - no new spending that day <br/>Blank - no data |

### Health system policies

| ID | Name | Description | Measurement | Coding |
| --- | --- | --- | --- | --- |
| H1 | `H1_Public information campaigns` | Record presence of public info campaigns | Ordinal scale | 0 - no Covid-19 public information campaign <br/>1 - public officials urging caution about Covid-19 <br/>2- coordinated public information campaign (eg across traditional and social media) <br/>Blank - no data |
| | `H1_Flag` | | Binary flag for geographic scope |  0 - targeted <br/>1- general <br/>Blank - no data |
| H2 | `H2_Testing policy` | Record government policy on who has access to testing <br/><br/>Note: this records policies about testing for current infection (PCR tests) not testing for immunity (antibody test) | Ordinal scale | 0 - no testing policy <br/>1 - only those who both (a) have symptoms AND (b) meet specific criteria (eg key workers, admitted to hospital, came into contact with a known case, returned from overseas) <br/>2 - testing of anyone showing Covid-19 symptoms <br/>3 - open public testing (eg "drive through" testing available to asymptomatic people) <br/>Blank - no data |
| H3 | `H3_Contact tracing` | Record government policy on contact tracing after a positive diagnosis <br/><br/>Note: we are looking for policies that would identify all people potentially exposed to Covid-19; voluntary bluetooth apps are unlikely to achieve this | Ordinal scale | 0 - no contact tracing <br/>1 - limited contact tracing; not done for all cases <br/>2 - comprehensive contact tracing; done for all identified cases |
| H4 | `H4_Emergency investment in healthcare` | Announced short term spending on healthcare system, eg hospitals, masks, etc <br/><br/>Note: only record amount additional to previously announced spending | USD | Record monetary value in USD <br/>0 - no new spending that day <br/>Blank - no data |
| H5 | `H5_Investment in vaccines` | Announced public spending on Covid-19 vaccine development <br/><br/>Note: only record amount additional to previously announced spending | USD | Record monetary value in USD <br/>0 - no new spending that day <br/>Blank - no data |

### Miscellaneous policies

| ID | Name | Description | Measurement | Coding |
| --- | --- | --- | --- | --- |
| M1 | `M1_Wildcard` | Record policy announcements that do not fit anywhere else | Free text notes field | Note unusual or interesting interventions that are worth flagging  |

## Codebook changelog

- 22 May 2020: v2.2 changed description of E1=2 from "replacing more than 50% of lost salary" to "replacing 50% or more of lost salary"
- 11 May 2020: moved v2 codebook to GitHub


### Projects:
-------------
Visualization Dashboard provided by University of Oxford. [Link to Visualizations](https://covidtracker.bsg.ox.ac.uk/stringency-scatter)

### License:
-------------
This data is provided free of charge. More Info about the usage can be found the [webpage](https://www.bsg.ox.ac.uk/research/research-projects/coronavirus-government-response-tracker) of the dataset.

### Authors:
-------------
Contributors to the project include: Aditya Lolla, Ahmed Safar, Alejandrina Cripovich, Alfredo Ortega, Andrea Garaiova, Andrea Klaric, Andrew Wood, Anjali Viswamohanan, Anupah Makoond Makoond, Arkar Hein, Babu Ahamed, Barbara Roggeveen, Beatriz Kira, Ben Luria, Blessing Oluwatosin Ajimoti, Caroline Weglinski, Charlotte Rougier, Chloe Mayoux, Clara Pavillet, Connor Lyons, Dane Alivarius, Dario Moreira, Dita Listya, Eleanor Altamura, Emily Cameron-Blake, Fatima Zehra Naqvi, Femi Adebola, Finn Klebe, Francesca Lovell-Read, Francesca Valmorbida McSteen, Gabriel Podesta, Grace Mzumara, Guillermo Miranda, Hakeem Onasanya, Hala Sheikh Al Souk, Helen Tatlow, Huma Zile, Ilya Zlotnikov, Isabela Blumm, James Fox, James Green, Javier Pardo-Diaz, Jenna Hand, Jeroen Frijters, Jessica Anania, Joanna Klimczak, John Miller, Joseph Ssentongo, Juan David Gutierrez, Juhi Kore, Kangning Zhang, Katherine Tyson, Kaushalya Gupta, Kristie Jameson, Lana Ahmad, Laura Chavez-Varela, Liliana Estrada Galindo, Lin Shi, Lione Alushula, Liu Yang (Victoria), Lore Purroy Sanchez, Louisa-Madeline Singer, Lucia Soriano, Lucy Goodfellow, Marcela Reynoso Jurado, María de los Ángeles Lasa, Maria Paz Astigarraga Baez, Martina Lejtreger, Maurice Kirschbaum, Melody Leong, Michael Chen, Muktai Panchal, Natalia Espinola, Negin Shahiar, Oksana Matiiash, Olga Romanova, Pamela Gongora, Paola Del Carpio Ponce, Paola Schietekat Sedas, Patricia Silva Castillo, Pollyana Lima, Priya Lakshmy Tbalasubramaniam, Priyanka Bijlani, Qingling Kong, Rene' Landers, Robert Gorwa, Robin Thompson, Salim Salamah, Serene Singh, SeungCheol Ohk, Shabana Basij-Rasikh, Silvia Shen, Simphiwe Stewart, Siu Cheng, Sophie Pearlman, Syed Shoaib Hasan Rizvi, Tanyah Hameed, Tatsuya Yasui, Tebello Qhotsokoane, Tetsekela Anyiam-Osigwe, Tim Nusser, Tiphaine Le Corre, Twan van der Togt, Uttara Narayan, William Dowling, William Hart, Yulia Taranova, Zoe Lin and Zunaira Mallick 
