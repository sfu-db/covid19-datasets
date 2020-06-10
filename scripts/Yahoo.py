import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport

#fill only the following 2 variables (PATH_TO_FILE and FINAL_FILE_NAME)
PATH_TO_FILE = "https://raw.githubusercontent.com/yahoo/covid-19-data/master/data/by-region-2020-06-09.json"
FINAL_FILE_NAME = "Yahoo_COVID-19"

# do not touch the rest of the code
FINAL_HTML_PATH = "../webpages/" + FINAL_FILE_NAME + ".html"

df = pd.read_json(PATH_TO_FILE, lines=True)
profile = ProfileReport(df, title=FINAL_FILE_NAME, explorative=True)
profile.to_file(FINAL_HTML_PATH)