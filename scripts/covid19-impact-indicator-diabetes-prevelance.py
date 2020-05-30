import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport

PATH_TO_FILE = "http://api.worldbank.org/v2/en/indicator/SH.STA.DIAB.ZS?downloadformat=excel"
FINAL_FILE_NAME = "impact-indicator"
FINAL_HTML_PATH = "../webpages/" + FINAL_FILE_NAME + ".html"

df = pd.ExcelFile(PATH_TO_FILE)
df1 = pd.read_excel(df,"Data")
profile = ProfileReport(df1, title=FINAL_FILE_NAME, explorative=True)
profile.to_file(FINAL_HTML_PATH)
