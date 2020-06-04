import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport

PATH_TO_FILE = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
FINAL_FILE_NAME = "owiddataset"
FINAL_HTML_PATH = "../webpages/" + FINAL_FILE_NAME + ".html"

df = pd.read_csv(PATH_TO_FILE, error_bad_lines=False)
profile = ProfileReport(df, title=FINAL_FILE_NAME, explorative=True)
profile.to_file("../webpages/owiddataset.html")
