import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport

PATH_TO_FILE = "https://raw.githubusercontent.com/sammyhawkrad/ghana-covid-19-dataset/master/Ghana_Covid19_DailyActive.csv"
FINAL_FILE_NAME = "Ghana_COVID-19_Dataset"
FINAL_HTML_PATH = "../webpages/" + FINAL_FILE_NAME + ".html"

df = pd.read_csv(PATH_TO_FILE, error_bad_lines=False)
profile = ProfileReport(df, title=FINAL_FILE_NAME, explorative=True)
profile.to_file(FINAL_HTML_PATH)
