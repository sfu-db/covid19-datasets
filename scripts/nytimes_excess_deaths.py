import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport

#fill only the following 2 variables (PATH_TO_FILE and FINAL_FILE_NAME)
PATH_TO_FILE = "https://github.com/nytimes/covid-19-data/blob/master/excess-deaths/deaths.csv"
FINAL_FILE_NAME = "nytimes-excess-deaths"

# do not touch the rest of the code
FINAL_HTML_PATH = "../webpages/" + FINAL_FILE_NAME + ".html"

df = pd.read_csv(PATH_TO_FILE, error_bad_lines=False)
profile = ProfileReport(df, title=FINAL_FILE_NAME, explorative=True)
profile.to_file(FINAL_HTML_PATH)