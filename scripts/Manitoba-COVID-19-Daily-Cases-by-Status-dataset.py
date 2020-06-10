import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport

PATH_TO_FILE = "Manitoba_COVID-19_Cases_by_Status.csv"
FINAL_FILE_NAME = "Manitoba-COVID-19-Daily-Cases-by-Status-dataset"
FINAL_HTML_PATH = "../webpages/" + FINAL_FILE_NAME + ".html"

df = pd.read_csv(PATH_TO_FILE, error_bad_lines=False)
print(df.info())
profile = ProfileReport(df, title=FINAL_FILE_NAME, explorative=True)
profile.to_file(FINAL_HTML_PATH)